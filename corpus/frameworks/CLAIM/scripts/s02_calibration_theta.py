"""
S-02 — Calibration de theta_conflit
Projet IDEeS AP6-defi-13 — Protocole d'echange epistemique
Version : 2.0 — 18 mai 2026

Correctif DOOM (feedback 18 mai 2026) :
  v1.0 avait un corpus trivial : les cas non-conflictuels donnaient m(vide)=0
  pour tous les seuils => FPR=0.000, recommandation artefact.

  v2.0 introduit un troisieme type de cas : AMBIGU.
  Definition : supports disjoints (m(vide) > 0) mais etiquete non-conflit,
  simulant deux capteurs observant des entites distinctes (pas de desaccord
  sur la meme entite). Ce cas genere des faux positifs potentiels pour theta bas.

Limite connue (AM-04) :
  Le corpus reste synthetique. La frontiere alpha=0.6 entre cas ambigu
  et cas conflit est artificielle. Calibration sur donnees reelles : NMT-3.

Usage : python s02_calibration_theta.py
"""

import random
from tbm_utils import (
    THETA, EMPTY, normalize_keys, tbm_conjunctive, THETA_CONFLIT_DEFAULT,
)


# ---------------------------------------------------------------------------
# 1. Generateur de paires de masses synthetiques
# ---------------------------------------------------------------------------
def generer_masses_conflit(prob_conflict: float, prob_ambiguous: float,
                           rng: random.Random) -> tuple:
    """
    Retourne (m1, m2, is_conflict) avec trois categories :

    CONFLIT (prob_conflict) :
      Supports disjoints {H1} vs {H2}, croyance forte (alpha in [0.6, 0.9]).
      Etiquete is_conflict=True.
      => m(vide) = alpha1 * alpha2 in [0.36, 0.81]

    AMBIGU (prob_ambiguous) :
      Supports disjoints {H1} vs {H2}, croyance MODEREE (alpha in [0.4, 0.6]).
      Etiquete is_conflict=False.
      Semantique : deux capteurs observant des entites distinctes —
      mathematiquement generateur de m(vide) > 0 mais sans conflit reel.
      => m(vide) = alpha1 * alpha2 in [0.16, 0.36]
      => Source de faux positifs pour les seuils bas.

    NON-CONFLIT SIMPLE (1 - prob_conflict - prob_ambiguous) :
      Accord sur le meme singleton ou incertitude globale.
      => m(vide) = 0 par construction.
      Etiquete is_conflict=False.

    Hypothese du corpus (AM-04) :
      La frontiere alpha=0.6 entre AMBIGU et CONFLIT est artificielle.
      En donnees ISR reelles, la distribution est continue sans seuil net.
    """
    assert prob_conflict + prob_ambiguous <= 1.0, \
        "prob_conflict + prob_ambiguous doit etre <= 1.0"

    r = rng.random()

    if r < prob_conflict:
        # Conflit reel : forte croyance sur des singletons disjoints
        alpha1 = rng.uniform(0.6, 0.9)
        alpha2 = rng.uniform(0.6, 0.9)
        m1 = normalize_keys({frozenset({"H1"}): alpha1, THETA: 1.0 - alpha1})
        m2 = normalize_keys({frozenset({"H2"}): alpha2, THETA: 1.0 - alpha2})
        is_conflict = True

    elif r < prob_conflict + prob_ambiguous:
        # Cas ambigu : supports disjoints, croyance moderee, etiquete non-conflit
        alpha1 = rng.uniform(0.4, 0.6)
        alpha2 = rng.uniform(0.4, 0.6)
        m1 = normalize_keys({frozenset({"H1"}): alpha1, THETA: 1.0 - alpha1})
        m2 = normalize_keys({frozenset({"H2"}): alpha2, THETA: 1.0 - alpha2})
        is_conflict = False

    else:
        # Non-conflit simple : accord sur meme singleton ou incertitude globale
        if rng.random() < 0.5:
            alpha1 = rng.uniform(0.4, 0.8)
            alpha2 = rng.uniform(0.4, 0.8)
            m1 = normalize_keys({frozenset({"H1"}): alpha1, THETA: 1.0 - alpha1})
            m2 = normalize_keys({frozenset({"H1"}): alpha2, THETA: 1.0 - alpha2})
        else:
            m1 = normalize_keys({THETA: 1.0})
            m2 = normalize_keys({THETA: 1.0})
        is_conflict = False

    return m1, m2, is_conflict


# ---------------------------------------------------------------------------
# 2. Calcul du taux de faux positifs pour un seuil donne
# ---------------------------------------------------------------------------
def taux_faux_positifs(theta: float, n_pairs: int, prob_conflict: float,
                        prob_ambiguous: float, rng: random.Random) -> float:
    """
    FPR = (escalades declenchees sur paires non-conflictuelles) /
          (nombre total de paires non-conflictuelles)

    Les cas ambigus (m(vide) > 0 mais etiquetes non-conflit) contribuent au FPR.
    """
    fp = 0
    tn = 0
    for _ in range(n_pairs):
        m1, m2, is_conflict = generer_masses_conflit(prob_conflict, prob_ambiguous, rng)
        combined = tbm_conjunctive(m1, m2)
        m_empty = combined.get(EMPTY, 0.0)
        escalade = m_empty >= theta

        if not is_conflict:
            tn += 1
            if escalade:
                fp += 1

    return fp / tn if tn > 0 else 0.0


