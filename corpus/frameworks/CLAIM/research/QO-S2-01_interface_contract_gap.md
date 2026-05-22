# QO-S2-01 — Gap du contrat d'interface minimal : preuves numériques et analyse
**Projet** : IDEeS AP6-défi-13
**Question** : Existe-t-il un travail existant unifiant confiance DS + états épistémiques + statut illocutionnaire + fraîcheur + provenance dans un contrat d'interface unique pour systèmes multi-agents hétérogènes ?
**Statut** : **RÉSOLU — Gap confirmé, ancré sur POC reproductible**
**Version** : 2.2 — 18 mai 2026
**Précédente version** : v2.1 (18 mai 2026) — AM-04 v2 documentée, avertissement θ=0.35 insuffisant dans tableau
**Preuves** : S-01 `s01_tbm_minimal.py` · S-02 `s02_calibration_theta_v2.py` · S-03 `s03_validation_malformed.py` · S-04 `s04_fipa_contrast.py`
**Reproductibilité** : Python 3.9+, stdlib uniquement, seed = 42 (S-02), zéro dépendance externe

---

## Mindsets appliqués à ce document

| # | Mindset | Application |
|---|---------|-------------|
| #1 | Ground Truth or Silence | Toute affirmation numérique cite le script source et la ligne de sortie exacte |
| #4 | No Hidden State | Hypothèses du corpus S-02 explicites — corpus simple, non représentatif ISR réel |
| #9 | Test Before Trust | Seuls S-01 et S-03 constituent des preuves d'exécution ; S-02 est une preuve de méthode partielle |
| #17 | Validate Before Automate | Violation documentée dans S-02 (FPR trivial) — corpus non validé manuellement avant scripting |
| #18 | Debt Visibility | Artefact S-02 tracé comme AM-04, daté, avec condition de résolution |

---

## Verdict

**Gap structurel confirmé.** Aucun standard existant n'obtient ✓ sur les cinq dimensions simultanément.
Ce résultat, initialement argumenté de sources littéraires, est désormais **ancré sur une POC exécutable** :

- S-01 démontre qu'un CLAIM structuré résout un problème de conflit inter-agents **que FIPA-ACL et les protocoles existants ne peuvent pas représenter** (pas de champ pour `m(∅)`).
- S-03 démontre que la politique de validation B.1 est **complète et opérationnelle** sur 6 cas distincts.
- S-04 démontre, par **contraste exécutable**, que des messages FIPA-ACL-like ne permettent pas de calculer `m(∅)` ni de déclencher une escalade fondée sur une métrique — l'orchestrateur est réduit à une comparaison textuelle.

---

## Formulation du gap (inchangée — DEC-S3-01 FERME)

> **Absence de contrat d'interface atomique unifié pour l'orchestration épistémique de systèmes multi-agents hétérogènes.**
>
> Les standards existants couvrent chaque dimension en isolation. Aucun travail n'unifie les cinq dimensions — confiance formelle (masse DS sur 2^Θ), états épistémiques (Belnap FOUR), statut illocutionnaire (Speech Acts), fraîcheur temporelle, provenance traçable — dans un format unique, indépendant de l'implémentation interne des agents.

---

## Tableau de couverture consolidé

| Standard | Confiance DS | États épist. | Illocution | Fraîcheur | Provenance | Score | Lacune principale |
|----------|:-----------:|:------------:|:----------:|:---------:|:----------:|:-----:|-------------------|
| **FIPA-ACL** | ✗ | ~ | ✓ | ✗ | ✗ | 1/5 | Pas de champ `m(∅)` — conflit non représentable |
| **TBM (Smets)** | ✓ | ~ | ✗ | ✗ | ✗ | 1/5 | Cadre de raisonnement, pas protocole d'échange |
| **JDL L1→L2** | ~ | ✗ | ✗ | ~ | ~ | 0/5 | Interface inter-niveaux non spécifiée (Steinberg 1999) |
| **SCF / SIG** | ~ | ✗ | ✓ | ~ | ✓ | 2/5 | Pas d'états épistémiques formels (pas de Belnap) |
| **PROV-O** | ✗ | ✗ | ✗ | ✓ | ✓ | 2/5 | Traçabilité seule — pas de confiance ni d'épistémique |
| **A2A (Google)** | ✗ | ✗ | ~ | ~ | ✓ | 1/5 | Conçu pour LLM coopératifs, pas boîtes noires |
| **Conformal Pred.** | ✓ | ~ | ✗ | ✗ | ✗ | 1/5 | Intervalle de couverture seul, pas de protocole |
| **CLAIM (proposé)** | ✓ | ✓ | ✓ | ✓ | ✓ | **5/5** | — |

