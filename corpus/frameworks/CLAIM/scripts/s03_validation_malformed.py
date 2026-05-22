"""
S-03 — Validation des CLAIM malformes
Projet IDEeS AP6-defi-13 — Protocole d'echange epistemique
Version : 1.0 — 18 mai 2026

Implemente la politique de validation B.1 de CLAIM_specification.md v1.1.
Teste la fonction validate_claim() sur des cas valides et invalides.

Usage : python s03_validation_malformed.py
"""

import re
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# Constantes de validation
# ---------------------------------------------------------------------------
THETA_LABELS = {"H1", "H2", "H3"}  # cadre de discernement Theta
VALID_ILLOCUTIONS = {"OBSERVE", "INFER", "DEDUCE", "ASSUME"}
MASS_TOLERANCE = 1e-6

# Pattern URI/URN minimal (RFC 3986 simplifie)
URI_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9+\-.]*:.+$")


# ---------------------------------------------------------------------------
# Utilitaire : analyser une cle de belief_mass (str)
# ---------------------------------------------------------------------------
def parse_mass_key(key: str) -> bool:
    """
    Valide qu'une cle de belief_mass est un sous-ensemble de Theta valide.
    Formats acceptes :
      "H1"         => {H1}
      "H1|H2"      => {H1, H2}
      "Theta"      => Theta (ensemble complet)
      "empty"      => ensemble vide
      "H1|H2|H3"   => Theta (equivalent)
    """
    if key == "empty" or key == "Theta":
        return True
    parts = key.split("|")
    return all(p in THETA_LABELS for p in parts)


# ---------------------------------------------------------------------------
# Fonction principale de validation
# ---------------------------------------------------------------------------
def validate_claim(claim: dict, now: datetime = None) -> tuple:
    """
    Valide un CLAIM selon la politique B.1 de CLAIM_specification.md.

    Parametres :
      claim : dict representant le CLAIM (format JSON Schema CLAIM_schema.json)
      now   : datetime de reference (UTC). Defaut : datetime.now(timezone.utc)

    Retourne :
      (True,  "")          si valide
      (False, "<message>") si invalide
    """
    if now is None:
        now = datetime.now(timezone.utc)

    # --- 1. Presence des champs obligatoires ---
    required = ["proposition", "belief_mass", "illocution", "freshness", "provenance"]
    for field in required:
        if field not in claim:
            return False, f"Champ obligatoire manquant : '{field}'"

    # --- 2. belief_mass : normalisation et cles ---
    bm = claim["belief_mass"]
    if not isinstance(bm, dict) or len(bm) == 0:
        return False, "belief_mass doit etre un objet non vide"

    for key in bm:
        if not parse_mass_key(str(key)):
            return False, f"belief_mass : cle invalide '{key}' (hors 2^Theta)"
        val = bm[key]
        if not isinstance(val, (int, float)) or val < 0.0 or val > 1.0:
            return False, f"belief_mass : valeur hors [0,1] pour cle '{key}'"

    total = sum(bm.values())
    if abs(total - 1.0) > MASS_TOLERANCE:
        return False, f"belief_mass : somme = {total:.8f} (attendu 1.0, tolerance {MASS_TOLERANCE})"

    # --- 3. illocution ---
    illocution = claim["illocution"]
    if illocution not in VALID_ILLOCUTIONS:
        return False, f"illocution invalide : '{illocution}' (valeurs admises : {sorted(VALID_ILLOCUTIONS)})"

    # --- 4. freshness ---
    freshness = claim["freshness"]
    if not isinstance(freshness, dict):
        return False, "freshness doit etre un objet"

    if "t_obs" not in freshness:
        return False, "freshness.t_obs manquant"

    t_obs_str = freshness["t_obs"]
    try:
        # Accepte ISO 8601 avec Z ou +00:00
        t_obs_str_norm = t_obs_str.replace("Z", "+00:00")
        t_obs = datetime.fromisoformat(t_obs_str_norm)
        if t_obs.tzinfo is None:
            t_obs = t_obs.replace(tzinfo=timezone.utc)
    except (ValueError, AttributeError):
        return False, f"freshness.t_obs : format ISO 8601 invalide ('{t_obs_str}')"

    if t_obs > now:
        return False, f"freshness.t_obs dans le futur : {t_obs_str}"

    if "delta_t_valid" not in freshness:
        return False, "freshness.delta_t_valid manquant"

    delta = freshness["delta_t_valid"]
    if not isinstance(delta, (int, float)) or delta < 0:
        return False, f"freshness.delta_t_valid negatif ou invalide : {delta}"

    # --- 5. provenance ---
    prov = claim["provenance"]
    if not isinstance(prov, dict):
        return False, "provenance doit etre un objet"

    chain_id = prov.get("chain_id", None)
    if not chain_id:
        return False, "provenance.chain_id absent ou vide"

    if not URI_PATTERN.match(str(chain_id)):
        return False, f"provenance.chain_id n'est pas une URI/URN valide : '{chain_id}'"

    return True, ""


