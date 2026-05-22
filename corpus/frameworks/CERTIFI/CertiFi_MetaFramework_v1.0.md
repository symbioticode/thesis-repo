# CertiFi — Meta-Framework de Certification Quantitative
## Vision v1.0 — Avril 2026

*Andrei + Claude (Sonnet 4.6)*
*Document de référence — tout autre document s'y réfère, aucun ne le remplace.*

---

## 0. Ce que ce document est

Ce document nomme. Il ne spécifie pas d'implémentation, ne détaille pas de protocole. Il établit les quatre entités, le pattern à quatre niveaux, la matrice, et la séquence de progression. Chaque autre document du corpus lui est subordonné.

---

## 1. Les quatre entités

```
CertiFi          Standard        Les règles du jeu. Évolue lentement, par consensus.
                                 Versionné (v1.0, v2.0). Un changement majeur invalide
                                 les comparaisons entre certifications de versions différentes.

QAAF Studio      Implémentation  La première application de CertiFi sur un domaine concret
                                 (paire PAXG/BTC, finance crypto quantitative).
                                 Évolue rapidement, par expérimentation. Itératif.

QAAF KB          Mémoire         S'accumule en permanence. Ne repart jamais à zéro.
                                 Survit aux implémentations. Doit être matérialisée comme
                                 un système interrogeable (RAG/embeddings), pas seulement
                                 des fichiers YAML.

CertiFi Commons  Communauté      Packages PyPI, publications, peer review, projets tiers.
                                 Ce qui transforme un protocole interne en standard défendu
                                 publiquement. FRAF est la première mission de cette entité.
```

**Règle de lecture :** CertiFi *spécifie* chaque cellule de la matrice. QAAF Studio l'*implémente*. QAAF KB la *capture*. CertiFi Commons la *publie*.

---

## 2. Le pattern QAF — quatre niveaux

Ce pattern est le cœur du meta-framework. Il s'applique à tout artefact de recherche quantitative — donnée, signal, métrique, modèle — dans n'importe quel domaine d'application.

```
Niveau 1 — PHYSIQUE       Les données sont-elles valides ?
           DQF             Propriétés observables, indépendantes de tout modèle.
                           Peut être axiomatique. Sol ferme sur lequel tout repose.
                           Statut : package autonome (mif-dqf), déjà conçu pour
                           4 marchés (actions, forex, crypto, commodités).
                           Dans QAAF Studio : optionnel (mode diagnostique) via import
                           conditionnel, jamais contraignant en phase de recherche.

Niveau 2 — ATOMIQUE       Cette mesure mesure-t-elle ce qu'elle prétend ?
           MIF             Une fonction, ses propriétés statistiques, son comportement
                           sous conditions adversariales (synthétiques + réelles).
                           Certifie les métriques une par une, indépendamment du signal.

Niveau 3 — CONTEXTUEL     Cet environnement est-il adapté à cette classe de méthodes ?
           PAF             Une paire, un régime, une classe de signaux.
                           "X ne sait pas qu'il teste" — la généricité comme garantie
                           d'objectivité.

Niveau 4 — INFÉRENTIEL    Que peut-on conclure au-delà de ce cas précis ?
           MÉTIS / FRAF    Généralisation, robustesse conditionnelle, transfert.
                           MÉTIS valide qu'une stratégie génère de la valeur OOS.
                           FRAF valide qu'une méthode résiste aux conditions adversariales
                           générales de la finance quantitative.
```

**Note sur le Niveau 4 :** MÉTIS et FRAF ne répondent pas à la même question.
MÉTIS dit : *ce signal, sur cette paire, dans ces conditions, est robuste OOS.*
FRAF dit : *cette méthode, en général, tient-elle face aux biais connus de la discipline ?*
Les deux sont inférentiels. Ils opèrent à des échelles différentes.

---

## 3. La matrice

La matrice croisant la chaîne verticale (Niveaux 1-4 + KB) avec les invariants transversaux est définie dans `certifi_matrix.svg`. Elle ne se redéfinit pas ici.

**Les cinq invariants transversaux** — présents à chaque niveau, appartenant à aucun :

| Invariant | Rôle | Implémentation dans QAAF Studio |
|---|---|---|
| Numéraire commun | Même langue à tous les niveaux | CNSR-USD (log-rendements, identité K&S) |
| Mémoire | Cohérence temporelle et logique | QAAF KB (YAML → RAG à terme) |
| Intégrité IS/OOS | L'OOS vu une seule fois | SplitManager (figé dès le premier test) |
| Benchmarks passifs | Référence absolue non trivialisable | B_5050, B_BTC (valeurs scellées KB) |
| Anti-cherry-picking | Protection contre le multiple testing | DSR + compteur N_trials (MÉTIS Q4) |

**Les trois plans de lecture de la matrice :**

```
M[couche, transversal, entité]

  couche       ∈ {DQF, MIF, PAF, MÉTIS, KB}
  transversal  ∈ {Numéraire, Mémoire, IS/OOS, Benchmarks, DSR}
  entité       ∈ {CertiFi (spec), QAAF Studio (code), QAAF KB (résultat)}
```

Chaque cellule est une affirmation vérifiable. La KB capture le plan `entité = Mémoire`.

---

## 4. Les deux applications

```
QAAF Studio                              FRAF
────────────────────────────────         ────────────────────────────────────────
Domaine : paire PAXG/BTC                 Domaine : finance quantitative mainstream
Mission : certifier H9+EMA60j           Mission : auditer les méthodes publiées
Niveau 1 : DQF (optionnel)              Niveau 1 : DQF adapté (données OHLCV génériques)
Niveau 2 : MIF                          Niveau 2 : MAF (Metric Audit Framework)
Niveau 3 : PAF                          Niveau 3 : FAF (Framework Adequacy Framework)
Niveau 4 : MÉTIS                        Niveau 4 : OVP (Out-of-Sample Validation Protocol)
Statut : en cours de construction       Statut : concept, en attente de QAAF Studio v1.0
```