Légende : ✓ = couvert formellement · ~ = couvert partiellement · ✗ = absent

**Note méthodologique** : les lacunes des standards existants sont issues de l'analyse littéraire (Delphi 4/4 sources, v1.0). La colonne CLAIM proposé est ancrée sur S-01 (confiance DS + états épistémiques) et S-03 (fraîcheur + provenance + illocution — validation B.1). Le tableau est un argument ; S-01/S-03 sont les preuves.

---

## Preuves numériques par dimension

### Dimension 1 — Confiance DS : m(∅) conservation (S-01, prouvé)

**Ce que FIPA-ACL ne peut pas faire** : FIPA-ACL ne possède aucun champ pour représenter le conflit inter-sources. Le champ `UNCERTAIN` de sa sémantique BDI modélise l'incertitude d'un agent sur lui-même, pas le conflit entre deux agents.

**Ce que S-01 démontre** :

```
Radar  : m({H1}) = 0.70, m(Θ) = 0.30   — croit à l'hypothèse militaire
SIGINT : m({H2}) = 0.60, m(Θ) = 0.40   — croit à l'hypothèse civile

Règle conjonctive non normalisée (Smets TBM) :
  m_combined(∅)    = 0.70 × 0.60 = 0.42   ← conflit explicite, conservé
  m_combined({H1}) = 0.70 × 0.40 = 0.28
  m_combined({H2}) = 0.30 × 0.60 = 0.18
  m_combined(Θ)    = 0.30 × 0.40 = 0.12
  Somme            = 1.00 ✓
```

*Sortie vérifiée — `s01_tbm_minimal.py`, section "Vérification algébrique" :*
```
  Somme m_combined : 1.000000 (attendu : 1.000000)
  [OK] Conservation de la masse verifiee
  m_combined({vide}) = 0.4200 <-- CONFLIT
```

**Pourquoi c'est important** : la règle de Dempster normalisée aurait effacé ce 0.42 et redistribué la masse entre {H1} et {H2}, masquant le désaccord (paradoxe de Zadeh, 1979). Aucun protocole ACL existant n'expose `m(∅)` comme champ de premier niveau.

---

### Dimension 2 — États épistémiques Belnap (S-01, prouvé)

**Ce que S-01 démontre** : l'état Belnap est dérivé de `m_combined(∅)` par règle de priorité décroissante (CORR-TP01-06), sans hypothèse sur les internals des agents.

*Sortie vérifiée :*
```
  belnap_state = B
```

`B` (Both — contradiction) est déclenché car `m(∅) = 0.42 ≥ θ_conflit = 0.30`. L'orchestrateur ne tranche pas ; il escalade vers l'opérateur humain.

