# Dette de décision — Branche BR-2026-CLAIM_completude
**Date** : 21 mai 2026
**Statut** : EN ATTENTE — aucune intégration avant compilation finale toutes branches
**Source** : CLAIM_completude_v0_3_consolidee.md (ANAMNESE, consolidation v0.1+v0.2+REV12B)
**Branches restantes** : 3 autres branches isolées à réviser avant décision
**Session de décision** : après compilation tableau toutes branches

---

## Contexte de la branche

La branche BR-2026-CLAIM_completude est issue d'une instance AMANMESE travaillant
en isolation sur la question : *"Quelles lacunes de la spec CLAIM v1.1 méritent
d'être comblées avant soumission IDEeS ?"*

Elle a produit 8 composants d'amélioration, révisés par une instance adverse (REV12B),
soumis à un deep search externe, et consolidés dans CLAIM_completude_v0_3_consolidee.md.

**Ce document ne tranche rien.** Il pose chaque composant comme une décision en attente,
avec les informations nécessaires pour trancher une fois que toutes les branches auront
été révisées.

---

## Tableau de dette de décision — vue consolidée

| § | Composant | Pertinence NMT 2 | Pertinence NMT 3 | Solidité formelle | Risque intégration | Verdict corpus | Valeur proposition | Statut décision |
|---|---|---|---|---|---|---|---|---|
| §1 | Cycle de vie 7 statuts | **HAUTE** | HAUTE | BONNE | FAIBLE | Convergence partielle · SUPERSEDED/VOID inédits | **ÉLEVÉE** | EN ATTENTE |
| §2 | Cascade validation 3 niveaux | **HAUTE** | HAUTE | EXCELLENTE | NUL | Convergence forte principe · formalisation originale | **ÉLEVÉE** | EN ATTENTE |
| §3a | Freshness OBSERVE (`freshness_decay_rate` optionnel) | MOYENNE | — | BONNE | FAIBLE | Convergence partielle | MOYENNE | EN ATTENTE |
| §3b | Freshness INFER/DEDUCE (dépendances + prémisses) | FAIBLE | HAUTE | PARTIELLE | MOYEN | Convergence partielle | MOYENNE | EN ATTENTE |
| §3c | Freshness ASSUME (`assume_max_validity_s`) | MOYENNE | — | BONNE | NUL | Contribution originale (garde-fou) | MOYENNE | EN ATTENTE |
| §4 | Détection stale storm (3 paramètres + fermeture AM-03) | MOYENNE | **HAUTE** | BONNE | FAIBLE | Convergence forte problème | **ÉLEVÉE** | EN ATTENTE |
| §5 | Graphe dépendances inter-CLAIMs (index léger) | FAIBLE | **HAUTE** | BONNE | MOYEN | Convergence forte structure | MOYENNE | EN ATTENTE |
| §6 | Protocole nouvel agent (UNREGISTERED→REGISTERED→QUARANTINED) | FAIBLE | **HAUTE** | BONNE | FAIBLE | Convergence partielle · solution TBM inédite | **ÉLEVÉE** | EN ATTENTE |
| §7 | Log certifiable (8 champs + `trust_discount_applied`) | **HAUTE** | — | EXCELLENTE | NUL | **Convergence forte · 3 domaines indépendants** | **ÉLEVÉE** | EN ATTENTE |
| §8a | `HYPOTHESIS_OUT_OF_FRAME` (6e cas B.1) | **HAUTE** | — | BONNE | NUL | Absence convergence = contribution prospective | MOYENNE | EN ATTENTE |
| §8b | Gouvernance Θ versionnée + rétrocompatibilité | FAIBLE | HAUTE | BONNE | MOYEN | Absence convergence = contribution prospective | MOYENNE | EN ATTENTE |

---

## Fiches de décision individuelles

Chaque fiche pose la question, les options, et les éléments pour trancher.
**Aucune option n'est recommandée ici** — c'est le rôle de la session de décision finale.

---

### D-01 — §1 Cycle de vie 7 statuts

