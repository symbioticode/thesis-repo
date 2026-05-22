"""
S-01 — Scénario synthétique minimum : fusion TBM non normalisée
Projet IDEeS AP6-défi-13 — Protocole d'échange épistémique
Version : 1.0 — 17 mai 2026

Deux agents (Radar, SIGINT) sur cadre de discernement Theta = {H1, H2, H3}
  H1 : objet militaire
  H2 : objet civil
  H3 : inconnu (etat ouvert)

Masses initiales :
  Radar  : m({H1}) = 0.7,  m(Theta) = 0.3
  SIGINT : m({H2}) = 0.6,  m(Theta) = 0.4

Regle de combinaison : conjonctive NON NORMALISEE (Smets / TBM)
  m_combined(A) = sum_{B inter C = A} m1(B) * m2(C)  pour tout A inclus dans Theta
  m(vide) est CONSERVE — jamais normalise.

Seuil d'escalade : theta_conflit = 0.3
  Si m_combined(vide) >= theta_conflit → escalade humaine obligatoire.

Prerequis : Python 3.8+, aucune librairie externe requise.
Usage    : python s01_tbm_minimal.py
"""

from itertools import combinations


# ---------------------------------------------------------------------------
# 1. Definition du cadre de discernement
# ---------------------------------------------------------------------------
THETA = frozenset({"H1", "H2", "H3"})  # cadre de discernement commun
EMPTY = frozenset()  # ensemble vide — conflit explicite


def all_subsets(universe: frozenset) -> list:
    """Retourne tous les sous-ensembles de universe, y compris vide et universe."""
    elements = list(universe)
    subsets = [EMPTY]
    for r in range(1, len(elements) + 1):
        for combo in combinations(elements, r):
            subsets.append(frozenset(combo))
    return subsets


ALL_SUBSETS = all_subsets(THETA)


def validate_bba(bba: dict, name: str) -> None:
    """Verifie que la masse est bien definie sur 2^Theta et normalisee a 1."""
    total = sum(bba.values())
    assert (
        abs(total - 1.0) < 1e-9
    ), f"[ERREUR] {name} : masse non normalisee (somme = {total:.6f})"
    for key in bba:
        assert (
            key in ALL_SUBSETS or key == EMPTY
        ), f"[ERREUR] {name} : cle '{key}' hors de 2^Theta"
    print(f"[OK] {name} : masse valide (somme = {total:.6f})")


# ---------------------------------------------------------------------------
# 2. Definition des CLAIM (masses de croyance des agents)
# ---------------------------------------------------------------------------
# Toutes les cles non listees ont masse 0.0

bba_radar = {
    frozenset({"H1"}): 0.7,  # Radar tres confiant sur objet militaire
    THETA: 0.3,  # Incertitude residuelle sur toutes hypotheses
    EMPTY: 0.0,  # Conflit initial nul
}

bba_sigint = {
    frozenset({"H2"}): 0.6,  # SIGINT confiant sur objet civil
    THETA: 0.4,  # Incertitude residuelle
    EMPTY: 0.0,
}


# Normaliser : s'assurer que toutes les cles de 2^Theta sont presentes (masse 0 sinon)
def normalize_keys(bba: dict) -> dict:
    full = {s: 0.0 for s in ALL_SUBSETS}
    full[EMPTY] = 0.0
    full.update(bba)
    return full


bba_radar = normalize_keys(bba_radar)
bba_sigint = normalize_keys(bba_sigint)


# ---------------------------------------------------------------------------
# 3. Regle de combinaison conjonctive NON normalisee (Smets TBM)
# ---------------------------------------------------------------------------
def tbm_conjunctive(m1: dict, m2: dict) -> dict:
    """
    Combine deux masses par la regle conjonctive non normalisee.
    m_combined(A) = sum_{B inter C = A} m1(B) * m2(C)
    L'ensemble vide est traite comme tout autre element de 2^Theta.
    """
    combined = {s: 0.0 for s in ALL_SUBSETS}
    combined[EMPTY] = 0.0

    # all_keys = list(ALL_SUBSETS) + [EMPTY]

    for B, mB in m1.items():
        if mB == 0.0:
            continue
        for C, mC in m2.items():
            if mC == 0.0:
                continue
            intersection = B & C  # vide si B et C sont disjoints
            combined[intersection] = combined.get(intersection, 0.0) + mB * mC

    return combined


# ---------------------------------------------------------------------------
# 4. Derivation de l'etat Belnap (EPISTEMIC_STATE)
# ---------------------------------------------------------------------------
THETA_CONFLIT = 0.3  # seuil configurable — valeur par defaut NMT-2


def derive_belnap(combined: dict, theta: float = THETA_CONFLIT) -> str:
    """
    Derive l'etat Belnap a partir de m_combined selon les regles CORR-TP01-06.
    Priorite decroissante : B > N > T/F

    B : contradiction — m(vide) >= theta_conflit
    N : silence qualifie collectif — m(Theta) domine tous les singletons
    T : accord sur H — m({H}) > 0.5 et m(vide) ≈ 0
    F : accord sur ¬H (complement du cas T)
    N (defaut conservateur) : aucune condition satisfaite
    """
    m_empty = combined.get(EMPTY, 0.0)

    # Priorite 1 : contradiction
    if m_empty >= theta:
        return "B"

    # Priorite 2 : silence qualifie collectif
    m_theta = combined.get(THETA, 0.0)
    m_singletons = {h: combined.get(frozenset({h}), 0.0) for h in THETA}
    if m_theta > max(m_singletons.values(), default=0.0):
        return "N"

    # Priorite 3 : accord sur une hypothese
    for h, mass in m_singletons.items():
        if mass > 0.5 and m_empty < 1e-6:
            return f"T (accord sur {h})"

    # Defaut conservateur
    return "N"


