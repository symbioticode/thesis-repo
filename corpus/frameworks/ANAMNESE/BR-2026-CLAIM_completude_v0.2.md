# CLAIM — Proposition de complétude
**Version** : 0.2 — 21 mai 2026
**Statut** : PENDING — soumis pour validation Andrei
**Nature** : Analyse comparative, références corpus externe, réponses aux manquements REV12B
**Précédent** : v0.1 — 16 mai 2026 (AMANMESE instance)
**Révision adverse** : REV12B.md — instance Analyste
**Corpus externe** : layer_1_generic_problem.md, layer_2_specific_invariants.md, layer_3_counter_examples.md (Jules)
**Deep search** : session_branche_completude — 21 mai 2026

---

## Note de version

La v0.1 a fait l'objet d'une révision adverse structurée (REV12B) identifiant cinq manquements, dont deux de gravité **Élevée**. La présente version v0.2 intègre :

1. Les références de corpus externe produites par le deep search (Couches 1, 2, 3 de la méthode REV12B Partie 2)
2. La vérification de cohérence avec les fichiers layer_*.md de Jules (convergence confirmée sans contradiction)
3. Les réponses formelles aux cinq manquements de REV12B, avec solutions pour les gravités Élevée et Moyenne
4. La mise à jour du tableau de synthèse avec NMT cibles et statuts de validation

Aucune des propositions de la v0.1 n'a été retirée. Certaines ont été reformulées pour tenir compte des manquements.

---

## Préambule — Convergence externe validée

### Réponse au manquement 1 REV12B (gravité Élevée)

Le préambule de la v0.1 affirmait une convergence avec des "travaux antérieurs dans des domaines distincts" sans citer ces travaux. REV12B identifiait cette affirmation comme une pétition de principe.

Le deep search produit la réponse suivante, par composant :

