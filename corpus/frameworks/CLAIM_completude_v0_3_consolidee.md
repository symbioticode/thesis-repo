# CLAIM — Proposition de complétude consolidée
**Version** : 0.3 — 21 mai 2026
**Statut** : PENDING — soumis pour validation Andrei
**Nature** : Consolidation de deux instances indépendantes (v0.1 instance A · v0.2 instance B)
**Précédents** :
- v0.1 — instance A (ANAMNESE) — 8 composants, propositions NMT 2 et NMT 3
- v0.2 — instance B — révision adverse REV12B + deep search externe + corpus Jules
**Convergence externe** : validée par deep search 3 domaines distincts (§7) · corpus layer_*.md (§3/§4/§5)
**Manquements REV12B** : tous résolus dans la présente version

---

## Note de consolidation

Les deux instances ont produit des propositions identiques dans leur structure sur 8 composants,
sans coordination préalable. La v0.2 a ensuite soumis la v0.1 à une révision adverse (REV12B)
identifiant cinq manquements, dont deux de gravité Élevée, tous résolus.

La présente version consolide les deux documents en une seule source de vérité.
Les résolutions REV12B sont intégrées directement dans chaque section concernée —
elles ne sont plus des addenda mais des éléments constitutifs de la proposition.

**Règle de consolidation** : en cas de conflit entre les deux versions, la formulation
la plus précise ou la plus contraignante est retenue. Aucune proposition n'a été retirée.

---

## Préambule — Convergence structurelle

Plusieurs corpus de travaux antérieurs menés dans des domaines distincts —
gestion de connaissance distribuée, continuité cognitive inter-sessions,
navigation de graphes épistémiques, systèmes distribués — ont abouti indépendamment
aux mêmes invariants fondamentaux que le CLAIM.

Cette convergence n'est pas superficielle et n'est pas un artefact de substrat cognitif
partagé. Elle a été vérifiée par deep search dans trois domaines n'ayant eu aucun accès
à la spec CLAIM : industrie pharmaceutique (FDA 21 CFR Part 11 / GxP Audit Trail),
standards ISR NATO (STANAG 4559 Ed.3), et bioinformatique (audit genomique NIH/NCI 2020).
Les cinq champs structurels universels retrouvés — identifiant unique, horodatage,
transition de cycle de vie, cause de transition, hash d'intégrité — convergent vers
les exigences du §7 (log certifiable).

La convergence reflète une contrainte profonde commune : **comment faire coopérer des
producteurs d'information hétérogènes avec des consommateurs qui n'ont pas accès à leur
état interne ?** La réponse dans chaque domaine, et dans le CLAIM, est structurellement
identique : un format d'interface minimal, auto-déclarant, avec un cycle de vie
épistémique explicite, et une règle cardinale interdisant à l'émetteur d'interpréter
son propre état dans le message qu'il transmet.

**Ce que le corpus externe n'a pas retrouvé** confirme la contribution originale du CLAIM :
les trois champs épistémiques du log certifiable (`m_empty_before`, `m_empty_after`,
`belnap_state_after`), les statuts SUPERSEDED et VOID du cycle de vie, la freshness
différenciée par type d'illocution, et la gouvernance opérationnelle de Θ sont absents
de tous les corpus consultés.

**Règle d'application de ce préambule** : aucune des propositions ci-dessous ne modifie
les cinq invariants du CLAIM, la règle cardinale sur m(∅), ni la propriété stateless.
Toutes opèrent au niveau de l'orchestrateur et du registre de provenance.

---

## 1. Cycle de vie épistémique des CLAIMs entrants

### Lacune dans la spec v1.1

B.1 définit une politique de rejet par cas de malformation mais pas le cycle de vie
complet d'un CLAIM valide. Deux angles morts : sémantique de l'expiration silencieuse
(un CLAIM dont `Δt_valid` expire est-il ignoré ou signalé ?), et règle de remplacement
sur double-émission du même agent (le second CLAIM remplace-t-il le premier par
convention ou par règle formelle ?).

