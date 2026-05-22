# MASTER_BRIEF — Thèse & PoC
## Contrat d'interface épistémique dans les systèmes cognitifs distribués
**Version** : 1.0 — 21 mai 2026
**Statut** : ACTIF — document de démarrage pour Jules (thèse) et Claude Code (PoC)
**Autorité** : Andrei (PI) — toute décision hors périmètre remonte à Andrei

---

## SECTION 0 — BOOTSTRAP OBLIGATOIRE

**Tout agent lisant ce document doit produire cette confirmation avant toute action :**

```
BRIEF CHARGÉ.
Agent         : [Jules | Claude Code]
Périmètre     : [THÈSE | POC]
Livrable J1   : [voir section correspondante]
Question avant démarrage : [OUI — laquelle | NON]
```

Si une ambiguïté bloque le démarrage, la poser ici. Ne pas commencer en supposant.

---

## SECTION 1 — CONTEXTE ET GENÈSE

### Ce qui s'est passé

Ce projet n'a pas commencé par une hypothèse. Il a commencé par des besoins concrets
de gestion de connaissance sur des projets techniques simultanés, sans savoir qu'une
architecture émergente allait se dessiner.

Sur 6+ mois, plusieurs frameworks ont été développés en parallèle, chacun répondant
à une contrainte réelle :

- Des sessions de travail humain/IA qui perdent leur contexte entre les sessions
- Des projets multiples qui ne se parlent pas
- Des données financières qui doivent être certifiées avant d'être utilisées
- Un protocole d'échange entre agents ISR hétérogènes en temps réel

Sans coordination préalable, ces travaux ont convergé vers les mêmes invariants
structurels. Cette convergence n'était pas planifiée. Elle a été observée après coup.

### Ce que cette convergence signifie

Des systèmes développés indépendamment, dans des domaines contraignants distincts,
ont abouti aux mêmes trois invariants :

1. **Séparation émetteur/interpréteur** — un nœud ne lit jamais son propre état
2. **Cycle de vie épistémique explicite** — toute unité de connaissance a un statut
3. **Escalade humaine sur conflit non résolu** — la machine n'arbitre jamais seule

Une validation externe (deep search dans 3 domaines sans accès au corpus — industrie
pharmaceutique FDA, standards militaires NATO STANAG 4559, bioinformatique NIH)
a retrouvé les mêmes 5 champs structurels que ceux produits indépendamment.

Ce résultat réfute l'hypothèse que la convergence serait un artefact cognitif.
C'est une contrainte réelle, observable dans des domaines qui n'ont aucun contact
entre eux.

### Les six frameworks du corpus

| Framework | Domaine | Statut | Rôle dans la thèse |
|---|---|---|---|
| PCCD | Théorie universelle connaissance distribuée | PENDING | Hypothèse centrale |
| RKA | Navigation et réutilisation de connaissance | CERTIFIED | Implémentation persistante |
| ANAMNÈSE | Continuité cognitive inter-sessions humain/IA | PENDING | Protocole de continuité |
| HALO | Instance terrain sur projet MIF-DAL | Opérationnel | Validation empirique |
| SYNAPSE | Architecture exocortex 4 couches | PENDING | Proposition architecturale |
| CLAIM | Protocole échange épistémique ISR temps-réel | Spec validée | Instanciation temps-réel |

### Les trois systèmes périphériques analysés

| Système | Ce qu'il résout | Ce qu'il laisse ouvert |
|---|---|---|
| LLM Wiki (Karpathy) | Maintenance corpus par LLM discipliné | Pas de mémoire inter-sessions, pas de statuts épistémiques |
| GraphRAG (Microsoft Research) | Réponses globales par communautés de graphe | Pas de Couche 2 (mémoire IA), drift sémantique non détectable |
| Graphify | Extraction de graphe depuis documents | Arêtes inférées dérivent avec le modèle, pas de provenance |

**Le gap commun à ces trois systèmes** : aucun ne spécifie le contrat d'interface
entre la connaissance persistante et l'agent qui agit dessus en temps réel.
C'est ce gap que ce travail adresse.

---

## SECTION 2 — LA THÈSE

### Énoncé

> Les systèmes cognitifs distribués — qu'ils soient humain/IA ou agent/agent —
> convergent vers une architecture à trois invariants : séparation émetteur/interpréteur,
> cycle de vie épistémique explicite, et escalade humaine sur conflit non résolu.
> Cette convergence est observable indépendamment du domaine et du substrat.
> Le contrat d'interface épistémique est le chaînon manquant entre les systèmes
> de gestion de connaissance persistante et les systèmes de fusion multi-agents
> temps-réel.