**Question** : Intégrer les 7 statuts épistémiques (RECEIVED/VALID/ACTIVE/EXPIRED/
SUPERSEDED/REJECTED/VOID) dans la Partie B de la spec ?

**Ce que ça clarifie** : la sémantique de l'expiration silencieuse et la règle formelle
de remplacement sur double-émission du même agent — deux angles morts réels dans la
spec v1.1.

**Options** :
- A : Intégrer en Partie B §B.3 (GitHub annex, pas dans le portail IDEeS)
- B : Intégrer uniquement SUPERSEDED et VOID (les deux statuts originaux), les autres
  étant implicites dans la spec actuelle
- C : Reporter post-J19 — les angles morts existent mais ne bloquent pas NMT 2

**Éléments pour trancher** :
- SUPERSEDED et VOID sont absents de tous les corpus consultés (A2A, Agent Contracts,
  STANAG 4559, Dublin Core) — valeur de contribution documentable
- Le texte complet est déjà rédigé dans CLAIM_completude_v0_3_consolidee.md §1 —
  coût d'intégration = zéro rédaction, seulement un commit GitHub
- Impact portail IDEeS : NUL (Partie B = GitHub annex uniquement)

**Dépendances** : §2 (la cascade de validation définit les transitions RECEIVED→VALID)

---

### D-02 — §2 Cascade de validation à 3 niveaux

**Question** : Restructurer B.1 pour ordonner explicitement les 5 vérifications en
cascade numérotée O(1)/O(log n)/O(k), avec paramètre timeout et comportement charge
dégradée ?

**Ce que ça clarifie** : l'ordre d'évaluation est actuellement implicite — deux
implémentations conformes à la spec v1.1 peuvent valider les champs dans des ordres
différents, produisant des logs non comparables.

**Options** :
- A : Intégrer en B.1 comme sous-section "Ordre d'évaluation" (modification de la spec
  soumise au portail IDEeS — Partie A ou Partie B selon le point d'insertion)
- B : Intégrer uniquement dans le GitHub annex (Partie B) comme note d'implémentation
  recommandée, sans modifier B.1 du portail
- C : Reporter post-J19

**Éléments pour trancher** :
- Si B.1 est dans la Partie B (GitHub annex) : option A ne touche pas le portail
- Si B.1 est dans la Partie A (formulaire portail) : option A est une modification
  du formulaire — vérifier la limite de caractères avant décision
- Valeur CCP-4 (SWaP) : la complexité annotée O(1)/O(log n)/O(k) est un argument
  direct de faisabilité embarquée — pertinent pour l'évaluateur MDN
- `validation_level1_timeout_ms` (défaut 50 ms) répond au manquement M5 REV12B
  (comportement charge dégradée) — questions ouvertes QO-BR-02 non encore fermées

**Dépendances** : §1 (les niveaux de cascade définissent les transitions de statuts)

---

### D-03 — §3a Freshness OBSERVE (`freshness_decay_rate` optionnel)

**Question** : Ajouter un champ optionnel `freshness_decay_rate` (λ) dans les CLAIMs
de type OBSERVE, permettant une décroissance exponentielle α(Δt) = e^{-λΔt} ?

**Ce que ça apporte** : permet aux agents radar/SIGINT/EO-IR de déclarer leur propre
taux d'obsolescence physique — plus précis que le `Δt_valid` binaire actuel.

**Options** :
- A : Intégrer en §A.3 comme champ optionnel (backward-compatible, pas de rupture)
- B : Reporter NMT 3 — le champ binaire `Δt_valid` est suffisant pour NMT 2

**Éléments pour trancher** :
- Champ optionnel = risque d'intégration nul (l'orchestrateur ignore si absent)
- Valeur opérationnelle : pertinente pour les capteurs à haute dynamique (radar)
  mais la calibration de λ est un travail de domaine non trivial
- Impact portail IDEeS : modification de la structure du CLAIM — vérifier si §A.3
  est dans la Partie A (portail) ou Partie B (annex)

**Dépendances** : §5 (la décroissance INFER dépend du graphe de dépendances)