### Proposition — sept statuts

**RECEIVED** — Le CLAIM est arrivé. Les vérifications structurelles (§2 Niveau 0) n'ont
pas encore été appliquées. Acteur : couche de réception de l'orchestrateur. Durée :
millisecondes. Transition déclenchée par : arrivée du message réseau.

**VALID** — Le CLAIM a passé les trois niveaux de la cascade de validation (§2). Il est
éligible à la combinaison TBM. Acteur : moteur de validation de l'orchestrateur.
Transition déclenchée par : succès des trois niveaux de cascade.

**ACTIVE** — Le CLAIM est dans sa fenêtre `Δt_valid` et contribue à l'EPISTEMIC_STATE
courant. C'est le seul statut dans lequel un CLAIM influence `m_combined(∅)` et
`belnap_state`. Acteur : moteur de combinaison TBM. Transition déclenchée par :
passage à VALID dans une fenêtre temporelle valide.

**EXPIRED** — La fenêtre `Δt_valid` est dépassée. Le CLAIM n'est plus actif mais est
conservé dans le log de supervision pour auditabilité. Il ne contribue plus à aucune
combinaison. Acteur : horloge système de l'orchestrateur, log de supervision.
Transition déclenchée par : `t_courant > t_obs + Δt_valid`. Automatique, aucune
décision humaine requise.

**SUPERSEDED** — Un CLAIM plus récent du même agent (`provenance.chain_id` identique)
sur la même hypothèse Θ est arrivé VALID. Le CLAIM précédent est archivé avec référence
au successeur. Acteur : registre de provenance de l'orchestrateur. Transition déclenchée
par : réception d'un nouveau CLAIM VALID du même `chain_id` sur la même hypothèse.
Ce statut résout formellement le problème de double-émission. SUPERSEDED est absent
de tous les protocoles multi-agents consultés — contribution originale.

**REJECTED** — Le CLAIM a échoué à au moins un niveau de la cascade de validation (§2).
Écarté de toute combinaison. Signalé dans le log de supervision avec le niveau et la
cause de l'échec. Acteur : couche de validation, log de supervision.

**VOID** — Le CLAIM est référencé (par un SUPERSEDED ou par le log) mais son contenu
n'est plus interprétable. Cas typique : agent déconnecté dont le `chain_id` n'est plus
résolvable. Ce statut préserve la traçabilité sans maintenir le contenu actif.
VOID est absent de tous les protocoles multi-agents consultés — contribution originale.

**Règle d'invariant** : aucune transition n'est déclenchée par l'agent émetteur.
L'orchestrateur gère intégralement le cycle de vie — INV-01 tenu à tous les stades.

**Convergence externe** : le pattern "états mutuellement exclusifs + transitions
déterministes + terminal immuable" est documenté dans A2A Protocol v0.3 (9 états)
et Agent Contracts arXiv 2510.14133 (conditions de garde formelles). STANAG 4559
et Dublin Core couvrent partiellement. SUPERSEDED et VOID sont inédits.

---

## 2. Cascade de validation à trois niveaux

### Lacune dans la spec v1.1

La liste de vérifications B.1 est plate, sans ordre de priorité. Deux conséquences :
ambiguïté sur la cause reportée dans le log si deux vérifications échouent simultanément,
et coût computationnel non optimisé pour les architectures embarquées à ressources
contraintes (SWaP).

### Proposition — trois niveaux ordonnés avec arrêt au premier échec

**Niveau 0 — Intégrité structurelle** — Coût O(1), sans accès réseau ni registre.
Vérifications : masse normalisée (Σ m(A) = 1 ± ε = 1e-6), timestamp cohérent
(t_obs ≤ t_reception), timestamp non futur (t_obs ≤ t_reception), illocution dans
l'énumération {OBSERVE, INFER, DEDUCE, ASSUME}, freshness présente et bien formée.
Si échec : REJECTED immédiat, cause B.1 correspondante. L'orchestrateur ne consulte
pas le registre de provenance.