# ---------------------------------------------------------------------------
# 5. Localisation PCR5 simplifiee (identification des paires en conflit)
# ---------------------------------------------------------------------------
def pcr5_sources(m1: dict, m2: dict, agent1: str, agent2: str) -> list:
    """
    Identifie les paires d'hypotheses qui ont genere le conflit.
    Retourne une liste de triplets (agent_i, agent_j, hypothese_conflit).
    PCR5 complet necessite redistribution proportionnelle — ici on liste
    les intersections vides generatrices (version NMT-2).
    """
    conflicts = []
    for B, mB in m1.items():
        if mB == 0.0 or B == EMPTY or B == THETA:
            continue
        for C, mC in m2.items():
            if mC == 0.0 or C == EMPTY or C == THETA:
                continue
            if B & C == EMPTY and B != C:
                contribution = mB * mC
                if contribution > 0.0:
                    conflicts.append(
                        {
                            "agent_i": agent1,
                            "agent_j": agent2,
                            "H_i": set(B),
                            "H_j": set(C),
                            "contribution": round(contribution, 6),
                        }
                    )
    return conflicts


# ---------------------------------------------------------------------------
# 6. Affichage structure du CLAIM (format portail)
# ---------------------------------------------------------------------------
def print_claim(name: str, bba: dict) -> None:
    print(f"\n  CLAIM [{name}]")
    for subset, mass in sorted(
        bba.items(), key=lambda x: (len(x[0]), str(sorted(x[0])))
    ):
        if mass > 0.0 or subset == EMPTY:
            label = (
                "{vide}" if subset == EMPTY else ("{" + ", ".join(sorted(subset)) + "}")
            )
            print(f"    m({label}) = {mass:.4f}")


# ---------------------------------------------------------------------------
# 7. Execution principale
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("S-01 — Fusion TBM non normalisee (IDEeS Defi 13)")
    print("Protocole d'echange epistemique — NMT-2 -> NMT-3")
    print("=" * 60)

    # Validation des masses d'entree
    print("\n--- Validation des CLAIM entrants (B.1) ---")
    validate_bba(bba_radar, "Agent Radar")
    validate_bba(bba_sigint, "Agent SIGINT")

    # Affichage des CLAIM
    print("\n--- CLAIM emis par les agents ---")
    print_claim("Radar", bba_radar)
    print_claim("SIGINT", bba_sigint)

    # Combinaison TBM non normalisee
    combined = tbm_conjunctive(bba_radar, bba_sigint)

    # Verification algebrique : somme doit etre 1.0
    total_combined = sum(combined.values())
    print("\n--- Verification algebrique ---")
    print(f"  Somme m_combined : {total_combined:.6f} (attendu : 1.000000)")
    assert abs(total_combined - 1.0) < 1e-9, "ERREUR : combinaison non normalisee"
    print("  [OK] Conservation de la masse verifiee")

    # Affichage de l'EPISTEMIC_STATE
    print("\n--- EPISTEMIC_STATE (orchestrateur -> interface C-07) ---")
    m_empty = combined.get(EMPTY, 0.0)
    print(f"  conflict_mass  m(vide) = {m_empty:.4f}")
    print(f"  theta_conflit          = {THETA_CONFLIT}")

    for subset, mass in sorted(
        combined.items(), key=lambda x: (len(x[0]), str(sorted(x[0])))
    ):
        if mass > 1e-9:
            label = (
                "{vide}" if subset == EMPTY else ("{" + ", ".join(sorted(subset)) + "}")
            )
            marker = " <-- CONFLIT" if subset == EMPTY else ""
            print(f"  m_combined({label}) = {mass:.4f}{marker}")

    # Etat Belnap
    belnap = derive_belnap(combined)
    print(f"\n  belnap_state = {belnap}")

    # Localisation PCR5
    pcr5 = pcr5_sources(bba_radar, bba_sigint, "Radar", "SIGINT")
    print("\n--- Localisation PCR5 (conflits par paire d'agents) ---")
    if pcr5:
        for entry in pcr5:
            print(
                f"  Conflit : {entry['agent_i']} ({set(entry['H_i'])}) "
                f"vs {entry['agent_j']} ({set(entry['H_j'])}) "
                f"| contribution = {entry['contribution']:.4f}"
            )
    else:
        print("  Aucun conflit localise.")

    # Verdict final
    print("\n" + "=" * 60)
    if m_empty >= THETA_CONFLIT:
        print("VERDICT : ESCALADE HUMAINE REQUISE")
        print(f"  m(vide) = {m_empty:.4f} >= theta_conflit = {THETA_CONFLIT}")
        print("  L'orchestrateur suspend toute decision automatique.")
        print("  L'etat de conflit est expose a l'operateur (C-07).")
    else:
        print(f"VERDICT : Pas d'escalade (m(vide) = {m_empty:.4f} < {THETA_CONFLIT})")
    print("=" * 60)


if __name__ == "__main__":
    main()