---

### D-04 — §3b Freshness INFER/DEDUCE (dépendances + prémisses)

**Question** : Définir des règles de décroissance conditionnelle pour les CLAIMs INFER
(validité liée aux sources déclarées) et DEDUCE (validité liée aux prémisses logiques) ?

**Ce que ça apporte** : corrige les expirations prématurées de CLAIMs dont les prémisses
logiques sont encore valides.

**Options** :
- A : Reporter NMT 3 — requiert §5 (graphe de dépendances) comme prérequis
- B : Définir le mécanisme conceptuellement en Partie B, implémentation NMT 3

**Éléments pour trancher** :
- Dépendance forte sur §5 (graphe) — §5 lui-même est NMT 3
- Valeur formelle réelle mais coût d'implémentation élevé
- Recommandation naturelle : archiver dans research/post_submission_ideas.md

**Dépendances** : §5 (prérequis non négociable)

---

### D-05 — §3c Freshness ASSUME (`assume_max_validity_s`)

**Question** : Ajouter un paramètre `assume_max_validity_s` dans la configuration de
l'orchestrateur pour plafonner `Δt_valid` des CLAIMs ASSUME indépendamment de ce que
l'agent déclare ?

**Ce que ça apporte** : garde-fou de sécurité opérationnelle — un agent mal calibré ne
peut pas maintenir un CLAIM ASSUME actif indéfiniment. Répond au manquement M3 REV12B
(gravité Moyenne).

**Options** :
- A : Intégrer comme paramètre de configuration orchestrateur (pas dans le CLAIM,
  impact portail nul)
- B : Reporter NMT 3 — le risque est réel mais non bloquant pour NMT 2

**Éléments pour trancher** :
- Ce paramètre vit dans la configuration de l'orchestrateur, pas dans la spec CLAIM —
  impact portail IDEeS : NUL
- La cause `ASSUME_CAPPED` dans le log certifiable est la seule trace visible
  (champ `transition_cause` déjà prévu)
- Valeur sécurité : réelle pour les systèmes certifiables DO-178C

**Dépendances** : §7 (le log doit inclure la cause ASSUME_CAPPED)

---

### D-06 — §4 Détection stale storm (3 paramètres + fermeture AM-03)

**Question** : Définir les trois paramètres de détection du stale storm
(`stale_window_duration`, `stale_threshold_ratio`, `stale_escalation_policy`) et
reclassifier AM-03 de NMT 4-5 à NMT 3 ?

**Ce que ça apporte** : fermeture formelle d'un failure mode connu — AM-03 passe de
"futur lointain" à "défini, implémentation NMT 3".

**Options** :
- A : Intégrer en Partie B §B.4 (GitHub annex) avec note de fermeture AM-03
- B : Reporter post-J19 — AM-03 NMT 4-5 est une position défendable

**Éléments pour trancher** :
- Les trois paramètres vivent dans la configuration de l'orchestrateur — impact portail NUL
- La fermeture d'AM-03 est un signal positif pour un évaluateur MDN qui remarquerait
  l'angle mort : "vous avez identifié ce failure mode mais pas de plan ?"
- Contre-exemple Loopy BP (layer_3_counter_examples.md §4) valide positivement le
  choix d'orchestrateur centralisé — argument CCP-4 utilisable