# ---------------------------------------------------------------------------
# Cas de test
# ---------------------------------------------------------------------------
def run_tests():
    """Execute les cas de test de la politique B.1."""

    now_ref = datetime(2026, 5, 18, 12, 0, 0, tzinfo=timezone.utc)

    # Cas valide (exemple tire du CLAIM_schema.json)
    claim_valid = {
        "proposition": "Aucune signature acoustique detectee dans le secteur Nord-B",
        "belief_mass": {
            "H1": 0.7,
            "Theta": 0.3,
            "empty": 0.0,
        },
        "illocution": "OBSERVE",
        "freshness": {
            "t_obs": "2026-05-17T14:32:00Z",
            "delta_t_valid": 60,
        },
        "provenance": {
            "chain_id": "urn:idees:agent:sonar-tribord:chain:20260517T143200Z",
        },
    }

    # Masse non normalisee (somme = 1.1)
    claim_bad_mass = {
        "proposition": "Test masse non normalisee",
        "belief_mass": {"H1": 0.8, "H2": 0.3},  # somme = 1.1
        "illocution": "OBSERVE",
        "freshness": {"t_obs": "2026-05-17T14:32:00Z", "delta_t_valid": 60},
        "provenance": {"chain_id": "urn:idees:test:001"},
    }

    # Timestamp manquant
    claim_no_timestamp = {
        "proposition": "Test timestamp manquant",
        "belief_mass": {"H1": 0.7, "Theta": 0.3},
        "illocution": "INFER",
        "freshness": {"delta_t_valid": 60},  # t_obs absent
        "provenance": {"chain_id": "urn:idees:test:002"},
    }

    # delta_t_valid negatif
    claim_negative_delta = {
        "proposition": "Test delta negatif",
        "belief_mass": {"H1": 0.7, "Theta": 0.3},
        "illocution": "DEDUCE",
        "freshness": {"t_obs": "2026-05-17T14:32:00Z", "delta_t_valid": -10},
        "provenance": {"chain_id": "urn:idees:test:003"},
    }

    # Provenance absente
    claim_no_provenance = {
        "proposition": "Test provenance absente",
        "belief_mass": {"H1": 0.7, "Theta": 0.3},
        "illocution": "ASSUME",
        "freshness": {"t_obs": "2026-05-17T14:32:00Z", "delta_t_valid": 60},
        # champ 'provenance' absent
    }

    # Illocution invalide
    claim_bad_illocution = {
        "proposition": "Test illocution invalide",
        "belief_mass": {"H1": 0.7, "Theta": 0.3},
        "illocution": "GUESS",  # hors enumeration
        "freshness": {"t_obs": "2026-05-17T14:32:00Z", "delta_t_valid": 60},
        "provenance": {"chain_id": "urn:idees:test:005"},
    }

    test_cases = [
        ("VALIDE       - exemple nominal",            claim_valid,           True),
        ("REJET        - masse non normalisee",        claim_bad_mass,        False),
        ("REJET        - timestamp manquant",          claim_no_timestamp,    False),
        ("REJET        - delta_t_valid negatif",       claim_negative_delta,  False),
        ("REJET        - provenance absente",          claim_no_provenance,   False),
        ("REJET        - illocution invalide",         claim_bad_illocution,  False),
    ]

    print("=" * 70)
    print("S-03 — Validation des CLAIM malformes (politique B.1)")
    print("=" * 70)
    print(f"\nHorodatage de reference : {now_ref.isoformat()}\n")

    all_pass = True
    for description, claim, expected_valid in test_cases:
        valid, msg = validate_claim(claim, now=now_ref)
        status_ok = (valid == expected_valid)
        marker = "[OK]    " if status_ok else "[ECHEC] "
        result  = "[VALIDE]" if valid else f"[REJET] {msg}"
        print(f"  {marker} {description}")
        print(f"           => {result}")
        if not status_ok:
            all_pass = False
            print(f"           !! ATTENDU {'VALIDE' if expected_valid else 'REJET'} — GOT {'VALIDE' if valid else 'REJET'}")
        print()

    print("=" * 70)
    if all_pass:
        print("BILAN : tous les cas de test passent — politique B.1 conforme.")
    else:
        print("BILAN : des cas de test ont echoue — revoir l'implementation.")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()