**Niveau 1 — Résolvabilité de la provenance** — Coût O(log n), lookup dans le registre
local. Vérification unique : `chain_id` résolvable dans le registre de provenance.
Si échec : REJECTED avec cause `provenance_absent`. Ne s'exécute que si le Niveau 0
a réussi. Paramètre : `validation_level1_timeout_ms` (défaut : 50 ms). Si le lookup
dépasse ce timeout, le CLAIM transite vers RECEIVED avec cause `VALIDATION_TIMEOUT`
et entre dans une file de réessai à basse priorité (max 3 tentatives). Ce comportement
est conforme DO-178C : un CLAIM dont la provenance n'est pas vérifiable dans la
fenêtre temporelle n'est pas pénalisé définitivement — l'agent n'est pas faussement
sanctionné pour une défaillance de l'orchestrateur.

**Niveau 2 — Cohérence contextuelle** — Coût O(k), comparaison avec les CLAIMs ACTIVE
en mémoire. Vérifications : le CLAIM n'est pas un doublon ACTIVE du même `chain_id`
sur la même hypothèse (déclenchement de SUPERSEDED si oui), et la fenêtre `Δt_valid`
n'est pas expirée au moment de la validation. C'est le seul niveau qui peut modifier
l'état d'un autre CLAIM (transition SUPERSEDED sur le prédécesseur).

**Convergence externe** : convergence forte sur le principe (DO-178C "early rejection",
edge computing cascade validation). A2A Protocol v0.3 a deux niveaux, pas trois —
l'absence de cohérence contextuelle inter-CLAIMs est la différence discriminante.
Formalisation avec complexité annotée : contribution originale, argument CCP-4 (SWaP).

---

## 3. Freshness différenciée par type d'illocution

### Lacune dans la spec v1.1

`freshness` est traité comme un champ uniforme `(t_obs, Δt_valid)` pour tous les types
d'illocution. Cette uniformité produit des comportements incorrects dans deux cas
fréquents : expirations prématurées pour les CLAIMs DEDUCE dont les prémisses logiques
sont encore valides, et maintiens inappropriés pour les CLAIMs OBSERVE dans des
environnements à haute dynamique (radar, SIGINT).

### Proposition — décroissance différenciée par illocution

**OBSERVE** — Décroissance exponentielle : α(Δt) = e^{-λ·Δt}. L'agent déclare
`freshness_decay_rate` (λ) dans le CLAIM — paramètre optionnel en NMT 2, si absent
le comportement actuel (`Δt_valid` binaire) s'applique par défaut. λ est calibré par
domaine (radar, SIGINT, EO/IR) lors de la configuration système. L'orchestrateur
applique la décroissance — l'agent ne la connaît pas.

**INFER** — Décroissance liée à la validité des CLAIMs sources déclarés dans
`provenance.chain_id`. Un CLAIM INFER passe EXPIRED quand au moins un CLAIM source
passe EXPIRED ou VOID. L'orchestrateur maintient l'index de dépendances (§5) pour
propager cet événement. Aucun paramètre temporel supplémentaire requis.

**DEDUCE** — Décroissance conditionnelle sur prémisses : le CLAIM reste ACTIVE
tant que ses prémisses logiques déclarées sont ACTIVE, indépendamment du temps
écoulé. L'expiration est déclenchée par un événement (changement d'état d'une
prémisse), pas par l'horloge. Ce mécanisme est le plus coûteux — applicable
uniquement aux CLAIMs explicitement marqués DEDUCE, pas par défaut.