**Dépendances** : §6 (AGENT_QUARANTINE est l'une des options de `stale_escalation_policy`)

---

### D-07 — §5 Graphe de dépendances inter-CLAIMs (index léger)

**Question** : Définir un index léger `chain_id → [chain_ids dépendants]` maintenu
par l'orchestrateur pour la propagation d'expiration entre CLAIMs corrélés ?

**Ce que ça apporte** : évite le scan O(n²) à chaque expiration. Rend la propagation
d'expiration INFER→source correcte sans coût prohibitif.

**Options** :
- A : Définir conceptuellement en Partie B §B.5 comme prérequis NMT 3, implémentation
  post-J19
- B : Reporter entièrement post-J19 avec archivage dans research/

**Éléments pour trancher** :
- Prérequis de §3b (freshness INFER) — si §3b est reporté, §5 peut l'être aussi
- Convergence forte (réseaux bayésiens, Belief Propagation Pearl) — argument CCP-1
  si mentionné comme future direction
- Risque d'intégration MOYEN si intégré maintenant (dépendances croisées à spécifier)

**Dépendances** : §3b (freshness INFER)

---

### D-08 — §6 Protocole nouvel agent (UNREGISTERED→REGISTERED→QUARANTINED)

**Question** : Définir un cycle de vie agent à trois états avec `newcomer_trust_weight`
(discount multiplicatif sur belief_mass) et `trust_discount_applied` dans le log ?

**Ce que ça apporte** : résout la tension stateless/confiance progressive. Un agent
inconnu peut émettre un premier CLAIM sans enregistrement préalable (stateless préservé)
mais avec contribution pondérée jusqu'à validation structurelle.

**Options** :
- A : Intégrer en Partie B §B.5 (GitHub annex)
- B : Reporter NMT 3 — la tension existe mais les évaluateurs NMT 2 n'en ont pas
  conscience

**Éléments pour trancher** :
- Le mécanisme est solide et sa formulation v0.3 résout le manquement M2 REV12B
  (auditabilité DO-178C via `trust_discount_applied`)
- Il introduit une notion de "réputation d'agent" qui était absente — à présenter
  avec soin pour ne pas laisser penser que le CLAIM est modifié (il ne l'est pas)
- Convergence partielle (FIPA, TrustTrack) — la solution TBM avec discount progressif
  est inédite dans la littérature consultée

**Question ouverte QO-BR-03** : sortie de quarantaine sous reconnexion massive —
non encore résolue, à traiter avant intégration.

**Dépendances** : §7 (champ `trust_discount_applied` dans le log), §4 (AGENT_QUARANTINE)

---

### D-09 — §7 Log certifiable (8 champs + `trust_discount_applied`)

**Question** : Documenter les 8 champs obligatoires du log certifiable comme contrat
d'interface que TP-02 devra respecter, avec note de convergence externe ?

**Ce que ça apporte** : ferme le gap de TP-02 (livrable non encore spécifié dans la
spec v1.1). La convergence externe sur 3 domaines distincts est l'argument le plus
solide de toute la branche.

**Options** :
- A : Ajouter une note de convergence dans LOG_certifiable.md (déjà commité en v1.1)
  — 3 lignes, impact minimal
- B : Créer un document séparé LOG_certifiable_convergence.md dans research/
- C : Reporter — LOG_certifiable.md v1.1 est suffisant pour la soumission

**Éléments pour trancher** :
- LOG_certifiable.md v1.1 existe déjà avec 11 champs — la convergence externe
  *valide* ce qui existe, elle ne l'étend pas (sauf `trust_discount_applied`)
- Le champ `trust_discount_applied` est une extension qui dépend de D-08 (§6)
- La note de convergence (option A) est la modification la moins risquée possible
  et la plus défendable face à un évaluateur MDN ou à un auditeur REV

**Dépendances** : §6 pour `trust_discount_applied` uniquement

---

### D-10 — §8a `HYPOTHESIS_OUT_OF_FRAME` (6e cas B.1)

**Question** : Ajouter un 6e cas de malformation dans B.1 pour les CLAIMs dont
l'hypothèse est absente de la version courante de Θ ?

**Ce que ça apporte** : ferme un comportement undefined dans la spec v1.1 — que fait
l'orchestrateur si un agent émet un CLAIM sur une hypothèse hors-Θ ?

**Options** :
- A : Ajouter en B.1 (si B.1 est dans la Partie B/GitHub annex = impact portail nul)
- B : Documenter comme note comportementale dans Partie B §B.6 sans modifier B.1
- C : Reporter — le cas est improbable en NMT 2 avec Θ statique

**Éléments pour trancher** :
- En NMT 2 avec Θ statique et |Θ| ≤ 20 hypothèses prédéfinies, le risque de CLAIM
  hors-Θ est faible mais non nul (agent mal configuré)
- Le comportement est simple à définir (REJECTED + notification C-07) et cohérent
  avec le reste de B.1
- Impact portail : dépend de l'emplacement exact de B.1 dans la spec

**Dépendances** : §8b (gouvernance Θ versionnée — prérequis pour que la règle ait
un sens complet, mais D-10 est valide même sans §8b)

---

### D-11 — §8b Gouvernance Θ versionnée + règle de rétrocompatibilité

**Question** : Définir Θ comme artefact versionné (`Θ.version`, `Θ.valid_from`,
`Θ.hypotheses`) avec règle explicite de rétrocompatibilité lors d'un changement de Θ ?

**Ce que ça apporte** : ferme une ambiguïté d'implémentation (manquement M4 REV12B) —
le comportement des CLAIMs ACTIVE lors d'un retrait d'hypothèse de Θ est undefined
dans la spec v1.1.

**Options** :
- A : Définir `Θ.version` comme optionnel NMT 2 + règle de rétrocompatibilité en
  Partie B §B.6
- B : Reporter NMT 3 — Θ est statique en NMT 2, le problème est hypothétique
- C : Intégrer uniquement la règle de rétrocompatibilité (sans versioning complet)
  comme note dans Partie B

**Éléments pour trancher** :
- En NMT 2 avec Θ statique, le problème de rétrocompatibilité est hypothétique —
  il devient réel en NMT 3 quand Θ peut évoluer en opération
- La règle est formellement correcte mais ajoute de la complexité à un composant
  déjà non trivial
- Absence de convergence externe = contribution prospective, argument CCP-2

**Question ouverte QO-BR-01** : limite `max_pending_review_per_theta_change` —
non encore résolue.

**Dépendances** : D-10 (§8a prérequis logique)

---

## Questions ouvertes de la branche (bloquantes pour certaines décisions)

| QO | Question | Bloque | Difficulté de résolution |
|---|---|---|---|
| QO-BR-01 | Limite `max_pending_review_per_theta_change` — nécessaire ? | D-11 | Faible (décision de conception) |
| QO-BR-02 | Calibration `validation_level1_timeout_ms` — benchmark RTOS disponible ? | D-02 | Moyenne (recherche de référence) |
| QO-BR-03 | Sortie quarantaine par lot — procédure à définir ? | D-08 | Faible (décision de conception) |

Les trois QO ont des réponses provisoires dans la session_branche_completude (50 ms
conservateur, sortie par lot vers UNREGISTERED, limite configurable) — elles peuvent
être adoptées sans recherche supplémentaire si Andrei les valide.

---

## Ce que cette branche NE touche PAS

Pour mémoire et clarté :
- Les cinq invariants du CLAIM
- La règle cardinale sur m(∅)
- La propriété stateless des agents
- La structure du CLAIM lui-même (aucun champ ajouté au CLAIM, sauf §3a optionnel)
- La Partie A soumise au portail IDEeS (toutes les propositions ciblent Partie B /
  GitHub annex ou configuration orchestrateur)

---

## Statut de la branche

```
Branche          : BR-2026-CLAIM_completude
Documents source : CLAIM_completude_v0_3_consolidee.md (ANAMNESE)
                   REV12B.md (instance Analyste)
                   layer_1/2/3_*.md (Jules)
                   BR-2026-CLAIM_completude_v0.2.md (deep search)
Révision adverse : ✓ complète (REV12B — 5 manquements, tous résolus en v0.3)
Deep search      : ✓ complet (Couches 1+2+3, corpus Jules vérifié cohérent)
Décisions        : 11 en attente (D-01 à D-11)
Questions ouv.   : 3 (QO-BR-01/02/03, réponses provisoires disponibles)
Prochaine action : révision branches 2, 3, 4 → compilation tableau final
```

---

*Document de dette de décision — branche BR-2026-CLAIM_completude*
*Produit le 21 mai 2026 — session_branche_completude*
*Aucune intégration avant session de décision finale toutes branches*