### Structure en 5 chapitres

**Chapitre 0 — Genèse** (2-3 pages)
Raconter honnêtement : pas d'hypothèse de départ, des besoins concrets, une
architecture émergente. Nommer la méthode : *recherche par contrainte*, pas par design.
Montrer la trajectoire chronologique des frameworks.

**Chapitre 1 — Le problème** (5-7 pages)
Trois systèmes existants (LLM Wiki, GraphRAG, Graphify) et le modèle JDL comme
cartographie du gap. Montrer que chaque système résout une partie et laisse le même
vide : l'interface entre connaissance persistante et agent temps-réel.

**Chapitre 2 — Convergence observée** (8-10 pages)
Les six frameworks. Pour chacun : domaine, contrainte génératrice, invariant émergent.
Tableau de convergence. Réfutation du biais de substrat par validation externe.
C'est le cœur empirique de la thèse.

**Chapitre 3 — Formalisation** (10-12 pages)
L'invariant de séparation épistémique comme principe unificateur. PCCD comme
spécification abstraite. CLAIM comme instanciation temps-réel. Les ponts non résolus
(couche de traduction RKA→CLAIM, pont C1↔C2 SYNAPSE) nommés honnêtement.

**Chapitre 4 — Implémentation de référence** (8-10 pages)
HALO/MIF-DAL comme terrain. Ce qui a marché, ce qui n'a pas marché, ce que ça valide.
Les métriques : tests passing, coverage, invariants vérifiés.

**Chapitre 5 — PoC** (5-7 pages)
Description du PoC, scénarios de démonstration, limites déclarées.

### Ton — important

La thèse est écrite à la première personne du pluriel de recherche.
Elle ne prétend pas avoir tout résolu. Elle documente ce qui a été observé,
ce qui a convergé, et ce qui reste ouvert. Les gaps sont nommés explicitement —
c'est une force épistémique, pas une faiblesse.

Pas de jargon inutile. Un lecteur en sciences cognitives sans background ISR
doit comprendre les chapitres 0, 1, et 2.

---

## SECTION 3 — LE POC

### Ce que le PoC doit démontrer

Deux scénarios, pas plus.

**Scénario A — Démonstration du problème**
Trois agents synthétiques émettent des assertions sur la même hypothèse avec des
masses de croyance contradictoires. Sans le protocole CLAIM, l'orchestrateur ne
peut pas détecter le conflit — il combine aveuglément et produit une décision
fausse avec haute confiance apparente. Montrer ce résultat.

**Scénario B — Démonstration de la solution**
Les mêmes trois agents, avec le protocole CLAIM. L'orchestrateur applique TBM
non normalisé, `m(∅)` dépasse `θ_conflit`, la décision automatique est suspendue,
le conflit est localisé (PCR5), l'opérateur humain est notifié avec le diagnostic.
Montrer ce résultat.

### Ce que le PoC n'est pas

- Pas un système de production
- Pas une implémentation complète de CLAIM v1.1
- Pas une interface utilisateur

### Stack technique

Python 3.11+. Pas de dépendances lourdes. Tout doit tourner avec `pip install`
en moins de 2 minutes sur n'importe quelle machine.

```
poc/
├── README.md                 ← instructions de lancement en 3 commandes
├── requirements.txt          ← scipy, numpy, pyyaml uniquement
├── claim/
│   ├── __init__.py
│   ├── structures.py         ← dataclasses CLAIM + EPISTEMIC_STATE
│   ├── validator.py          ← cascade validation B.1 (3 niveaux)
│   ├── combinator.py         ← TBM non normalisé + PCR5 minimal
│   └── orchestrator.py       ← logique escalade θ_conflit + Belnap
├── scenarios/
│   ├── scenario_a_sans_claim.py
│   └── scenario_b_avec_claim.py
└── tests/
    ├── test_validator.py
    ├── test_combinator.py
    └── test_orchestrator.py
```

### Sorties attendues du PoC

Scénario A produit :
```
[SANS CLAIM] Décision : H2 (confiance : 0.87)
[SANS CLAIM] Conflit m(∅) : 0.0  ← non détecté, normalisé à zéro
[SANS CLAIM] Résultat : DÉCISION AUTOMATIQUE ÉMISE — conflit invisible
```

Scénario B produit :
```
[AVEC CLAIM] m(∅) combiné : 0.41  ← > θ_conflit (0.30)
[AVEC CLAIM] Belnap : B (Both — contradiction diagnostique)
[AVEC CLAIM] Conflit localisé : Agent_1 vs Agent_3 sur H2
[AVEC CLAIM] Décision automatique : SUSPENDUE
[AVEC CLAIM] Escalade C-07 : OUI
```