FRAF attend QAAF Studio. Pas parce que l'un dépend de l'autre architecturalement, mais parce que les outils (PAF D1/D2/D3, tests adversariaux, protocole MÉTIS) doivent exister en code avant d'être appliqués à de nouvelles cibles. L'ordre est empirique, pas logique.

---

## 5. Le principe du "juste milieu"

Deux erreurs symétriques à éviter :

**Erreur gauche — abstraction prématurée.** Construire le framework générique avant d'avoir fini PAXG/BTC. Résultat : des référentiels universels sans cas de validation, des paramètres synthétiques non calibrés sur des données réelles, une théorie sans poids empirique.

**Erreur droite — sur-spécialisation.** Finir PAXG/BTC sans que les abstractions soient dans la structure du code. Résultat : QAAF Studio devient inextricable, FRAF nécessite une réécriture, `mif-dqf` sur PyPI est une extraction difficile plutôt qu'une publication naturelle.

**Le juste milieu :**
1. Finir ce qui est commencé (certification H9+EMA60j, MÉTIS Q1-Q4).
2. Construire avec les bonnes abstractions dès maintenant — Layer 1 déjà générique, PAF déjà aveugle au signal.
3. Garder les versions d'abstraction "au chaud" dans la KB (Couche B : patterns méthodologiques).
4. Ne publier sur PyPI qu'après avoir une implémentation testée et stable.

La règle pratique : si du code mentionne "PAXG" ou "BTC" dans sa logique principale (pas dans ses données de test), il n'est pas encore au bon niveau d'abstraction.

---

## 6. La QAAF KB — ce qu'elle doit devenir

La KB actuelle (fichiers YAML + Markdown) est un point de départ. Elle ne peut pas rester là.

**Ce qu'elle est maintenant :**
- Couche A : résultats d'hypothèses (YAML versionné) — existe
- Couche B : patterns méthodologiques (dans les .md) — existe, non interrogeable
- Couche C : lignée des certifications (quelle version a produit quoi) — absente

**Ce qu'elle doit devenir :**
Un système avec index, embeddings, chunks — type OpenClaw, Outline, ou RAG maison — capable de répondre à "a-t-on déjà testé ça ?" sans lecture humaine de tous les artefacts. La quantité documentaire va augmenter de façon continue. Sans ce système, la KB devient une archive morte.

La KB n'est pas un module de QAAF Studio. C'est une entité à part entière avec son propre cycle de vie. Elle survit aux versions du Studio.

---

## 7. La séquence de progression — Avril 2026

```
MAINTENANT                   Certifier H9+EMA60j
                             MÉTIS Q1 (walk-forward 5 fenêtres)
                             MÉTIS Q2 (permutation 10k, p-value vs B_5050)
                             MÉTIS Q3 (stabilité span EMA, grille IS)
                             MÉTIS Q4 (DSR, N_trials = 101)
                             → Verdict : CERTIFIÉ ou ARCHIVÉ

APRÈS CERTIFICATION          Vérifier la généricité de Layer 1
                             Tester PAF D1 sur une seconde paire (ETH/BTC)
                             sans modifier le code de Layer 1
                             → Si ça marche : le meta-framework est là structurellement
                             → Si ça ne marche pas : identifier exactement ce qui est
                               codé en dur pour PAXG/BTC

ENSUITE                      Préparer mif-dqf pour PyPI
                             (API publique stable, doc indépendante de PAXG/BTC,
                              données de test = SyntheticDataGeneratorMIF)
                             Première session FRAF pilote
                             (cible : Sharpe ×√252 naïf — Lo 2002 + correction HAC)

HORIZON                      QAAF KB comme système interrogeable (RAG)
                             CertiFi Commons : premier package + premier papier
                             FRAF : catalogue de cibles + premier audit complet publié
```

---

## 8. Ce que ce document ne fait pas

Il ne détaille pas les implémentations. Elles sont dans les artefacts #1-#6 (migration), `QAAF_Studio_3_0_Architecture.md`, et `QAAF_Studio_Vision_Complete.md`.

Il ne résout pas la question de la KB interrogeable. Il la nomme comme problème ouvert et prioritaire.

Il ne fixe pas de date. La progression est empirique : chaque étape attend que la précédente soit verte.

---

## Annexe — Noms définitifs

| Concept | Nom retenu | Variantes rejetées |
|---|---|---|
| Le meta-framework | CertiFi | QAF (trop générique), QAAF Framework (trop lié à l'implémentation) |
| Le pattern à 4 niveaux | Pattern QAF | QAF Ladder, certification chain |
| L'audit de la finance quant | FRAF | QAAF Audit, FinAudit |
| La première application | QAAF Studio | QAAF Lab, QAAF Research |
| La mémoire | QAAF KB | QAAF Archive, QAAF Memory |
| La communauté | CertiFi Commons | CertiFi Public, CertiFi Open |
| Niveau 1 | DQF — Physical | Layer 0, DataQuality |
| Niveau 2 | MIF — Atomic | Layer 2, MetricValidity |
| Niveau 3 | PAF — Contextual | Layer 2 (aussi), PairAdequacy |
| Niveau 4 | MÉTIS / FRAF — Inferential | Layer 3, OOS Validation |

---

*CertiFi Meta-Framework v1.0 — Avril 2026*
*Ce document remplace toute formulation antérieure du "meta-framework".*
*Prochaine révision : après certification H9+EMA60j et test de généricité Layer 1 sur ETH/BTC.*