**ASSUME** — `Δt_valid` contrôlé par l'émetteur. Garde-fou côté orchestrateur :
paramètre `assume_max_validity_s` (défaut : 3600 secondes) dans la configuration
de l'orchestrateur. Si l'agent déclare un `Δt_valid` supérieur, l'orchestrateur
applique `min(Δt_valid_déclaré, assume_max_validity_s)` sans modifier le CLAIM.
La modification est documentée dans le log avec cause `ASSUME_CAPPED`. Ce mécanisme
est transparent pour l'agent et auditable — il résout la délégation non plafonnée
d'une décision de sécurité opérationnelle à l'agent.

**Convergence externe** : Speech Act Theory (Searle) définit les types d'actes sans
décroissance temporelle. Age of Information (AoI) documente la fraîcheur sans
couplage illocutoire. Cache HTTP/TTL est le contre-exemple discriminant : TTL uniforme
indépendant de la sémantique — exactement ce que cette proposition corrige.
Freshness différenciée par illocution : contribution originale.

---

## 4. Détection du stale storm

### Lacune dans la spec v1.1

AM-03 identifie le comportement sous flux continu de CLAIMs expirés comme failure
mode NMT 4-5 sans paramètres de détection définis. Cette classification retarde
inutilement une spécification qui peut être documentée dès maintenant sans complexité
d'implémentation.

Un stale storm se produit quand un agent émet des CLAIMs dont `Δt_valid` est
systématiquement inférieur à la latence réseau + traitement. Les CLAIMs arrivent
déjà EXPIRED — ignorés individuellement, leur accumulation signale une anomalie
structurelle (mauvaise calibration de `Δt_valid`, dégradation réseau, agent défaillant).

### Proposition — trois paramètres configurables dans l'orchestrateur

`stale_window_duration` — fenêtre d'observation (défaut : 60 secondes).

`stale_threshold_ratio` — ratio CLAIMs EXPIRED à la réception / total CLAIMs reçus
dans la fenêtre, par `chain_id` (défaut : 0.5). Si dépassé, l'orchestrateur émet
une alerte C-07 avec diagnostic `STALE_STORM` et l'identifiant de l'agent concerné.