---

## SECTION 4 — RÉPARTITION DES TÂCHES

### Jules — Thèse (J1 à J3)

**J1 — Chapitres 0 et 1**
- Lire SECTION 1 de ce brief + les fichiers corpus/ listés ci-dessous
- Produire ch0_genese.md et ch1_probleme.md
- Commit sur branche `thesis/ch0-ch1`
- Confirmation de fin de J1 : fichiers présents + nombre de mots dans AGENT_HANDOFF.md

**J2 — Chapitres 2 et 3**
- Lire les résultats de J1 + continuer depuis le corpus
- Produire ch2_convergence.md et ch3_formalisation.md
- Commit sur branche `thesis/ch2-ch3`

**J3 — Chapitres 4 et 5 + assemblage**
- Produire ch4_implementation.md et ch5_poc.md (description du PoC depuis les résultats Claude Code)
- Assembler thesis/README.md avec table des matières et résumé
- Commit sur branche `thesis/final`

**Fichiers corpus à lire pour Jules :**
```
corpus/frameworks/PCCD_Doc1_Hypothesis_v0_3.md
corpus/frameworks/PCCD_Doc2_Synthese_Contributions.md
corpus/frameworks/RKA_Formalisation_v4.md
corpus/frameworks/ANAMNESE_v0_3.md
corpus/frameworks/SYNAPSE_Architecture_Proposition_v0_1.md
corpus/frameworks/CLAIM_specification.md
corpus/frameworks/CLAIM_completude_v0_3_consolidee.md
corpus/frameworks/RESUME_APERCU.md
corpus/frameworks/CO-1_description_RD.md
corpus/frameworks/CCP-1_merite_scientifique.md
corpus/frameworks/CCP-2_innovation.md
corpus/frameworks/CO-2_harmonisation_defi.md
```

**Ce que Jules ne fait pas :**
- Ne pas toucher poc/
- Ne pas modifier MASTER_BRIEF.md
- Ne pas prendre de décision sur la structure de la thèse sans poser la question dans AGENT_HANDOFF.md

---

### Claude Code — PoC (J1 à J5)

**J1 — Structures et validator**
- Lire SECTION 3 de ce brief
- Implémenter `claim/structures.py` et `claim/validator.py`
- Tests unitaires correspondants — 100% coverage sur ces deux fichiers
- Commit sur branche `poc/j1-structures`
- Confirmation : SESSION_REPORT dans AGENT_HANDOFF.md

**J2 — Combinator (TBM)**
- Implémenter `claim/combinator.py` — règle conjonctive non normalisée de Smets
- `m(∅)` conservé comme output explicite — jamais normalisé à zéro
- PCR5 minimal : identifier les agents en conflit, pas la redistribution complète
- Tests : vérifier que `m_combined(∅)` > 0 quand deux agents se contredisent
- Commit sur branche `poc/j2-combinator`

**J3 — Orchestrator + Belnap**
- Implémenter `claim/orchestrator.py`
- Dériver `belnap_state` depuis `m_combined(∅)` et la distribution sur Θ
- Logique d'escalade : si `m(∅) ≥ θ_conflit` → suspendre décision + logger
- Commit sur branche `poc/j3-orchestrator`

**J4 — Scénarios A et B**
- Implémenter `scenarios/scenario_a_sans_claim.py`
  - Combination naïve normalisée (règle de Dempster standard)
  - Montrer que `m(∅)` disparaît et que la confiance apparente est haute
- Implémenter `scenarios/scenario_b_avec_claim.py`
  - Pipeline complet : validation → combinaison TBM → Belnap → escalade
  - Sorties conformes au format SECTION 3 de ce brief
- Commit sur branche `poc/j4-scenarios`

**J5 — Intégration et documentation**
- `poc/README.md` — 3 commandes pour lancer, 2 paragraphes d'explication
- `requirements.txt` — scipy, numpy, pyyaml uniquement
- Merge de toutes les branches poc/ vers `poc/main`
- SESSION_REPORT final dans AGENT_HANDOFF.md

**Ce que Claude Code ne fait pas :**
- Ne pas toucher thesis/
- Ne pas implémenter CLAIM v1.1 complète — PoC minimal uniquement
- Ne pas ajouter de dépendances sans poser la question dans AGENT_HANDOFF.md
- Ne pas committer si pytest échoue

---

## SECTION 5 — FICHIER DE COORDINATION