**§7 (log certifiable) — convergence FORTE, réfutation de la pétition de principe.**
Cinq champs structurels (`log_id`, `timestamp`, `lifecycle_transition`, `transition_cause`, hash d'intégrité) sont retrouvés de façon indépendante dans trois domaines distincts n'ayant eu aucun accès à la spec CLAIM :

- GxP Audit Trail (FDA 21 CFR Part 11 / industrie pharmaceutique) : record ID, event type, timestamp, previous/new values, reason/comment — cinq correspondances directes [source : sgsystemsglobal.com/glossary/audit-trail-gxp]
- STANAG 4559 Ed.3 (NATO ISR Library Interface) : identifiant unique, horodatage, provenance de chaîne, CreationMgr/UpdateMgr [source : GlobalSpec STANAG 4559 ; UAV Data Exchange Testbed, DTIC AD1003629]
- Blockchain audit genomique (NIH/NCI 2020) : node, id, user, resource, activity, timestamp, reference_id avec intégrité SHA-256 [source : PMC7372873]

Les trois champs épistémiques de TP-02 (`m_empty_before`, `m_empty_after`, `belnap_state_after`) sont **absents de tous les corpus consultés** — ce sont les champs originaux de la contribution CLAIM.

**Conclusion** : la convergence n'est pas un artefact cognitif de substrat partagé. Les cinq champs universels reproduisent une contrainte réelle documentée dans des domaines distincts depuis les années 1990. REV12B manquement 1 est résolu.

**§1, §2, §6 — convergence partielle documentée.**
Détail dans les sections correspondantes ci-dessous.

**§3, §4, §5 — convergence confirmée par layer_2_specific_invariants.md (Jules).**
Ces composants ne faisaient pas partie du deep search initial ; les références de Jules sont reprises et intégrées.

**§8 — absence de convergence confirmée.**
Constitue une contribution prospective documentable en CCP-2.

---

## 1. Cycle de vie épistémique des CLAIMs entrants

### Lacune identifiée (inchangée v0.1)

B.1 définit la politique de rejet mais pas le cycle de vie complet d'un CLAIM valide. Deux angles morts : sémantique de l'expiration silencieuse, règle de remplacement sur double-émission du même agent.

### Proposition (inchangée v0.1)

Sept statuts épistémiques : **RECEIVED → VALID → ACTIVE → EXPIRED / SUPERSEDED / REJECTED / VOID**

*[Texte complet des définitions : voir v0.1 §1]*

### Références corpus externe

| Source externe | Convergence observée | Delta significatif |
|---|---|---|
| STANAG 4559 (NSILI) | Partielle | États de "publication", "validation", "expiration" — ne couvre pas SUPERSEDED ni VOID [GlobalSpec STANAG 4559] |
| Dublin Core Metadata | Partielle | `date.valid`, `date.available` — moins granulaire que 7 statuts [layer_2_specific_invariants.md] |
| A2A Protocol v0.3 (Google, 2025) | Partielle | 9 états formels (submitted, working, input-required, completed, canceled, failed, rejected, auth-required, unknown). Transitions déterministes, état terminal immuable [a2a-protocol.org/v0.3.0/specification] |
| Agent Contracts (arXiv 2510.14133, 2025) | Partielle | États EXPIRED, TERMINATED, FAILED avec conditions de garde formelles. Exactement un état terminal par contrat [arxiv.org/pdf/2510.14133] |

**Verdict** : CONVERGENCE PARTIELLE. Le pattern "états mutuellement exclusifs + transitions déterministes + terminal immuable" est universel dans les protocoles multi-agents modernes. **SUPERSEDED** (remplacement épistémique par le même agent sur la même hypothèse) et **VOID** (invalidation par contradiction extérieure) sont absents de tous les corpus — contribution originale documentable en CCP-2.

---

## 2. Cascade de validation à trois niveaux

### Lacune identifiée (inchangée v0.1)

Liste plate de B.1 sans ordre de priorité. Ambiguïté sur le log en cas de double-échec. Coût computationnel non optimisé pour les systèmes embarqués.

### Proposition (inchangée v0.1)

Trois niveaux ordonnés : **Niveau 0** O(1) intégrité structurelle → **Niveau 1** O(log n) résolvabilité provenance → **Niveau 2** O(k) cohérence contextuelle. Arrêt au premier niveau défaillant.

### Réponse au manquement 5 REV12B (gravité Moyenne)

REV12B §2 : la cascade ne définit pas le comportement sous charge dégradée (timeout niveau 1).

**Solution** : Ajout d'un paramètre `validation_level1_timeout_ms` (défaut : 50 ms) configurable dans l'orchestrateur. Si le lookup registre dépasse ce timeout, le CLAIM transite vers RECEIVED avec cause `VALIDATION_TIMEOUT` et est placé dans une file de réessai à basse priorité (max 3 tentatives). Ce comportement est conforme DO-178C : un CLAIM dont la provenance n'est pas vérifiable dans la fenêtre temporelle ne contribue pas à l'EPISTEMIC_STATE — il n'est pas pénalisé définitivement mais mis en attente. L'agent n'est pas faussement pénalisé pour une défaillance de l'orchestrateur. Ce paramètre figure dans la configuration de l'orchestrateur, pas dans le CLAIM.

### Références corpus externe

| Source externe | Convergence observée | Delta significatif |
|---|---|---|
| DO-178C (DAL B/C) | Oui (principe) | "Requirements-based testing" avec hiérarchie de criticité. "Early rejection" documenté comme invariant des systèmes certifiés [layer_2_specific_invariants.md ; LDRA Do178.org] |
| Edge Computing Architectures | Oui | Filtres de validation en cascade pour optimiser trafic et calcul [layer_2_specific_invariants.md] |
| A2A Protocol v0.3 | Partielle | Deux niveaux (syntaxe/sémantique), pas trois. Pas de cohérence croisée inter-champs [a2a-protocol.org/v0.2.5/specification] |

**Verdict** : CONVERGENCE FORTE sur le principe, ABSENCE sur la formalisation numérotée avec complexité annotée. Contribution de formalisation originale — argument direct CCP-4 (SWaP) et CCP-1 (rigueur formelle).

---

## 3. Freshness différenciée par type d'illocution

### Lacune identifiée (inchangée v0.1)

`freshness` traité comme champ uniforme pour tous les types d'illocution. Expirations prématurées pour DEDUCE, maintiens inappropriés pour OBSERVE haute dynamique.

### Proposition (partiellement modifiée)

Décroissance différenciée : **OBSERVE** exponentielle (α = e^{-λΔt}), **INFER** liée à la validité des sources, **DEDUCE** conditionnelle sur prémisses, **ASSUME** contrôlée par émetteur.

**Ajout v0.2 — réponse au manquement 3 REV12B (gravité Moyenne)** :
REV12B signale que ASSUME sans plafond configurable délègue une décision de sécurité opérationnelle à l'agent. Solution : ajout d'un paramètre `assume_max_validity_s` dans la configuration de l'orchestrateur (défaut : 3600 secondes). Ce paramètre plafonne `Δt_valid` de tout CLAIM `ASSUME` indépendamment de ce que l'agent déclare. Si l'agent déclare un `Δt_valid` supérieur, l'orchestrateur applique `min(Δt_valid_déclaré, assume_max_validity_s)` sans modifier le CLAIM — la modification est documentée dans le log de supervision avec cause `ASSUME_CAPPED`. Ce mécanisme est analogue au `stale_threshold_ratio` de §4 : une garde-fou côté orchestrateur, transparente pour l'agent, auditée dans le log.

### Références corpus externe

| Source externe | Convergence observée | Delta significatif |
|---|---|---|
| Théorie des Actes de Langage (Searle) | Partielle | Définit les types d'actes (assertif, directif...) sans fonction de décroissance temporelle associée [layer_2_specific_invariants.md] |
| Age of Information (AoI) | Partielle | Fraîcheur temporelle bien documentée, rarement couplée à la force illocutoire [layer_2_specific_invariants.md] |
| Cache HTTP (TTL) / HFT | Contre-exemple | TTL basé uniquement sur le temps écoulé, indépendant de la sémantique — différence discriminante [layer_3_counter_examples.md §3] |

**Verdict** : CONVERGENCE PARTIELLE. Freshness par illocution est une innovation spécifique à CLAIM, documentée comme telle par le contre-exemple TTL/HFT. Contribution originale.

---

## 4. Détection du stale storm (AM-03)

### Lacune identifiée (inchangée v0.1)

AM-03 classifiée NMT 4-5 sans paramètres de détection définis. Absence de seuils opérationnels.

### Proposition (inchangée v0.1)

Trois paramètres : `stale_window_duration` (défaut 60 s), `stale_threshold_ratio` (défaut 0.5), `stale_escalation_policy` (ALERT_ONLY ou AGENT_QUARANTINE).

### Références corpus externe

| Source externe | Convergence observée | Delta significatif |
|---|---|---|
| Systèmes distribués (Consensus) | Oui | Tempêtes de données obsolètes lors de reconnexions — défi classique de synchronisation [layer_2_specific_invariants.md] |
| Observabilité (SRE) | Oui | Seuils de "staleness" déclenchant des circuit breakers [layer_2_specific_invariants.md] |
| Loopy Belief Propagation | Contre-exemple | Propagation décentralisée sans orchestrateur — inapplicable à des consommateurs stateless [layer_3_counter_examples.md §4] |

**Verdict** : CONVERGENCE FORTE sur le problème. La solution par orchestrateur centralisé est justifiée par la contrainte stateless — le contre-exemple Loopy BP est l'argument négatif qui valide ce choix architectural.

---

## 5. Graphe de dépendances inter-CLAIMs léger

### Lacune identifiée (inchangée v0.1)

Sans graphe de dépendances, la propagation d'expiration des CLAIM INFER requiert O(n²) ou ignore les dépendances.

### Proposition (inchangée v0.1)

Index léger `chain_id → [chain_ids dépendants]`. Statut PENDING_REVIEW comme tampon. Dépendances uniquement déclarées (pas inférées).

### Références corpus externe

| Source externe | Convergence observée | Delta significatif |
|---|---|---|
| Réseaux Bayésiens | Oui (Forte) | Graphes pour propagation de probabilités et inférences [layer_2_specific_invariants.md] |
| Belief Propagation (Pearl) | Oui (Forte) | Algorithmes standard pour cohérence dans réseaux de croyances [layer_2_specific_invariants.md] |

**Verdict** : CONVERGENCE FORTE sur la structure. Le delta CLAIM est la contrainte "dépendances déclarées uniquement" (pas inférées) — conséquence directe de INV-01 (l'orchestrateur ne tranche pas). NMT 3.

---

## 6. Protocole d'entrée d'un nouvel agent

### Lacune identifiée (inchangée v0.1)

Tension stateless vs. confiance progressive : accepter immédiatement (risque pollution) ou rejeter (perte stateless).

### Proposition (reformulée pour répondre au manquement 2 REV12B)

États agent : **UNREGISTERED → REGISTERED → QUARANTINED**

`newcomer_trust_weight` (défaut 0.5) appliqué multiplicativement à `belief_mass` avant combinaison TBM.

### Réponse au manquement 2 REV12B (gravité Élevée)

REV12B identifie une tension structurelle entre §6 et §7 : le discount `newcomer_trust_weight` modifie silencieusement la `belief_mass` sans que le log de supervision ne le capture, rendant l'audit DO-178C impossible.

**Solution** : Extension du format log certifiable (§7) avec un champ optionnel `trust_discount_applied` :

```
trust_discount_applied : {
  chain_id   : <chain_id de l'agent UNREGISTERED>,
  factor     : <valeur newcomer_trust_weight appliquée>,
  mass_before: <belief_mass déclarée par l'agent>,
  mass_after : <belief_mass effective après discount>
}
```

Ce champ est présent dans l'entrée de log **uniquement** si un discount a été appliqué (null sinon). Un auditeur DO-178C peut ainsi reconstruire la contribution réelle de tout agent UNREGISTERED à partir du log. La tension §6/§7 est résolue : le discount est opérationnel ET auditable.

Cette extension respecte le contrat §7 : TP-02 peut l'ajouter, ne peut pas la supprimer.

**Clarification conceptuelle — réponse à la question INV-01** :
Le `newcomer_trust_weight` n'est pas une violation d'INV-01 car c'est l'**orchestrateur** qui applique le discount, non l'agent émetteur. L'agent transmet sa `belief_mass` sans modification. L'orchestrateur applique un facteur de pondération externe au CLAIM, comme il appliquerait un discounting temporel. La propriété "l'émetteur ne peut pas interpréter son propre état dans le message qu'il transmet" est préservée.

La distinction avec les systèmes de réputation (EigenTrust, P2P) est formelle :
- EigenTrust : confiance basée sur l'historique **comportemental** de la source
- CLAIM §6 : discount basé sur le **nombre de CLAIMs validés structurellement** — critère formel, pas comportemental [layer_3_counter_examples.md §2]

### Références corpus externe

| Source externe | Convergence observée | Delta significatif |
|---|---|---|
| FIPA (Agent Management) | Oui | Étapes d'enregistrement et découverte pour nouveaux agents [layer_2_specific_invariants.md] |
| Trust bootstrapping MAS (ResearchGate 2015) | Partielle (problème) | Problème du bootstrap documenté et nommé. Solutions : confiance uniforme, dérivée du type de nœud, propagée depuis pairs [ResearchGate 308671453] |
| TrustTrack (arXiv 2507.22077, 2025) | Partielle | Protocole DID + logs signés pour agents vérifiables. Modèle tout-ou-rien (vérifié/non vérifié) — pas de discount progressif [arXiv 2507.22077] |
| EigenTrust / systèmes réputation P2P | Contre-exemple | Confiance par historique transactionnel vs. validité intrinsèque de la masse — différence discriminante [layer_3_counter_examples.md §2] |

**Verdict** : CONVERGENCE PARTIELLE sur le problème, ABSENCE sur la solution TBM. Intégration originale d'un problème MAS connu dans le cadre DS. L'auditabilité est maintenant garantie par l'extension §7.

---

## 7. Format de log certifiable — complément à TP-02

### Lacune identifiée (inchangée v0.1, enrichie)

TP-02 existe (LOG_certifiable.md v1.1, 11 champs). La v0.1 proposait 7 champs. La convergence avec TP-02 est maintenant validée par corpus externe.

### Proposition (étendue v0.2)

Champs obligatoires v0.1 (inchangés) + extension pour le discount de provenance (§6) :

```
log_id                  : UUID non réutilisable
timestamp_reception     : UTC ISO 8601, précision milliseconde
claim_chain_id          : chain_id du CLAIM (même si non résolvable)
lifecycle_transition    : ex. RECEIVED→REJECTED, ACTIVE→EXPIRED
transition_cause        : code formel (B.1, CLOCK, STALE_STORM, ASSUME_CAPPED...)
epistemic_state_before  : snapshot (belnap_state, conflict_mass) si transition modifie l'EPISTEMIC_STATE
operator_notified       : booléen
trust_discount_applied  : {chain_id, factor, mass_before, mass_after} — présent si discount appliqué, null sinon
```

Le champ `trust_discount_applied` est la réponse formelle au manquement 2 REV12B.

### Références corpus externe

| Source externe | Convergence observée | Delta significatif |
|---|---|---|
| DO-178C / DO-330 | Oui (Forte) | Traçabilité stricte des données et décisions pour certification aéronautique [layer_2_specific_invariants.md ; LDRA do178.org] |
| GxP Audit Trail (FDA 21 CFR Part 11) | Oui (Forte) | record ID, event type, timestamp, previous/new values, reason/comment. Append-only, tamper-evident [sgsystemsglobal.com/glossary/audit-trail-gxp] |
| Audit Trail ISO 27001 | Oui | Standardisation logs pour intégrité et non-répudiation [layer_2_specific_invariants.md] |
| STANAG 4559 (NSILI) | Partielle | Identifiant unique, horodatage, provenance de chaîne. Orienté produit/fichier, pas transition épistémique [DTIC AD1003629] |
| Blockchain audit genomique (NIH, PMC7372873) | Oui | node, id, user, resource, activity, timestamp, reference_id + hash SHA-256. Convergence sur UUID+timestamp+hash [PMC7372873] |

**Verdict** : CONVERGENCE FORTE. Cinq champs universels (UUID, timestamp, transition, cause, hash) retrouvés dans trois domaines distincts. Trois champs épistémiques (`m_empty_before`, `m_empty_after`, `belnap_state_after`) absents de tous les corpus — contribution originale CLAIM. Le champ `trust_discount_applied` est une extension v0.2 pour l'auditabilité §6. **Manquement 1 REV12B résolu formellement.**

---

## 8. Θ — Gouvernance du cadre de discernement

### Lacune identifiée (inchangée v0.1)

Θ statique dans la spec actuelle. Comportement undefined sur CLAIM hors-Θ. Rétrocompatibilité des CLAIMs ACTIVE lors d'un changement de Θ non définie.

### Proposition (enrichie pour répondre au manquement 4 REV12B)

Θ versionné avec `Θ.version` (optionnel NMT 2, obligatoire NMT 3+). Autorité de modification : opérateur humain uniquement. CLAIM hors-Θ → REJECTED avec cause `HYPOTHESIS_OUT_OF_FRAME`.

### Réponse au manquement 4 REV12B (gravité Moyenne)

REV12B identifie que §8 ne définit pas le comportement des CLAIMs déjà ACTIVE lors d'un changement de version de Θ (trois comportements possibles laissés ambigus).

**Solution** : Règle explicite de rétrocompatibilité lors du changement Θ_v(n) → Θ_v(n+1) :

- Si H_k est **présente dans Θ_v(n+1)** : les CLAIMs ACTIVE sur H_k restent ACTIVE, leur `Θ.version` est mis à jour automatiquement par l'orchestrateur dans le registre interne (pas dans le CLAIM — INV-01 tenu).
- Si H_k est **absente de Θ_v(n+1)** (hypothèse retirée) : les CLAIMs ACTIVE sur H_k transitent vers **PENDING_REVIEW** (statut §5) avec cause `THETA_VERSION_MISMATCH`. L'opérateur est notifié via C-07. L'opérateur décide : VOID (hypothèse définitivement abandonnée) ou ACTIVE maintenu jusqu'à expiration naturelle (fenêtre opérationnelle de transition).
- **Pas de transition VOID automatique** : retirer une hypothèse de Θ est une décision opérationnelle qui ne doit pas invalider automatiquement des CLAIMs en cours de contribution à l'EPISTEMIC_STATE. L'opérateur humain conserve la décision finale — c'est l'équivalent de la règle cardinale sur m(∅) appliquée à la gouvernance de Θ.

Cette règle élimine l'ambiguïté des trois comportements possibles signalée par REV12B et est cohérente avec INV-01 et la règle cardinale.

### Références corpus externe

| Source externe | Convergence observée | Delta significatif |
|---|---|---|
| Ontologies dynamiques (OWL versioning) | Partielle | Gestion de versions d'ontologies, rarement intégrée en temps réel opérationnel [layer_2_specific_invariants.md] |
| Schema Versioning (DB) | Partielle | Évolution de schémas de données sans sémantique du Frame of Discernment [layer_2_specific_invariants.md] |
| Propagation entre frames DS (Springer 1993) | Partielle | Problème de propagation entre frames distinct documenté depuis 1993. Pas de protocole de gouvernance opérationnelle [Springer 10.1007/978-1-4471-3542-5_23] |

**Verdict** : ABSENCE DE CONVERGENCE sur la gouvernance opérationnelle de Θ. La question est reconnue dans la littérature DS et dans les architectures OTAN (DCRA v2). La proposition §8 v0.2 est une première réponse concrète avec règle de rétrocompatibilité. Contribution prospective — CCP-2 ou page 9a.

---

## Réponses aux manquements REV12B — bilan

| Manquement REV12B | Gravité | Statut v0.2 | Solution apportée |
|---|---|---|---|
| M1 — Convergence non falsifiable | **Élevée** | **RÉSOLU** | Deep search 3 domaines indépendants pour §7. §1/§2/§6 partiels documentés. |
| M2 — §6+§7 tension auditabilité | **Élevée** | **RÉSOLU** | Champ `trust_discount_applied` ajouté au log. Masse avant/après discountée tracée. |
| M3 — §3 ASSUME sans plafond | Moyenne | **RÉSOLU** | Paramètre `assume_max_validity_s` dans config orchestrateur. Log cause `ASSUME_CAPPED`. |
| M4 — §8 rétrocompatibilité Θ | Moyenne | **RÉSOLU** | Règle explicite : PENDING_REVIEW + décision opérateur. Pas de VOID automatique. |
| M5 — §2 charge dégradée | Moyenne | **RÉSOLU** | Paramètre `validation_level1_timeout_ms`. File de réessai 3 tentatives. Cause `VALIDATION_TIMEOUT`. |

Tous les manquements de gravité Élevée et Moyenne trouvent une réponse formelle dans la v0.2.

---

## Synthèse — tableau de décision mis à jour

| Composant | Spec v1.1 | Proposition v0.2 | Verdict corpus | NMT cible | Destination |
|---|---|---|---|---|---|
| §1 Cycle de vie 7 statuts | Rejet B.1 seulement | 7 statuts + SUPERSEDED/VOID originaux | Convergence partielle — SUPERSEDED/VOID inédits | NMT 2 | Partie B §B.3 |
| §2 Cascade validation 3 niveaux | Liste plate | Cascade numérotée + timeout charge dégradée | Convergence forte principe / Absence formalisation | NMT 2 | B.1 sous-section + arg. CCP-4 |
| §3 Freshness par illocution (OBSERVE) | `Δt_valid` uniforme | `freshness_decay_rate` optionnel + `assume_max_validity_s` | Convergence partielle — innovation illocutoire | NMT 3 (OBSERVE NMT 2) | §A.3 enrichissement |
| §4 Stale storm | AM-03 NMT 4-5 | 3 paramètres de détection | Convergence forte problème | NMT 3 | Partie B §B.4 + fermeture AM-03 |
| §5 Graphe dépendances | Absent | Index léger `chain_id → [chain_ids]` | Convergence forte (Bayésien/Pearl) | NMT 3 | research/post_submission |
| §6 Protocole nouvel agent | Absent (stateless) | UNREGISTERED→REGISTERED→QUARANTINED + auditabilité | Convergence partielle — solution TBM inédite | NMT 3 | Partie B §B.5 |
| §7 Log certifiable | TP-02 non spécifié | 7 champs + `trust_discount_applied` | **Convergence forte — 3 domaines distincts** | NMT 2 | Commentaire LOG_certifiable.md |
| §8 Gouvernance Θ | Θ statique | `HYPOTHESIS_OUT_OF_FRAME` + règle rétrocompat. | Absence convergence = contribution prospective | NMT 3 (`HYPOTHESIS_OUT_OF_FRAME` NMT 2) | B.1 cas 6 + Partie B §B.6 |

Les propositions NMT 2 (§1 partiel, §2, §3 OBSERVE, §7, §8 partiel) sont des clarifications sans ajout de complexité d'implémentation.
Les propositions NMT 3 sont des extensions fondées sur des besoins opérationnels prévisibles.

**Aucune proposition ne modifie les cinq invariants du CLAIM, la règle cardinale sur m(∅), ni la propriété stateless.** Toutes opèrent au niveau de l'orchestrateur et du registre de provenance.

---

## Plan d'intégration Sprint

### Intégrations immédiates (NMT 2 — avant J19)

**B.1** :
- Ajouter l'ordre de cascade §2 comme sous-section "Ordre d'évaluation" (Niveau 0/1/2)
- Ajouter `HYPOTHESIS_OUT_OF_FRAME` comme 6e cas de malformation §8 partiel
- Ajouter paramètre `assume_max_validity_s` dans config orchestrateur (note §3)

**Partie B §B.3** : cycle de vie 7 statuts §1

**Partie B §B.4** : paramètres stale storm §4 + fermeture formelle AM-03

**Partie B §B.5** : protocole nouvel agent §6 + champ `trust_discount_applied`

**LOG_certifiable.md** : note de convergence externe (5 champs universels documentés dans 3 domaines)

### Archivage post-J19

**research/post_submission_ideas.md** : §5 graphe dépendances, §8 versioning Θ complet, §3 freshness INFER/DEDUCE

---

## Questions ouvertes résiduelles (pour ANAMNESE)

**QO-BR-01** : La règle de rétrocompatibilité §8 (PENDING_REVIEW + décision opérateur) est-elle cohérente avec le comportement de l'orchestrateur sous forte charge lors d'un changement de Θ impliquant de nombreux CLAIMs ACTIVE simultanément ? Une limite `max_pending_review_per_theta_change` est-elle nécessaire ?

**QO-BR-02** : Le paramètre `validation_level1_timeout_ms` (défaut 50 ms) est-il calibré sur des architectures embarquées réelles ? Une référence à des benchmarks de lookup registre embarqué (RTOS, VxWorks) renforcerait l'argument SWaP de CCP-4.

**QO-BR-03** : La transition QUARANTINED → sortie uniquement par décision humaine est-elle opérationnellement tenable dans un scénario de reconnexion massive (perte réseau suivie de reconnexion de N agents simultanément) ? Une procédure de sortie de quarantaine par lot devrait-elle être définie ?

---

*BR-2026-CLAIM_completude v0.2 — 21 mai 2026*
*Statut : PENDING — à valider par Andrei avant intégration dans CLAIM_specification.md*
*Convergence externe : validée par deep search 3 domaines (§7), corpus layer_*.md Jules (§3/§4/§5)*
*Manquements REV12B : tous résolus (2 Élevée, 3 Moyenne)*