`stale_escalation_policy` — comportement de l'orchestrateur pendant le stale storm
détecté : `ALERT_ONLY` (émettre l'alerte, continuer à ignorer les CLAIMs expirés)
ou `AGENT_QUARANTINE` (suspendre la contribution de l'agent à l'EPISTEMIC_STATE
jusqu'à décision opérateur). Défaut : `ALERT_ONLY` — conforme à la règle cardinale,
l'orchestrateur n'écarte pas un agent sans décision humaine.

Ces trois paramètres vivent dans la configuration de l'orchestrateur. L'agent
n'a pas à savoir qu'il est en stale storm — INV-01 tenu.

**Fermeture formelle d'AM-03** : avec ces paramètres, AM-03 passe de NMT 4-5 à NMT 3.

**Convergence externe** : convergence forte sur le problème (systèmes distribués,
circuit breakers SRE/observabilité). Loopy Belief Propagation est le contre-exemple :
propagation décentralisée sans orchestrateur, inapplicable à la contrainte stateless
— ce contre-exemple valide positivement le choix d'orchestrateur centralisé.

---

## 5. Graphe de dépendances inter-CLAIMs léger

### Lacune dans la spec v1.1

Sans structure de dépendances, la propagation de l'expiration d'un CLAIM OBSERVE
vers les CLAIMs INFER qui en dépendent requiert soit un scan O(n²) de tous les
CLAIMs ACTIVE à chaque événement d'expiration, soit l'ignorance des dépendances
(correctness incorrecte). Les deux options sont inacceptables en production.

### Proposition — index léger de dépendances déclarées

Structure : dictionnaire `chain_id → [chain_ids dépendants]`, maintenu dans
l'orchestrateur. Mis à jour à chaque CLAIM passant VALID. La source de vérité
est la provenance PROV-O déclarée par chaque agent dans son CLAIM —
l'orchestrateur ne construit pas ce graphe par inférence, il le lit depuis les
déclarations. Cette contrainte est directe : INV-01 appliqué au graphe de dépendances.

**Propagation** : quand un CLAIM passe EXPIRED ou VOID, l'orchestrateur consulte
l'index et marque les CLAIMs dépendants PENDING_REVIEW. Ce statut transitoire
déclenche une réévaluation de leur contribution à l'EPISTEMIC_STATE sans les
invalider immédiatement. L'opérateur C-07 est notifié si un CLAIM en PENDING_REVIEW
était en phase de contribution active à l'EPISTEMIC_STATE.

**Limite déclarée** : cet index ne capture que les dépendances explicitement
déclarées via PROV-O. Les corrélations cachées (QO-02 — source physique commune
non déclarée) restent hors périmètre NMT 1-3. La règle Denœux couvre ce cas
partiellement par idempotence ; la résolution complète est NMT 4-5.

**Convergence externe** : convergence forte (réseaux bayésiens, Belief Propagation
de Pearl). Le delta CLAIM est la contrainte "dépendances déclarées uniquement" —
dans les réseaux bayésiens, les arêtes sont inférées ou apprises. Ici elles sont
déclarées par l'émetteur, ce qui est la seule option compatible avec la propriété
stateless des agents.

---

## 6. Protocole d'entrée d'un nouvel agent

### Lacune dans la spec v1.1

La propriété stateless du CLAIM permet à un agent d'émettre son premier CLAIM sans
enregistrement préalable. Cette propriété de robustesse est correcte mais laisse
ouverte une question opérationnelle : comment l'orchestrateur traite-t-il un `chain_id`
qu'il n'a jamais vu ? Accepter immédiatement à pleine masse risque la pollution de
l'EPISTEMIC_STATE par un agent non qualifié. Rejeter rompt la propriété stateless.

### Proposition — cycle de vie agent à trois états

**UNREGISTERED** — Le `chain_id` n'est pas dans le registre. Les CLAIMs de cet
agent suivent le cycle de vie normal (RECEIVED → VALID → ACTIVE) mais leur
contribution à l'EPISTEMIC_STATE est pondérée par `newcomer_trust_weight` (défaut :
0.5), appliqué multiplicativement à `belief_mass` avant combinaison TBM.
Ce discount est appliqué par l'orchestrateur, transparent pour l'agent — INV-01 tenu.
Chaque application est tracée dans le log de supervision (§7, champ
`trust_discount_applied`).

**REGISTERED** — Le `chain_id` a émis au moins N CLAIMs valides (N configurable,
défaut : 3) sans violation de B.1. `newcomer_trust_weight` est retiré. L'agent
contribue à pleine masse. Transition automatique déclenchée par le registre de
l'orchestrateur — aucune action requise de l'agent.

**QUARANTINED** — L'agent a déclenché une alerte stale storm (§4) ou a dépassé
un ratio de CLAIMs REJECTED configurable. Sa contribution à l'EPISTEMIC_STATE
est suspendue. Transition déclenchée automatiquement. Sortie de quarantaine :
décision humaine uniquement. Ce mécanisme protège l'EPISTEMIC_STATE sans créer
de penalité définitive automatique — conforme à la règle cardinale.

**Distinction formelle avec les systèmes de réputation** (EigenTrust, P2P) :
le `newcomer_trust_weight` est basé sur le nombre de CLAIMs validés structurellement
(critère formel), pas sur un historique comportemental. Un agent qui émet des CLAIMs
bien formés passe REGISTERED indépendamment du contenu de ses assertions.

**Auditabilité DO-178C** : le champ `trust_discount_applied` dans le log certifiable
(§7) permet à un auditeur de reconstruire la contribution réelle de tout agent
UNREGISTERED depuis le log. La tension stateless / auditabilité est résolue :
le discount est opérationnel ET traçable.

**Convergence externe** : FIPA Agent Management couvre l'enregistrement et la
découverte. TrustTrack (arXiv 2507.22077) propose un modèle DID + logs signés
mais tout-ou-rien (vérifié / non vérifié), pas de discount progressif. EigenTrust
est le contre-exemple discriminant (confiance comportementale vs. confiance formelle).
Solution TBM avec discount progressif et auditabilité : contribution originale.

---

## 7. Format de log certifiable

### Lacune dans la spec v1.1

TP-02 est identifié comme livrable mais non encore spécifié. B.1 fait référence à
"un log de supervision horodaté" sans définir son contenu ni ce qui le rend certifiable
au sens DO-178C / IEC 61508. Ce vide est acceptable en NMT 2 à condition de définir
maintenant le contrat d'interface que TP-02 devra respecter.

### Proposition — huit champs obligatoires

```
log_id                  : UUID non réutilisable
timestamp_reception     : UTC ISO 8601, précision milliseconde
claim_chain_id          : chain_id du CLAIM (même si non résolvable)
lifecycle_transition    : ex. RECEIVED→REJECTED, ACTIVE→EXPIRED, VALID→SUPERSEDED
transition_cause        : code formel (voir tableau des causes ci-dessous)
epistemic_state_before  : snapshot {belnap_state, conflict_mass} au moment de la
                          transition — présent uniquement si la transition modifie
                          l'EPISTEMIC_STATE, null sinon
operator_notified       : booléen
trust_discount_applied  : {chain_id, factor, mass_before, mass_after} — présent si
                          un newcomer_trust_weight a été appliqué, null sinon
```

**Codes de cause formels** :

| Code | Déclencheur |
|---|---|
| B.1-MASS | Masse non normalisée (Niveau 0) |
| B.1-TIMESTAMP | Timestamp manquant ou futur (Niveau 0) |
| B.1-EXPIRED_AT_RECEPTION | Validité expirée à la réception (Niveau 0) |
| B.1-PROVENANCE | Provenance absente ou non résolvable (Niveau 1) |
| B.1-ILLOCUTION | Illocution hors énumération (Niveau 0) |
| B.1-HYPOTHESIS_OUT_OF_FRAME | Hypothèse absente de Θ courant (Niveau 2) |
| CLOCK | Expiration par horloge système (ACTIVE→EXPIRED) |
| NEWCOMER_CLAIM | Remplacement par CLAIM plus récent (ACTIVE→SUPERSEDED) |
| STALE_STORM | Déclenchement quarantaine agent |
| ASSUME_CAPPED | `Δt_valid` ASSUME plafonné par `assume_max_validity_s` |
| VALIDATION_TIMEOUT | Timeout lookup provenance (RECEIVED, file réessai) |
| THETA_VERSION_MISMATCH | CLAIMs ACTIVE lors d'un changement de version Θ |

**Contrat envers TP-02** : TP-02 peut étendre ces champs, il ne peut pas les réduire.
Les trois champs épistémiques (`m_empty_before`, `m_empty_after`, `belnap_state_after`)
que TP-02 ajoute sont les champs originaux de la contribution CLAIM — absents de tous
les corpus externes consultés.

**Convergence externe** : convergence forte dans trois domaines distincts — GxP Audit
Trail (FDA 21 CFR Part 11), STANAG 4559 Ed.3, audit genomique NIH/NCI 2020. Les
cinq champs universels (UUID, timestamp, transition, cause, hash) convergent dans les
trois corpus. Ce résultat réfute formellement toute hypothèse d'artefact cognitif.

---

## 8. Θ — Gouvernance du cadre de discernement

### Lacune dans la spec v1.1

Θ est défini comme commun, fini (|Θ| ≤ 20), statique pour NMT 1-3. Ce qui n'est pas
défini : comportement d'un CLAIM sur une hypothèse absente de Θ, mécanisme de
communication de la version courante aux agents, et — lacune critique — règle de
rétrocompatibilité pour les CLAIMs ACTIVE lors d'un changement de Θ.

### Proposition — Θ versionné avec règle de rétrocompatibilité explicite

**Structure** : Θ est un artefact versionné avec `Θ.version` (optionnel NMT 2,
obligatoire NMT 3+), `Θ.valid_from` (timestamp UTC), et `Θ.hypotheses` (liste
ordonnée avec identifiants stables). Chaque CLAIM peut inclure `Θ.version` — si
absent, l'orchestrateur assume la version courante.

**Autorité de modification** : l'opérateur humain uniquement. L'orchestrateur
ne modifie pas Θ — il signale les situations hors-Θ via C-07. Cette règle est
l'équivalent fonctionnel de la règle cardinale sur m(∅) appliquée à la gouvernance
du frame de discernement.

**CLAIM hors-Θ** : un CLAIM sur une hypothèse H absente de la version courante de Θ
est REJECTED au Niveau 2 de la cascade de validation, cause `HYPOTHESIS_OUT_OF_FRAME`.
L'agent `chain_id` et l'hypothèse H sont reportés à C-07. L'opérateur décide :
étendre Θ ou traiter l'agent comme défaillant.

**Règle de rétrocompatibilité lors d'un changement Θ_v(n) → Θ_v(n+1)** :

- H_k présente dans Θ_v(n+1) : les CLAIMs ACTIVE sur H_k restent ACTIVE. L'orchestrateur
  met à jour `Θ.version` dans son registre interne — pas dans le CLAIM (INV-01 tenu).

- H_k absente de Θ_v(n+1) (hypothèse retirée) : les CLAIMs ACTIVE sur H_k transitent
  vers PENDING_REVIEW avec cause `THETA_VERSION_MISMATCH`. L'opérateur est notifié
  via C-07 et décide : VOID définitif ou maintien ACTIVE jusqu'à expiration naturelle.

- **Pas de transition VOID automatique** : retirer une hypothèse de Θ ne doit pas
  invalider automatiquement des CLAIMs en cours de contribution à l'EPISTEMIC_STATE.
  L'opérateur conserve la décision finale — c'est la règle cardinale sur m(∅)
  appliquée à la couche de gouvernance de Θ.

**Question ouverte QO-BR-01** : cette règle est-elle cohérente sous forte charge
lors d'un changement de Θ impliquant de nombreux CLAIMs ACTIVE simultanément ?
Une limite `max_pending_review_per_theta_change` est-elle nécessaire ?

**Convergence externe** : absence de convergence sur la gouvernance opérationnelle
de Θ. OWL versioning et schema versioning DB adressent partiellement le problème
sans sémantique du Frame of Discernment. La propagation entre frames DS est
documentée dans la littérature depuis 1993 (Springer) mais sans protocole de
gouvernance opérationnelle. Cette proposition est la première réponse concrète
avec règle de rétrocompatibilité — contribution prospective documentable en CCP-2.

---

## Questions ouvertes résiduelles

**QO-BR-01** — Règle de rétrocompatibilité §8 sous forte charge. Si un changement
de Θ invalide de nombreux CLAIMs ACTIVE simultanément, le volume de transitions
PENDING_REVIEW peut dépasser la capacité de traitement humain. Une limite
`max_pending_review_per_theta_change` est-elle nécessaire, et si oui, qui
décide du comportement au-delà du seuil ?

**QO-BR-02** — Calibration de `validation_level1_timeout_ms`. La valeur par défaut
de 50 ms est raisonnée mais non vérifiée sur architectures embarquées réelles
(RTOS, VxWorks). Une référence à des benchmarks de lookup registre embarqué
renforcerait l'argument SWaP de CCP-4.

**QO-BR-03** — Sortie de quarantaine sous reconnexion massive. Si N agents
simultanément perdent puis retrouvent la connexion, la politique "sortie de
quarantaine uniquement par décision humaine" peut créer un goulot opérationnel
non tenable. Une procédure de sortie de quarantaine par lot devrait-elle être
définie, et sous quelles conditions de garde ?

---

## Synthèse — tableau de décision consolidé

| § | Composant | Spec v1.1 | Proposition v0.3 | Verdict corpus externe | NMT | Destination |
|---|---|---|---|---|---|---|
| 1 | Cycle de vie 7 statuts | Rejet B.1 seulement | 7 statuts · SUPERSEDED/VOID originaux | Convergence partielle · SUPERSEDED/VOID inédits | 2 | Spec B §B.3 |
| 2 | Cascade validation 3 niveaux | Liste plate | Niveaux 0/1/2 + timeout charge dégradée | Convergence forte principe · Formalisation originale | 2 | B.1 sous-section · arg. CCP-4 |
| 3 | Freshness par illocution | `Δt_valid` uniforme | Décroissance différenciée + `assume_max_validity_s` | Convergence partielle · Innovation illocutoire | 3 (OBSERVE : 2) | §A.3 enrichissement |
| 4 | Stale storm | AM-03 NMT 4-5 | 3 paramètres · fermeture AM-03 | Convergence forte problème | 3 | Spec B §B.4 |
| 5 | Graphe dépendances | Absent | Index léger déclaré uniquement | Convergence forte structure · Delta : déclaré vs. inféré | 3 | research/post_submission |
| 6 | Protocole nouvel agent | Absent (stateless) | UNREGISTERED→REGISTERED→QUARANTINED + auditabilité | Convergence partielle · Solution TBM inédite | 3 | Spec B §B.5 |
| 7 | Log certifiable | TP-02 non spécifié | 8 champs + codes de cause · `trust_discount_applied` | **Convergence forte · 3 domaines indépendants** | 2 | LOG_certifiable.md |
| 8 | Gouvernance Θ | Θ statique | Θ versionné + règle rétrocompat. | **Absence convergence = contribution prospective** | 3 (`HYPOTHESIS_OUT_OF_FRAME` : 2) | B.1 cas 6 · Spec B §B.6 |

---

## Plan d'intégration Sprint

### Intégrations immédiates (NMT 2 — avant J19)

**Section B.1** :
- Ajouter l'ordre de cascade §2 comme sous-section "Ordre d'évaluation" (Niveaux 0/1/2)
- Ajouter `HYPOTHESIS_OUT_OF_FRAME` comme 6e cas de malformation (§8 partiel)
- Ajouter `assume_max_validity_s` comme note de configuration orchestrateur (§3 ASSUME)
- Ajouter `validation_level1_timeout_ms` avec comportement file de réessai (§2)

**Spec B §B.3** : cycle de vie 7 statuts complet (§1)

**Spec B §B.4** : paramètres stale storm + fermeture formelle AM-03 (§4)

**Spec B §B.5** : protocole nouvel agent + champ `trust_discount_applied` (§6)

**LOG_certifiable.md** : note de convergence externe (§7) + tableau codes de cause complet

### Archivage post-J19

**research/post_submission_ideas.md** :
- §3 freshness différenciée INFER/DEDUCE (NMT 3)
- §5 graphe de dépendances inter-CLAIMs (NMT 3)
- §8 versioning Θ complet avec `Θ.version` obligatoire (NMT 3)
- QO-BR-01/02/03 comme questions de recherche ouvertes

---

*CLAIM complétude consolidée v0.3 — 21 mai 2026*
*Statut : PENDING — à valider par Andrei avant intégration dans CLAIM_specification.md*
*Consolidation de : v0.1 instance A (ANAMNESE) + v0.2 instance B (deep search + REV12B)*
*Convergence externe : validée §7 (3 domaines) · corpus layer_*.md §3/§4/§5*
*Manquements REV12B : tous intégrés — M1 (Élevée) · M2 (Élevée) · M3/M4/M5 (Moyenne)*