# ---------------------------------------------------------------------------
# 3. Calcul du taux de vrais positifs (sensibilite) pour un seuil donne
# ---------------------------------------------------------------------------
def taux_vrais_positifs(theta: float, n_pairs: int, prob_conflict: float,
                         prob_ambiguous: float, rng: random.Random) -> float:
    """
    TPR = (escalades declenchees sur paires conflictuelles) /
          (nombre total de paires conflictuelles)
    """
    tp = 0
    pos = 0
    for _ in range(n_pairs):
        m1, m2, is_conflict = generer_masses_conflit(prob_conflict, prob_ambiguous, rng)
        combined = tbm_conjunctive(m1, m2)
        m_empty = combined.get(EMPTY, 0.0)
        escalade = m_empty >= theta

        if is_conflict:
            pos += 1
            if escalade:
                tp += 1

    return tp / pos if pos > 0 else 0.0


# ---------------------------------------------------------------------------
# 4. Execution principale
# ---------------------------------------------------------------------------
def main():
    print("=" * 70)
    print("S-02 v2.0 — Calibration de theta_conflit (IDEeS Defi 13)")
    print("Corpus v2 : 3 categories (conflit / ambigu / non-conflit simple)")
    print("=" * 70)

    N_PAIRS = 1000          # augmente pour reduire la variance Monte-Carlo
    PROB_CONFLICT  = 0.40   # 40% vrais conflits
    PROB_AMBIGUOUS = 0.30   # 30% cas ambigus (faux positifs potentiels)
    # restant 30% : non-conflits simples (m(vide)=0 par construction)
    SEED = 42

    seuils = [round(0.05 * i + 0.10, 2) for i in range(9)]  # [0.10 .. 0.50]

    print("\nParametres :")
    print(f"  N_PAIRS        = {N_PAIRS} paires par seuil")
    print(f"  PROB_CONFLICT  = {PROB_CONFLICT} — alpha in [0.6, 0.9], m(vide) in [0.36, 0.81]")
    print(f"  PROB_AMBIGUOUS = {PROB_AMBIGUOUS} — alpha in [0.4, 0.6], m(vide) in [0.16, 0.36]")
    print(f"  PROB_SIMPLE    = {1-PROB_CONFLICT-PROB_AMBIGUOUS:.2f} — m(vide)=0 par construction")
    print(f"  SEED           = {SEED} (reproductible)")
    print()
    print("  Note AM-04 : la frontiere alpha=0.6 entre AMBIGU et CONFLIT")
    print("  est artificielle. Ce corpus reste synthetique (NMT-3 : donnees reelles).")
    print("\nResultats :")
    print("-" * 70)
    print(f"  {'Seuil theta':>12}  {'FPR (faux positifs)':>22}  {'TPR (vrais positifs)':>22}")
    print("-" * 70)

    results = []
    for theta in seuils:
        rng_fpr = random.Random(SEED)
        rng_tpr = random.Random(SEED + 1)
        fpr = taux_faux_positifs(theta, N_PAIRS, PROB_CONFLICT, PROB_AMBIGUOUS, rng_fpr)
        tpr = taux_vrais_positifs(theta, N_PAIRS, PROB_CONFLICT, PROB_AMBIGUOUS, rng_tpr)
        results.append((theta, fpr, tpr))
        flag = " <-- seuil cible" if abs(theta - 0.30) < 0.01 else ""
        print(f"  theta = {theta:.2f}      FPR = {fpr:.3f}                    TPR = {tpr:.3f}{flag}")

    print("-" * 70)

    # Recommandation : premier seuil avec FPR <= 0.05 et TPR >= 0.80
    recommended = None
    for theta, fpr, tpr in results:
        if fpr <= 0.05 and tpr >= 0.80:
            recommended = (theta, fpr, tpr)
            break

    print("\nRecommandation :")
    if recommended:
        theta_r, fpr_r, tpr_r = recommended
        print(f"  Seuil recommande : theta_conflit = {theta_r}")
        print(f"  FPR = {fpr_r:.3f} (<= 0.05)  |  TPR = {tpr_r:.3f} (>= 0.80)")
        print(f"  Justification : premier seuil satisfaisant FPR<=0.05 et TPR>=0.80.")
        if abs(theta_r - 0.30) > 0.01:
            print(f"  Attention : recommandation = {theta_r}, PAS 0.30.")
            print(f"  La valeur 0.30 donne FPR={[r[1] for r in results if abs(r[0]-0.30)<0.01][0]:.3f} > 0.05.")
    else:
        print("  Aucun seuil ne satisfait FPR<=0.05 et TPR>=0.80 sur ce corpus.")
        print("  Valeur conservative 0.30 maintenue par argument operationnel (AM-04).")

    print()
    print("Limite du corpus (AM-04) :")
    print("  La frontiere alpha=0.6 cree une separation artificielle entre cas")
    print("  ambigu (m(vide) max=0.36) et cas conflit (m(vide) min=0.36).")
    print("  En donnees ISR reelles, cette frontiere est continue, sans seuil net.")
    print("  Calibration sur donnees reelles (MSTAR ou equivalent) : NMT-3.")
    print("=" * 70)


if __name__ == "__main__":
    main()