Les deux agents écrivent dans `AGENT_HANDOFF.md` à la fin de chaque journée.
Format imposé :

```yaml
# AGENT_HANDOFF.md
date: YYYY-MM-DD
agent: [Jules | Claude Code]
jour: J[N]
livrables_produits:
  - [fichier : mots/lignes]
questions_ouvertes:
  - [question → destinataire : Andrei | autre agent]
prochaine_action: [une phrase]
bloquants: [OUI — lequel | NON]
```

Andrei lit AGENT_HANDOFF.md chaque matin et répond aux questions avant le démarrage
de la journée. Pas de décision sans cette lecture.

---

## SECTION 6 — INVARIANTS NON NÉGOCIABLES

Ces règles s'appliquent aux deux agents, sans exception.

**I-01** — GitHub est la seule source de vérité. Aucun livrable n'existe tant qu'il
n'est pas commité.

**I-02** — Pas de contenu généré sans corpus source. Toute affirmation dans la thèse
doit être traçable à un fichier du corpus. Pas de raisonnement inventé.

**I-03** — Les gaps sont nommés explicitement. Ne pas prétendre résoudre ce qui
n'est pas résolu.

**I-04** — Les deux branches (thesis/ et poc/) ne se fusionnent pas avant J5.
Andrei fait le merge final.

**I-05** — Un seul AGENT_HANDOFF.md. Les deux agents écrivent dedans, avec leur
nom explicite. Pas deux fichiers séparés.

**I-06** — La thèse décrit le PoC tel qu'il a été construit, pas tel qu'il aurait
dû être construit. Jules écrit ch5 après avoir lu le SESSION_REPORT final de
Claude Code, pas avant.

---

## SECTION 7 — RÉFÉRENCES CLÉS

### Références internes (corpus — fichiers à mettre dans corpus/frameworks/)

Les fichiers PCCD, RKA, ANAMNÈSE, SYNAPSE, HALO (anamnese_state.yaml, protocols.yaml,
profil_stable.yaml), CLAIM_specification.md, CLAIM_completude_v0_3_consolidee.md,
CO-1, CO-2, CCP-1, CCP-2, RESUME_APERCU.md.

### Références externes (BibTeX à créer dans corpus/references/refs.bib)

```
Smets & Kennes (1994)       — Transferable Belief Model
Dezert & Smarandanche       — PCR5/PCR6
Belnap (1977)               — Four-valued logic
AGM (1985)                  — Belief revision postulates
Austin (1962)               — Speech Act Theory
Searle (1969)               — Speech Acts
Denœux (2008)               — Cautious conjunctive rule
Sarker et al. (2021)        — Neuro-Symbolic AI: The 3rd Wave
Steinberg et al. (1999)     — Revisions to the JDL Data Fusion Model
W3C PROV-O (2013)           — Provenance ontology
FDA 21 CFR Part 11          — GxP Audit Trail (convergence externe §7)
STANAG 4559 Ed.3            — NATO ISR Library Interface (convergence externe §7)
PMC7372873 (NIH 2020)       — Genomic audit blockchain (convergence externe §7)
Trope & Liberman (2003)     — CLT (Construal Level Theory)
Manhaeve et al. (2018)      — DeepProbLog
Zadeh (1979)                — Paradoxe (motivation centrale CLAIM)
```

---

## SECTION 8 — CRITÈRES DE SUCCÈS

### Thèse (J3)

- [ ] 5 chapitres présents et non vides
- [ ] Chaque affirmation traçable à un fichier corpus
- [ ] Les gaps nommés explicitement dans ch3 et conclusion
- [ ] Lisible par un non-spécialiste ISR (chapitres 0, 1, 2)
- [ ] Pas de jargon non défini

### PoC (J5)

- [ ] `pytest tests/` — 0 failing
- [ ] Scénario A produit la sortie attendue (SECTION 3)
- [ ] Scénario B produit la sortie attendue (SECTION 3)
- [ ] `pip install -r requirements.txt && python scenarios/scenario_b_avec_claim.py`
      fonctionne sur une machine propre
- [ ] README.md lisible en moins de 3 minutes

### Intégration finale (J5 soir)

- [ ] ch5 de Jules référence les résultats réels du PoC
- [ ] AGENT_HANDOFF.md indique 0 bloquants
- [ ] Andrei a validé le merge vers main

---

*MASTER_BRIEF v1.0 — 21 mai 2026*
*Autorité : Andrei (PI)*
*Ne pas modifier sans validation Andrei*
*Prochaine révision : après confirmation de bootstrap des deux agents*