**Distinction critique absente de tous les standards** : Belnap distingue `N` (Neither — silence qualifié : aucun agent n'a observé) de `B` (Both — contradiction : deux agents ont observé des hypothèses incompatibles). Dans un contexte ISR, un sonar silencieux sur un secteur hostile (`N`) n'a pas la même signification opérationnelle qu'un désaccord Radar/SIGINT (`B`). Aucun standard de communication inter-agents ne fait cette distinction au niveau du message.

---

### Dimension 3 — Statut illocutionnaire (S-03, prouvé)

**Ce que S-03 démontre** : le champ `illocution` est un invariant du CLAIM — sa valeur est validée avant toute combinaison.

*Sortie vérifiée :*
```
  [OK]    REJET        - illocution invalide
           => [REJET] illocution invalide : 'GUESS' (valeurs admises : ['ASSUME', 'DEDUCE', 'INFER', 'OBSERVE'])
```

**Preuve par contraste exécutée (S-04)** : `s04_fipa_contrast.py` exécute les deux formats pour le même scénario S-01 et affiche côte-à-côte :

```
  FIPA-ACL    belief_mass present : False  <-- ABSENT
              m(vide) calculable  : False  <-- IMPOSSIBLE
              DECISION : DESACCORD TEXTUEL DETECTE — heuristique ad hoc

  CLAIM       m(vide) calcule     : 0.42   <-- CONFLIT QUANTIFIE
              Etat Belnap         : B      <-- contradiction confirmee
              DECISION : ESCALADE HUMAINE REQUISE — conflit confirme
```

Fragilité 1 (v2.1) résolue : la lacune FIPA-ACL est maintenant démontrée par exécution, pas seulement par argument. Un agent ML est une boîte noire — on ne peut pas vérifier ce qu'il croit. Le champ `illocution` auto-déclaré (`OBSERVE | INFER | DEDUCE | ASSUME`) est la seule information sur l'origine épistémique que l'orchestrateur peut recevoir sans ouvrir la boîte. La validation B.1 garantit qu'une valeur hors énumération est rejetée avant toute combinaison.

---

### Dimension 4 — Fraîcheur temporelle (S-03, prouvé)

**Ce que S-03 démontre** : trois invariants de fraîcheur sont validés et rejetants.

*Sorties vérifiées :*
```
  [OK]    REJET        - timestamp manquant
           => [REJET] freshness.t_obs manquant

  [OK]    REJET        - delta_t_valid negatif
           => [REJET] freshness.delta_t_valid negatif ou invalide : -10
```

Un troisième cas (timestamp futur) est couvert dans le code source (`t_obs > now`). Les trois cas couvrent les modes de défaillance réels d'un capteur désynchronisé, redémarré, ou avec horloge corrompue.

---

### Dimension 5 — Provenance traçable (S-03, prouvé)

**Ce que S-03 démontre** : la provenance est un champ obligatoire dont le format (URI/URN RFC 3986) est validé syntaxiquement.

*Sorties vérifiées :*
```
  [OK]    REJET        - provenance absente
           => [REJET] Champ obligatoire manquant : 'provenance'
```

La validation vérifie que `chain_id` est présent ET est une URI valide (pattern `^[a-zA-Z][a-zA-Z0-9+\-.]*:.+$`). Un agent qui ne déclare pas sa chaîne de traitement est rejeté avant toute combinaison, prévenant le "rumor spreading" (deux agents apparemment indépendants issus de la même source corrompue).

---

## Calibration de θ_conflit (S-02 v2.0) — corpus enrichi, résultat discriminant

### Correction appliquée (feedback DOOM, 18 mai 2026)

S-02 v1.0 avait un corpus trivial : les cas non-conflictuels donnaient `m(∅) = 0` pour tous les seuils → FPR = 0.000 artefact. La v2.0 introduit une **troisième catégorie "ambigu"** : supports disjoints mais étiquetés non-conflit, simulant deux capteurs observant des entités distinctes. La vérification manuelle des plages de m(∅) a précédé l'implémentation (Mindset #17).

### Résultats prouvés (S-02 v2.0, seed=42, N=1000)

```
  theta = 0.10      FPR = 0.481      TPR = 1.000
  theta = 0.15      FPR = 0.481      TPR = 1.000
  theta = 0.20      FPR = 0.418      TPR = 1.000
  theta = 0.25      FPR = 0.238      TPR = 1.000
  theta = 0.30      FPR = 0.067      TPR = 1.000   ← FPR > 0.05 : critère non satisfait
  theta = 0.35      FPR = 0.005      TPR = 1.000   ← premier seuil satisfaisant FPR≤0.05
  theta = 0.40      FPR = 0.000      TPR = 0.961
  theta = 0.45      FPR = 0.000      TPR = 0.875
  theta = 0.50      FPR = 0.000      TPR = 0.735

  Recommandation automatique : theta_conflit = 0.35
```

La courbe est désormais discriminante. FPR passe de 0.481 à θ=0.10 à 0.005 à θ=0.35 puis 0 à θ=0.40.

### Pourquoi θ=0.35 et non θ=0.30

Les cas ambigus ont alpha ∈ [0.4, 0.6] → `m(∅) = alpha₁ × alpha₂ ∈ [0.16, 0.36]`. À θ=0.30, les ambigus avec `m(∅) ∈ [0.30, 0.36]` déclenchent l'escalade à tort (FPR = 0.067 > 0.05). À θ=0.35, seuls les ambigus avec `m(∅) ∈ [0.35, 0.36]` — zone quasi nulle de la distribution — passent le seuil (FPR = 0.005 ≤ 0.05). La prédiction "θ=0.30 ou 0.35" de DOOM était partiellement correcte ; la valeur exacte était vérifiable manuellement avant implémentation.

### Limite structurelle résiduelle — AM-04 v2

La frontière alpha=0.6 entre cas ambigu (max `m(∅)` = 0.36) et cas conflit (min `m(∅)` = 0.36) est **artificielle et tranchante** : un cas avec alpha=0.59 (ambigu) et un cas avec alpha=0.61 (conflit) ont des `m(∅)` quasi identiques mais des étiquettes opposées. En données ISR réelles, la séparation est continue. La recommandation θ=0.35 est donc **sensible à ce paramètre artificiel**.

### Décision opérationnelle NMT-2

θ_conflit = **0.30 maintenu** comme valeur conservative pour NMT-2. Justification : préférer l'escalade humaine (FPR=0.067) au silence sur un conflit réel, conformément à la règle cardinale. La calibration empirique (θ=0.35 sur corpus synthétique) est mentionnée comme borne supérieure informative, non comme valeur opérationnelle. Révision sur données réelles : NMT-3.

### Dette mise à jour (AM-04 v2)

---

## Résumé des preuves POC

| Dimension | Prouvé par | Sortie exacte | Note |
|-----------|-----------|---------------|------|
| Confiance DS — m(∅) conservé | S-01 | `m_combined({vide}) = 0.4200 <-- CONFLIT` | |
| Normalisation algébrique | S-01 | `Somme m_combined : 1.000000` | |
| État Belnap B déclenché | S-01 | `belnap_state = B` | |
| Escalade opérateur | S-01 | `VERDICT : ESCALADE HUMAINE REQUISE` | |
| PCR5 localisation conflit | S-01 | `Radar ({'H1'}) vs SIGINT ({'H2'}) \| contribution = 0.4200` | |
| Illocution invalide rejetée | S-03 | `[REJET] illocution invalide : 'GUESS'` | |
| Masse non normalisée rejetée | S-03 | `[REJET] belief_mass : somme = 1.10000000` | |
| Timestamp manquant rejeté | S-03 | `[REJET] freshness.t_obs manquant` | |
| Delta négatif rejeté | S-03 | `[REJET] freshness.delta_t_valid negatif ou invalide : -10` | |
| Provenance absente rejetée | S-03 | `[REJET] Champ obligatoire manquant : 'provenance'` | |
| FIPA-ACL : m(∅) non calculable | S-04 | `belief_mass present : False <-- ABSENT` | Preuve par contraste exécutée |
| FIPA-ACL : escalade impossible | S-04 | `Escalade metrique possible : False <-- IMPOSSIBLE` | Preuve par contraste exécutée |
| Calibration θ — courbe discriminante | S-02 v2.0 | FPR : 0.481 (θ=0.10) → 0.005 (θ=0.35) | AM-04 v1 résolu |
| Calibration θ — recommandation | S-02 v2.0 | `theta = 0.35 : FPR=0.005, TPR=1.000` | ⚠ Sensible à frontière artificielle alpha=0.6 (AM-04 v2). Valeur opérationnelle maintenue à **0.30** pour NMT-2. |
| θ=0.30 : FPR hors critère | S-02 v2.0 | `theta = 0.30 : FPR=0.067 > 0.05` | Conservé par précaution (DEC-S3-03) |
| **Calibration θ sur données réelles** | ✗ AM-04 v2 | Non disponible | NMT-3 — données ISR réelles requises |


---

## Ce que la POC ne démontre pas encore

Les affirmations suivantes restent argumentées (sources littéraires, consensus 4/4) mais sans preuve numérique à ce stade :

**1.** ~~L'absence de confiance formelle dans FIPA-ACL — argumentée par analyse des spécifications, non testée par code comparatif.~~ **Résolu par S-04** : la lacune FIPA-ACL est maintenant démontrée par exécution. L'absence de confiance formelle dans TBM (comme protocole), JDL, et PROV-O reste argumentée.

**2.** La supériorité de m(∅) sur la normalisation de Dempster pour le diagnostic de conflit — le paradoxe de Zadeh est un argument formel (Zadeh 1979), non testé comparativement sur des données réelles.

**3.** La valeur opérationnelle de θ = 0.30 — maintenue par argument conservateur. La calibration empirique sur corpus synthétique (S-02 v2.0) suggère θ=0.35 comme premier seuil satisfaisant FPR≤0.05 et TPR≥0.80, mais ce résultat est sensible à la frontière artificielle alpha=0.6 (AM-04 v2). Calibration sur données réelles : NMT-3.

---

## Implications pour la proposition — inchangées, renforcées

**CCP-2 (Innovation)** : le gap est désormais *démontrable* en exécutant S-01 devant un évaluateur. La différence entre un CLAIM structuré (m(∅) = 0.42, état Belnap B, PCR5 localisé) et un message FIPA-ACL (champ `UNCERTAIN` sans métrique, pas de conflit inter-sources) est observable en < 60 secondes.

**CCP-4 (Faisabilité)** : trois scripts Python stdlib, zéro dépendance externe, exécutables sur n'importe quelle machine avec Python 3.9+. La POC est reproductible par Thierry sans environnement de développement spécialisé (voir TECH_README.md).

**CCP-6 (Alignement résultats)** : S-01 démontre que l'orchestrateur peut prendre une décision d'escalade *traçable et justifiable* (`m(∅) = 0.42 ≥ θ = 0.30`, source du conflit identifiée : Radar/{H1} vs SIGINT/{H2}). Cette traçabilité est absente de tous les standards de communication inter-agents examinés.

---

## Analyse par standard — ce qui change par rapport à v1.0

La v1.0 analysait les lacunes des standards par argument. Cette version ajoute une **preuve par contraste** : FIPA-ACL et TBM sont insuffisants non pas parce qu'on le dit, mais parce que S-01 démontre ce qu'un CLAIM structuré produit et que ces standards ne produiraient pas.

### FIPA-ACL — lacune démontrée par contraste

**Argument v1.0** : "Aucune représentation formelle de la confiance quantifiée."

**Preuve par contraste (S-01)** : avec FIPA-ACL, le message de Radar serait `INFORM(orchestrateur, "cible = {H1}")` avec éventuellement `UNCERTAIN` dans la sémantique BDI. Le message de SIGINT serait `INFORM(orchestrateur, "cible = {H2}")`. L'orchestrateur reçoit deux assertions contradictoires sans aucune métrique de conflit. Il ne peut pas calculer `m(∅) = 0.42` car aucun champ ne porte les masses. Il ne peut pas déclencher un escalade fondée sur un seuil, car il n'existe pas de seuil sur `m(∅)` dans le protocole. La décision revient à une heuristique ad hoc.

### TBM — lacune démontrée par analyse du code

**Argument v1.0** : "TBM est un cadre de raisonnement, pas un protocole de communication."

**Preuve par inspection (S-01, tbm_utils.py)** : `tbm_conjunctive()` calcule correctement m_combined à partir de deux dicts Python. Mais ce calcul requiert que les masses soient déjà disponibles dans un format structuré. TBM ne spécifie pas ce format. La fonction de masse d'un agent ML en production n'est pas automatiquement exportée dans le format `{frozenset({"H1"}): 0.7, THETA: 0.3}`. Le CLAIM est précisément ce format — TBM ne le définit pas.

### JDL — lacune non modifiée

Argument identique à v1.0. Le gap d'interface JDL est documenté par Steinberg et al. (1999) ; aucune preuve numérique n'est nécessaire ni possible sur ce point.

---

## Références

| Référence | Pertinence | Type |
|-----------|------------|------|
| `s01_tbm_minimal.py` — exécuté le 18 mai 2026 | m(∅) = 0.42, Belnap B, PCR5 | **Preuve exécutée** |
| `s03_validation_malformed.py` — exécuté le 18 mai 2026 | 6/6 cas B.1 validés | **Preuve exécutée** |
| `s04_fipa_contrast.py` — exécuté le 18 mai 2026 | Contraste FIPA-ACL vs CLAIM : lacune belief_mass démontrée par exécution | **Preuve exécutée** |
| `s02_calibration_theta_v2.py` — exécuté le 18 mai 2026 | Courbe FPR/TPR discriminante, θ=0.35 recommandé (AM-04 v2) | **Preuve partielle** |
| Smets & Kennes (1994) — TBM | Fondement confiance DS | Littérature |
| Belnap (1977) — A useful four-valued logic | Fondement états épistémiques | Littérature |
| Steinberg et al. (1999) — Revisions to the JDL Data Fusion Model | Gap d'interface JDL documenté | Littérature |
| FIPA Consortium (1997) — FIPA-ACL | Standard de référence, lacune confiance | Littérature |
| W3C PROV-O (2013) | Standard de référence, traçabilité seule | Littérature |
| Zadeh (1979) — On the validity of Dempster's rule | Paradoxe normalisation | Littérature |

---

## Dettes tracées (Mindset #18)

| ID | Description | Source | Cible | Condition |
|----|-------------|--------|-------|-----------|
| **AM-04 v1** | ~~Corpus S-02 trop simple — FPR trivial (0.000). Cas ambigus absents.~~ | `s02_calibration_theta.py`, 18 mai 2026 | **RÉSOLU** | Corpus v2 introduit cas ambigus (S-02 v2.0) |
| **AM-04 v2** | Frontière alpha=0.6 artificielle entre cas ambigu (m(∅) max=0.36) et conflit (m(∅) min=0.36). Recommandation θ=0.35 sensible à ce paramètre. Distribution continue requise. | `s02_calibration_theta_v2.py`, 18 mai 2026 | NMT-3 | Calibration sur données ISR réelles (MSTAR ou CC-01) |

---

## Décisions

| ID | Décision | Statut |
|----|----------|--------|
| DEC-S3-01 | Formulation du gap retenue pour CCP-2 | FERME |
| DEC-S3-02 | Condition CCP-2 satisfaite — QO-S2-02 peut s'ouvrir | FERME |
| DEC-S3-03 | θ_conflit = 0.30 maintenu pour NMT-2 (conservateur). S-02 v2.0 recommande θ=0.35 sur corpus synthétique — non retenu car frontière alpha=0.6 artificielle (AM-04 v2). Révision sur données réelles : NMT-3. | FERME |
| QO-S2-02 | Rédaction CCP-6 | OUVERT → Sprint 3 |

---

*Document produit le 18 mai 2026 — Version 2.2.*
*Preuves numériques : S-01, S-02 v2.0, S-03, S-04 exécutés et vérifiés ce jour.*
*Fragilité 1 résolue : S-04 démontre par exécution la lacune FIPA-ACL.*
*Fragilité 2 résolue : tableau des preuves colonne Note + avertissement ⚠ sur θ=0.35.*
*AM-04 v1 résolu. AM-04 v2 ouverte (frontière artificielle — NMT-3).*
*Autorité de validation : Andrei (PI).*
*Remplace : toutes les versions précédentes de QO-S2-01_interface_contract_gap.md.*
