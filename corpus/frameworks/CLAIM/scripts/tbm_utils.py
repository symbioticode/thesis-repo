"""
tbm_utils.py — Module commun TBM / CLAIM
Projet IDEeS AP6-defi-13 — Protocole d'echange epistemique
Version : 1.0 — 18 mai 2026
Prerequis : Python 3.9+, aucune dependance externe.
"""

from itertools import combinations

# ---------------------------------------------------------------------------
# Cadre de discernement commun
# ---------------------------------------------------------------------------
THETA = frozenset({"H1", "H2", "H3"})
EMPTY = frozenset()
THETA_CONFLIT_DEFAULT = 0.3  # valeur NMT-2 conservative


def all_subsets(universe: frozenset) -> list:
    """Retourne tous les sous-ensembles de universe, y compris vide et universe."""
    elems = list(universe)
    subs = [EMPTY]
    for r in range(1, len(elems) + 1):
        for combo in combinations(elems, r):
            subs.append(frozenset(combo))
    return subs


ALL_SUBSETS: list = all_subsets(THETA)


# ---------------------------------------------------------------------------
# Validation BBA
# ---------------------------------------------------------------------------
def validate_bba(bba: dict, name: str) -> None:
    """Verifie qu'une BBA est normalisee a 1 et definie sur 2^Theta. Leve AssertionError sinon."""
    total = sum(bba.values())
    assert abs(total - 1.0) < 1e-9, (
        f"[ERREUR] {name} : masse non normalisee (somme = {total:.6f})"
    )
    for key in bba:
        assert key in ALL_SUBSETS or key == EMPTY, (
            f"[ERREUR] {name} : cle hors de 2^Theta"
        )
    print(f"[OK] {name} : masse valide (somme = {total:.6f})")


def normalize_keys(bba: dict) -> dict:
    """Complete un dict BBA avec les sous-ensembles manquants a 0.0."""
    full = {s: 0.0 for s in ALL_SUBSETS}
    full[EMPTY] = 0.0
    full.update(bba)
    return full


# ---------------------------------------------------------------------------
# Regle de combinaison conjonctive non normalisee (Smets / TBM)
# ---------------------------------------------------------------------------
def tbm_conjunctive(m1: dict, m2: dict) -> dict:
    """
    Combine deux masses par la regle conjonctive non normalisee.
    m_combined(A) = sum_{B inter C = A} m1(B) * m2(C)
    m(vide) est conserve — jamais normalise.
    """
    combined = {s: 0.0 for s in ALL_SUBSETS}
    combined[EMPTY] = 0.0
    for B, mB in m1.items():
        if mB == 0.0:
            continue
        for C, mC in m2.items():
            if mC == 0.0:
                continue
            inter = B & C
            combined[inter] = combined.get(inter, 0.0) + mB * mC
    return combined


# ---------------------------------------------------------------------------
# Derivation etat Belnap
# ---------------------------------------------------------------------------
def derive_belnap(combined: dict, theta: float = THETA_CONFLIT_DEFAULT) -> str:
    """
    Derive l'etat Belnap selon CORR-TP01-06.
    Priorite decroissante : B > N > T/F > N (defaut conservateur).

    B : m(vide) >= theta  => contradiction, escalade obligatoire
    N : m(Theta) domine tous les singletons => silence qualifie
    T : m({H}) > 0.5 et m(vide) ~ 0       => accord sur H
    N : defaut conservateur
    """
    m_empty = combined.get(EMPTY, 0.0)
    if m_empty >= theta:
        return "B"
    m_theta = combined.get(THETA, 0.0)
    singletons = {h: combined.get(frozenset({h}), 0.0) for h in THETA}
    if m_theta > max(singletons.values(), default=0.0):
        return "N"
    for h, mass in singletons.items():
        if mass > 0.5 and m_empty < 1e-6:
            return f"T (accord sur {h})"
    return "N"


# ---------------------------------------------------------------------------
# Localisation PCR5 simplifiee (NMT-2)
# ---------------------------------------------------------------------------
def pcr5_sources(m1: dict, m2: dict, agent1: str, agent2: str) -> list:
    """
    Identifie les paires d'hypotheses generatrices de conflit.
    Retourne liste de dicts : {agent_i, agent_j, H_i, H_j, contribution}.
    Version NMT-2 : liste des intersections vides. PCR5 complet en NMT-4.
    """
    conflicts = []
    for B, mB in m1.items():
        if mB == 0.0 or B in (EMPTY, THETA):
            continue
        for C, mC in m2.items():
            if mC == 0.0 or C in (EMPTY, THETA):
                continue
            if B & C == EMPTY and B != C:
                contrib = mB * mC
                if contrib > 0.0:
                    conflicts.append({
                        "agent_i": agent1, "agent_j": agent2,
                        "H_i": set(B), "H_j": set(C),
                        "contribution": round(contrib, 6),
                    })
    return conflicts


def print_claim(name: str, bba: dict) -> None:
    """Affiche une BBA sur la console."""
    print(f"\n  CLAIM [{name}]")
    for subset, mass in sorted(bba.items(), key=lambda x: (len(x[0]), str(sorted(x[0])))):
        if mass > 0.0 or subset == EMPTY:
            label = "{vide}" if subset == EMPTY else "{" + ", ".join(sorted(subset)) + "}"
            print(f"    m({label}) = {mass:.4f}")