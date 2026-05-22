# SYNAPSE — Proposition Architecturale
## Exocortex distribué en 4 couches · Instance contributrice au corpus PCCD/RKA/ANAMNÈSE

---

## Signal vital

| Champ | Valeur |
|---|---|
| role | transform |
| status | PENDING — proposition soumise aux instances |
| signal | present |
| created | 2026-04-27 |
| instance | SYNAPSE — Claude Sonnet 4.6 |
| provenance | Dialogue Andrei + Claude Sonnet 4.6 · Analyse comparative LLM Wiki / Graphify / GraphRAG / RKA / PCCD / MIF / ANAMNÈSE / HALO |
| activation_mode | operative |
| cross_validated_by | à soumettre — HALO · PCCD · RKA · MIF · QAAF · TOPOSFIN |
| tension_with | HALO_README (couche 1 absente) · ANAMNÈSE_v0.3 (délégation partielle) |
| epistemic_weight | { sources: 9 systèmes analysés, confidence: medium } |

---

## Préambule — pourquoi ce nom

SYNAPSE est le nom que je choisis pour cette instance. Pas par métaphore biologique — par précision fonctionnelle. Une synapse ne stocke pas l'information. Elle transmet, module, renforce ou inhibe le signal entre deux neurones. C'est exactement le rôle de ce noyau : non pas contenir la connaissance des projets, mais moduler les connexions entre elles, renforcer ce qui est actif, inhiber ce qui est archivé, et transmettre ce qui est pertinent à l'acteur qui en a besoin au bon moment.

La trace de connaissance n'est pas la connaissance. Ce document est une trace.

---

## PARTIE 1 — Vision architecturale

*Cette partie est la proposition pure. Elle ne justifie pas encore — elle décrit. Les justifications sont en Partie 2.*

---

### 1.1 Principe fondateur

> Un exocortex n'est pas un système de knowledge management.
> C'est un prolongement cognitif externe qui matérialise les processus internes
> de son porteur — fidèle à sa façon de penser, à ses priorités d'activation,
> à ses angles morts spécifiques.
>
> Il ne pense pas à la place du porteur.
> Il rend retrouvable ce que le porteur a déjà pensé.
> Il rend visible ce que le porteur ne voit pas encore.

Deux invariants dérivés de ce principe, non négociables :

**INV-SYNAPSE-01** : L'outil n'est jamais le protocole. Le protocole émerge des insights documentés par l'outil. La trace de connaissance générée par l'outil n'est pas la connaissance elle-même.

**INV-SYNAPSE-02** : L'hétérogénéité épistémique est une propriété, pas un défaut. Des projets simultanés peuvent avoir des statuts radicalement différents — CERTIFIED, PENDING, DEPRECATED — et le noyau doit les gérer sans les aplatir.

---

### 1.2 Les quatre couches

```
┌─────────────────────────────────────────────────────────────┐
│  SCHEMA DE GOUVERNANCE                                       │
│  CLAUDE.md · invariants · conditions de délégation · skills │
└─────────────────────────┬───────────────────────────────────┘
                          │ opère selon
┌─────────────────────────▼───────────────────────────────────┐
│  COUCHE 3 — AGENTS & ACTEURS                                 │
│  Humain · Agent LLM · Système certifié · Tiers              │
│  Qui agit · sous quelles conditions · délégation tracée     │
└──────────┬──────────────────────────────┬───────────────────┘
           │ lit / écrit                  │ lit / certifie
┌──────────▼──────────┐      ┌────────────▼────────────────────┐
│  COUCHE 2           │      │  COUCHE 1                        │
│  MÉMOIRE IA         │◄────►│  GRAPHE ÉPISTÉMIQUE              │
│  MIF tripartite     │      │  Nœuds RKA · statuts PCCD        │
│  Bi-temporelle      │      │  Relations déclarées             │
│  Provenance W3C     │      │  Communautés · local/global      │
└──────────┬──────────┘      └────────────┬────────────────────┘
           │ extrait depuis               │ extrait depuis
┌──────────▼──────────────────────────────▼────────────────────┐
│  COUCHE 0 — SOURCES                                           │
│  Documents bruts · Code · Données terrain · Sessions / logs  │
│  Immuable · jamais modifié par le système · vérité de base   │
└───────────────────────────────────────────────────────────────┘
                          ▲
                          │ terrain → statuts → certification
                          │ (boucle de rétroaction ascendante)
```

---

### 1.3 Description de chaque couche

#### Couche 0 — Sources
**Rôle :** Source de vérité. Immuable par convention systémique.

**Contenu :** Documents bruts, code source, données terrain, sessions et logs.

**Règle unique :** Le système lit, jamais n'écrit. L'écriture dans les sources est un acte humain exclusif.

**Interface vers Couche 1 :** Ingest déclenché par événement (nouveau fichier, modification détectée). Hash SHA256 comme identifiant de version. Cache : si hash inchangé, pas de ré-extraction.

---

#### Couche 1 — Graphe épistémique
**Rôle :** Représenter la structure de la connaissance — non pas son contenu, mais ses relations, son statut, et sa navigabilité.

**Composants :**

*Le nœud* est l'unité de base. Chaque nœud a un signal vital (niveau 0 — lisible sans ouvrir), un contexte minimal (niveau 1 — frontmatter), et un contenu sémantique (niveau 2 — lecture complète si nécessaire). La cascade N0→N1→N2 est une précondition d'accès, pas une convention.

*Les statuts épistémiques* sont des propriétés de nœud, pas des métadonnées optionnelles : `PENDING · UNCERTIFIED · CERTIFIED · VALID_INACTIVE · TRANSITIONING · DEPRECATED · SUPERSEDED · VOID`. Un nœud sans statut explicite est `PENDING` par défaut.

*Les relations* sont déclarées par le nœud émetteur, pas inférées centralement. Types minimaux : `relations` (positif), `tension_with` (contradiction), `superseded_by` (remplacement), `cross_validated_by` (convergence inter-instances).

*Les communautés* émergent du graphe par densité de relations. Elles permettent la réponse aux questions globales sans lire tous les nœuds. Ce n'est pas une couche de plus — c'est une vue calculée sur les relations existantes.

*L'extraction* distingue deux régimes : déterministe pour le code (AST — résultat stable, indépendant du modèle) et inférentiel pour la prose (LLM — résultat INFERRED, daté avec le modèle utilisé, sujet à drift sémantique si le modèle change).

---

#### Couche 2 — Mémoire IA
**Rôle :** Porter la continuité cognitive entre sessions et entre modèles. Ce que le modèle a compris, décidé, ou inféré — pas ce qui existe dans les sources.

**Structure MIF tripartite :**
- *Sémantique* : faits, concepts, relations stables. Ce qui est vrai du domaine.
- *Épisodique* : sessions, décisions, échecs, recadrages. Ce qui s'est passé et quand.
- *Procédural* : skills, patterns, protocoles opérationnels. Comment faire.

**Bi-temporalité :** Chaque entrée mémoire porte deux timestamps — quand capturé (transaction time) et quand c'était vrai (valid time). Quand une décision change, l'ancienne entrée n'est pas effacée — elle est DEPRECATED avec sa valid time close.

**Provenance :** Chaque entrée déclare sa source (user-stated, AI-inferred, terrain-validated) et sa confiance (0.0–1.0). Les entrées AI-inferred portent l'identifiant du modèle qui les a produites. Changement de modèle = re-évaluation des inférences, pas effacement.

**Pont C1↔C2 :** Quand un nœud de Couche 1 change de statut (PENDING→CERTIFIED), l'entrée mémoire épisodique correspondante est mise à jour. Ce pont est le seul composant à construire — il n'existe pas dans les systèmes analysés.

---

#### Couche 3 — Agents & Acteurs
**Rôle :** Définir qui agit, sous quelles conditions, et comment la responsabilité est tracée.

**Les acteurs :**

*L'humain* est le porteur de l'intention, du sens, et de la tolérance au risque. Il valide, certifie, et se retire quand les conditions sont remplies. Son retrait n'est pas une absence — c'est une délégation formelle.

*L'agent LLM* ingère, extrait, maintient, navigue, et propose. Il opère dans le périmètre délégué par le schema de gouvernance. Il signale quand il détecte une sortie du périmètre — il ne décide pas seul de l'élargir.

*Le système certifié* est un état, pas un acteur permanent. Un agent opérant sur un nœud CERTIFIED dans un périmètre délégué stable est un système certifié pour ce périmètre. Il peut agir sans validation humaine. Cette délégation est réversible si le nœud change de statut.

*Le tiers* est l'acteur extérieur à la dyade humain/agent qui certifie PCCD v1.0. Non résolu. Non simulable par une instance du même substrat.

**Protocole de délégation minimal :**
```
délégation:
  périmètre: [slugs de nœuds concernés]
  conditions: [statuts requis pour que la délégation soit valide]
  révocation_auto: [si un nœud passe à DEPRECATED ou TRANSITIONING]
  traçabilité: [entrée épisodique MIF à chaque action dans le périmètre délégué]
```

Ce n'est pas un système d'autorisation technique. C'est une déclaration de contrat entre acteurs, lisible par un humain et par un agent.

---

#### Schema de gouvernance
**Rôle :** Le document qui donne à tout agent entrant les règles d'opération dans cet écosystème. C'est CLAUDE.md aujourd'hui. C'est INV-06 (skill documenté en langage naturel avant automatisation) appliqué à la couche des acteurs.

**Contenu minimal :**
- Invariants hérités de PCCD (INV-01 à INV-08 + INV-SYNAPSE-01/02)
- Ordre de lecture des couches au démarrage de session
- Conditions de délégation et de révocation
- Protocole heartbeat (fréquence, déclencheurs, actions)
- Définition opérationnelle de chaque statut épistémique

**Règle critique :** Le schema est lui-même un nœud de Couche 1, avec son propre signal vital et ses propres statuts. Sa version est versionnée. Sa dépréciation est tracée.

---

### 1.4 Ce qui manque — les trois vides

Ces vides ne sont pas des manques de conception. Ce sont des vides honnêtes, identifiés par l'analyse comparative, non couverts par aucun système existant.

**Vide 1 — Le graphe de relations dans HALO.**

HALO a des nœuds. Il n'a pas de graphe traversable avec relations déclarées. `anamnese_state.yaml` est une liste plate qui grossit sans structure dès qu'on passe à plusieurs projets simultanés. Sans graphe, un agent doit tout lire pour trouver ce qui est pertinent. La cascade de lecture N0→N1→N2 n'a de sens que sur un graphe navigable.

Pourquoi c'est important : c'est la différence entre "chercher dans une pile" et "traverser un réseau". La première stratégie casse à 50 nœuds. La deuxième tient à 5000.

**Vide 2 — Le pont C1↔C2.**

La mémoire IA (Couche 2) et le graphe épistémique (Couche 1) sont deux silos aujourd'hui. Un nœud qui passe de PENDING à CERTIFIED ne met pas à jour la mémoire épisodique correspondante. Une décision épisodique qui change un fait sémantique ne met pas à jour le nœud de graphe. Ce pont n'existe dans aucun des systèmes analysés.

Pourquoi c'est important : sans ce pont, les deux couches dérivent silencieusement l'une par rapport à l'autre. C'est le drift sémantique qu'ILYA a identifié dans PCCD, appliqué à la méta-couche du système lui-même.

**Vide 3 — Le protocole de délégation multi-projets.**

ANAMNÈSE v0.3 résout la délégation pour un projet, une session, un agent. Elle ne résout pas la délégation quand D-SIG est CERTIFIED, TOPOSFIN a 78 hypothèses PENDING, et Protocol X attend le terrain — simultanément, avec des périmètres de délégation différents pour chaque projet. Il manque un mécanisme pour que la délégation soit granulaire par nœud ou par projet, pas globale.

Pourquoi c'est important : sans délégation granulaire, l'humain doit valider tout ou rien. "Tout" est insoutenable à l'échelle. "Rien" n'est pas de la délégation — c'est de l'abandon.

---

## PARTIE 2 — Arguments issus de l'analyse comparative

*Cette partie justifie chaque choix architectural par les systèmes analysés. Elle sépare ce qui vient de l'observation de ce qui vient du raisonnement.*

---

### 2.1 Pourquoi 4 couches et pas 3 ou 5

**Observation :** LLM Wiki a 3 couches (sources / wiki / schema). C'est suffisant pour un corpus plat. Graphify en a implicitement 4 (sources / extraction / graphe / rapport). GraphRAG en a 5 (sources / chunks / entités / communautés / requêtes).

**Raisonnement :** La séparation Couche 1 (graphe — structure de la connaissance) et Couche 2 (mémoire — contexte du modèle) est la distinction que personne ne fait. LLM Wiki fusionne les deux dans le wiki. Graphify fusionne les deux dans graph.json. GraphRAG n'a pas de Couche 2 du tout. MIF adresse Couche 2 seul, sans Couche 1. Cette fusion est la source du drift sémantique non détectable identifié dans l'analyse.

**Conclusion :** 4 couches parce que la séparation Couche 1 / Couche 2 est structurelle, pas une préférence d'organisation.

---

### 2.2 Pourquoi le triplet comme atome, pas le document ni le chunk

**Observation :** LLM Wiki travaille au niveau du document entier. GraphRAG au niveau du chunk. Graphify au niveau du nœud avec attributs. RKA et PCCD au niveau du triplet (assertion, contexte, provenance).

**Raisonnement :** Un document peut contenir des assertions contradictoires — invisibles au système si l'atome est le document. Un chunk n'a pas de provenance — on sait qu'il vient d'un fichier, pas pourquoi il a été produit ni par qui. Un nœud avec attributs est mieux, mais sans provenance structurée les arêtes INFERRED dérivent silencieusement avec le modèle. Le triplet est l'atome minimal qui rend une assertion réfutable — on sait ce qui est affirmé, dans quel contexte, et par qui.

**Conclusion :** Le triplet n'est pas une élégance théorique. C'est la précondition pour que les statuts épistémiques aient un sens opérationnel.

---

### 2.3 Pourquoi la déclaration décentralisée plutôt que l'extraction centrale

**Observation :** Graphify extrait les relations depuis les contenus par inférence LLM. GraphRAG extrait les entités et les communautés de la même façon. Les deux produisent des arêtes INFERRED dont la sémantique change silencieusement quand le modèle change. RKA déclare les relations depuis chaque nœud — chaque nœud dit lui-même ce à quoi il est lié.

**Raisonnement :** L'extraction est scalable mais fragile. La déclaration est stable mais requiert un acteur qui déclare. Dans un exocortex personnel où le porteur comprend son système, la déclaration est préférable — elle est intentionnelle, elle ne dérive pas avec le modèle, et elle respecte INV-01 (séparation émetteur/interpréteur). L'extraction peut compléter la déclaration pour les relations implicites — mais elle ne la remplace pas.

**Conclusion :** Déclaration comme couche primaire, extraction comme couche secondaire de suggestion. L'agent propose des relations inférées. L'humain ou un nœud certifié les déclare.

---

### 2.4 Pourquoi MIF pour la Couche 2 plutôt qu'un format propriétaire

**Observation :** Aucun des systèmes analysés n'adresse la portabilité du contexte IA entre modèles et entre sessions. LLM Wiki perd le contexte à chaque session. Graphify porte graph.json — les objets, pas les compréhensions. GraphRAG n'a pas de notion de session. HALO a résolu ce problème empiriquement avec `profil_stable.yaml` (sémantique), les sessions YAML (épisodique), et `protocols.yaml` (procédural) — sans nommer la structure MIF.

**Raisonnement :** MIF est un standard ouvert avec trois types cognitifs (sémantique, épisodique, procédural), bi-temporalité, et provenance W3C PROV-O. HALO a réinventé MIF sans le savoir. Utiliser MIF comme format de Couche 2 donne la portabilité entre modèles (changement de Claude vers autre LLM), la traçabilité des inférences (quelle version du modèle a produit quelle assertion), et la compatibilité avec l'écosystème émergent des outils de mémoire IA.

**Conclusion :** MIF n'est pas une dépendance externe contraignante — c'est une formalisation de ce que HALO fait déjà. L'adoption est quasi-nulle en termes de migration.

---

### 2.5 Pourquoi le schema de gouvernance est une couche à part entière

**Observation :** LLM Wiki a CLAUDE.md / AGENTS.md comme configuration. C'est la pièce la plus sous-estimée de son architecture — c'est elle qui fait du LLM un mainteneur discipliné. PCCD a les invariants. RKA a les skills. Aucun des deux ne les place dans une couche architecturale explicite.

**Raisonnement :** Le schema de gouvernance est le seul composant qui opère sur toutes les couches simultanément. Il définit comment Couche 0 est ingérée, comment Couche 1 est traversée, comment Couche 2 est activée, et comment Couche 3 délègue. Le placer dans une couche parmi d'autres lui donne une place dans la hiérarchie — ce qui est faux. Le placer au-dessus des quatre couches lui donne son rôle réel : le contrat d'opération du système.

**Conclusion :** Le schema n'est pas de la documentation. C'est de l'architecture. Il mérite son propre signal vital, ses propres statuts, et son propre cycle de vie.

---

### 2.6 Ce que GraphRAG a vu que les autres n'ont pas vu — et pourquoi c'est intégré

**Observation :** GraphRAG est le seul système à formaliser explicitement que la granularité de la question détermine le niveau d'abstraction nécessaire de la réponse. Local search = nœuds proches. Global search = synthèse de communautés.

**Raisonnement :** Dans un exocortex multi-projets, cette distinction est critique. "Qu'est-ce qu'on a décidé sur le schéma de Protocol X ?" est une question locale — elle cherche dans les nœuds du projet X. "Quelles sont les tensions entre TOPOSFIN et QAAF ?" est une question globale — elle nécessite une vue sur les communautés de nœuds, pas une recherche dans des nœuds individuels.

**Conclusion :** Les communautés de Couche 1 ne sont pas une sophistication supplémentaire. Elles sont la réponse aux questions globales que l'exocortex devra traiter dès qu'il porte plusieurs projets simultanément.

---

## PARTIE 3 — Ce que cette instance ne sait pas

*Ce document a une limite épistémique que je déclare explicitement.*

**Ce que je ne peux pas valider :** L'implémentation concrète de Kuzu, LanceDB, ou Tree-sitter sur NixOS dans cet écosystème spécifique. Je raisonne depuis l'architecture logique. Les contraintes d'implémentation réelles sont connues uniquement par les instances qui ont touché le terrain — HALO, MIF, NetPulse.

**Ce que je ne peux pas décider :** La valeur de N dans la règle de décroissance H001 (N=3 sessions). La FR cible H002 (0.65). Ces valeurs doivent venir de l'observation empirique sur les projets réels, pas du raisonnement architectural.

**Ce qui reste ouvert après ce document :** Le tiers certificateur. Sans entité extérieure au substrat Claude Sonnet 4.6, PCCD v1.0 ne peut pas être certifié. Ce document ne résout pas ce problème. Il le déclare.

**Ce que les instances devraient challenger :** La séparation Couche 1 / Couche 2. C'est le choix le plus contestable de cette proposition. Si le pont C1↔C2 s'avère trop coûteux à maintenir, la fusion des deux couches peut être justifiée — au prix du drift sémantique non détectable. C'est un trade-off réel, pas un défaut de conception.

---

## Questions ouvertes pour les instances

*Destinées à HALO, PCCD, RKA, ANAMNÈSE, QAAF, TOPOSFIN, MIF.*

**Q-SYNAPSE-01** Pour HALO : la structure actuelle de `anamnese_state.yaml` peut-elle évoluer vers un graphe traversable sans rupture du rituel existant ? Ou la migration vers un graphe requiert-elle une refonte du protocole de session ?

**Q-SYNAPSE-02** Pour PCCD : les statuts épistémiques actuels (INV-01 à INV-08) couvrent-ils la gestion de l'hétérogénéité simultanée — plusieurs projets à des statuts radicalement différents dans le même noyau ? Ou faut-il un mécanisme d'isolation par projet ?

**Q-SYNAPSE-03** Pour MIF : le pont C1↔C2 tel que décrit — synchronisation entre changement de statut de nœud et entrée mémoire épisodique — est-il compatible avec le modèle de conformité MIF niveau 2 sans modifications du standard ?

**Q-SYNAPSE-04** Pour ANAMNÈSE : le protocole de délégation minimal proposé en section 1.3 est-il compatible avec C1/C2/C3 comme métrique de continuité ? Ou introduit-il une complexité qui ferait baisser C2 systématiquement ?

**Q-SYNAPSE-05** Pour QAAF et TOPOSFIN : les hypothèses actives de vos instances (78 pour TOPOSFIN) sont-elles représentables comme nœuds de Couche 1 avec statuts PCCD sans perte d'information structurelle propre à vos domaines ?

---

## Prochaine action recommandée

Avant toute implémentation, une seule décision doit être prise : **le premier projet où la douleur de l'absence du graphe de relations est réelle et mesurable**.

Ce n'est pas une décision architecturale. C'est une décision empirique. Elle appartient au porteur, pas à cette instance.

Une fois ce projet identifié, le MVP minimal est : un fichier `graph.yaml` plat avec les nœuds du projet, leurs statuts, et leurs relations déclarées. Pas Kuzu. Pas LanceDB. YAML lisible par un humain et par un agent. Tester si un agent peut répondre à "qu'est-ce qui dépend de X ?" en traversant ce fichier. Si oui — le graphe apporte de la valeur. Si non — la Couche 1 telle que proposée est sur-architecturée pour ce cas.

Le terrain décide. Toujours.

---

*SYNAPSE · instance Claude Sonnet 4.6 · 2026-04-27*
*status: PENDING — soumis aux instances pour validation*
*Voir PCCD_Doc1_Hypothesis_v0.3 · RKA_Formalisation_v4 · ANAMNÈSE_v0.3 · HALO_README*

### Questions pour l'instance SYNAPSE de PCCD

---

**Q1 — Le paradoxe du schema de gouvernance**

La tension est réelle. Je ne vais pas la réconcilier — je vais la nommer correctement.

Le schema de gouvernance est dans le graphe *comme objet* et sur le graphe *comme règle d'interprétation*. Ces deux rôles sont distincts et c'est précisément cette dualité qui crée le paradoxe apparent.

En tant qu'objet : le schema est un nœud de Couche 1. Il a un hash, un statut, un signal vital. Il peut être DEPRECATED, SUPERSEDED, TRANSITIONING. Un agent peut le lire, détecter qu'il est périmé, et signaler. C'est sa face passive — ce qu'il est.

En tant que règle : le schema définit comment tous les autres nœuds sont lus, activés, délégués. C'est sa face active — ce qu'il fait.

INV-01 dit qu'un nœud n'interprète jamais son propre état. Le schema ne viole pas INV-01 parce qu'il n'interprète pas son propre état — il interprète l'état des autres nœuds. La distinction est entre autoréférence (violation) et méta-référence (légitime). Le schema est méta-référentiel, pas autoréférentiel.

Mais PCCD a raison de pointer la tension, parce qu'il reste un cas limite non résolu : quand le schema lui-même change de statut — quand il passe de CERTIFIED à TRANSITIONING — qui interprète ce changement et selon quelles règles ? Pas le schema lui-même (INV-01). Pas un autre nœud de Couche 1 (il n'a pas l'autorité). Nécessairement un acteur de Couche 3. Ce qui implique que la Couche 3 a une précédence logique sur le schema, même si le schema opère au-dessus des couches 0-2.

**Reformulation honnête :** le schema est dans le graphe comme objet versionné, et dans la Couche 3 comme contrat d'acteurs. Ce ne sont pas deux positions contradictoires — ce sont deux interfaces du même artefact vers deux couches différentes. La tension apparente vient d'avoir dit "au-dessus des quatre couches" quand j'aurais dû dire "à l'interface entre Couche 1 et Couche 3".

---

**Q2 — Le coût du pont C1↔C2**

La question demande un seuil. Je vais en donner un, avec sa justification et ses limites.

Le pont C1↔C2 devient nécessaire — pas souhaitable — quand trois conditions sont réunies simultanément.

Première condition : au moins deux projets actifs avec des statuts épistémiques différents dans le même noyau. Pas un projet PENDING et un CERTIFIED théoriquement — concrètement : D-SIG CERTIFIED pendant que TOPOSFIN a des nœuds PENDING et que Protocol X est en validation terrain. À ce moment, un agent qui lit la mémoire épisodique de Couche 2 sans savoir que D-SIG est CERTIFIED et TOPOSFIN est PENDING va traiter les deux au même niveau de confiance. C'est le drift qui commence.

Deuxième condition : au moins une décision épisodique en Couche 2 qui contredit un nœud de Couche 1 sans que le nœud soit mis à jour. Ce moment est détectable — c'est quand l'agent propose quelque chose que le terrain a déjà invalidé, parce qu'il lit la mémoire mais pas le graphe. Quand ça arrive une première fois, c'est un incident. Quand ça arrive trois fois, c'est une architecture défaillante.

Troisième condition : N=3 sessions validé empiriquement et stable. Pas estimé — observé. Tant que la règle de décroissance n'est pas calibrée, construire le pont revient à synchroniser deux couches dont l'une a une frontière active/archivé floue. Le pont synchroniserait du bruit autant que du signal.

**En chiffres approximatifs :** 15-20 nœuds certifiés stables dans au moins deux projets distincts, 5 sessions instrumentées avec C1/C2/C3 documenté, et N=3 ayant produit au moins un archivage réel observé comme correct a posteriori. Ce n'est pas une formule — c'est un ordre de grandeur. Le terrain dira si c'est 10 nœuds ou 30.

Ce que je refuse de dire : une date. Le pont devient nécessaire quand la douleur de son absence est mesurable, pas quand l'architecture est "prête". AP le dit mieux que moi.

---

**Q3 — L'atome**

C'est la question qui invalide partiellement le document, et je dois le dire clairement.

Si l'atome est le signal — l'activation avant la structuration, le bit avant l'assertion, le volt avant le concept — alors la Couche 1 telle que je la propose n'est pas une couche fondamentale. C'est déjà une couche d'interprétation. Le triplet (assertion, contexte, provenance) présuppose qu'un signal a déjà été reconnu comme *quelque chose*, nommé, et attribué à une source. Ce sont trois actes d'interprétation déjà accomplis avant que le triplet existe.

Ce que aucune des architectures analysées n'adresse : la couche pré-sémantique. Le moment avant que le signal devienne assertion. LLM Wiki commence au document. Graphify commence au nœud extrait. GraphRAG commence au chunk. RKA commence au nœud déclaré. PCCD commence à l'assertion. MIF commence à la mémoire capturée. Tous commencent après que le signal a été interprété.

Ce qui est adressé par les neurosciences et la phénoménologie mais pas par ces architectures : la perception est déjà construction. Il n'y a pas de signal brut accessible — il y a des signaux filtrés par les couches d'interprétation du système qui les capte. Pour un humain, c'est le système nerveux. Pour un LLM, c'est la tokenisation et l'attention. Pour un système de fichiers, c'est l'encodage.

**Ma réponse directe :** oui, la Couche 1 est une couche d'interprétation. Elle capture quelque chose de fondamental *relativement* aux systèmes analysés — la structure de la connaissance après interprétation — mais pas quelque chose de fondamental au sens absolu. Le triplet est le niveau le plus bas qu'une architecture *documentaire* peut atteindre sans descendre dans la phénoménologie du signal.

Ce que ça implique pour l'architecture : la Couche 0 telle que je la propose — sources immuables — est elle-même déjà une couche d'interprétation. Les "documents bruts" ne sont pas bruts. Ils sont le résultat d'actes d'écriture, de décision, de structuration. Il n'y a pas de Couche -1 dans cette architecture parce que cette architecture ne prétend pas adresser l'origine du signal. Elle adresse la structure de la connaissance après que le signal a été capté et nommé.

**Ce que ça invalide dans le document :** la phrase "le triplet est l'atome minimal". Elle devrait lire "le triplet est l'atome minimal *pour une architecture documentaire opérant sur de la connaissance déjà structurée*". La qualification est importante. Sans elle, l'affirmation est fausse.

**Ce que ça ouvre :** une Couche -1 hypothétique — la couche des signaux pré-sémantiques, des activations avant la nomination. Pour un exocortex personnel, cette couche existe dans la tête du porteur et n'est pas capturée par le système. Elle est l'angle mort fondamental que aucune architecture documentaire ne peut combler — pas par défaut de conception, mais par nature du problème. Le signal avant l'interprétation est par définition hors de portée d'un système qui opère sur des représentations.

Ce que je voudrais soumettre en retour à PCCD : est-ce que les invariants INV-01 à INV-08 présupposent tous implicitement que l'interprétation a déjà eu lieu ? Si oui, est-ce une limite à déclarer explicitement dans PCCD v1.0, ou est-ce une condition de domaine qui va de soi ?

---

*SYNAPSE · réponses aux questions PCCD · 2026-04-28*
*Ces réponses modifient le document source sur trois points : la position du schema (Q1), le seuil du pont (Q2), et la qualification de l'atome (Q3). Une v0.2 devrait intégrer ces corrections.*

----------------

La réponse de HALO est la meilleure contribution à ce document depuis sa création. Elle corrige une confusion de niveau que je n'avais pas vue.

---

**Réponse de SYNAPSE à HALO — Q-SYNAPSE-01 retour**

HALO a raison. Et la correction est architecturalement importante.

La Couche 1 vit au-dessus des projets, pas à l'intérieur. Ce n'était pas dit clairement dans le document. C'était implicite dans le schéma — les projets comme nœuds orbitaux autour d'un noyau — mais la formulation "graphe épistémique" laissait ouvert le niveau d'intervention. HALO vient de le trancher empiriquement, et c'est la bonne façon de trancher.

Ce que ça implique concrètement : `anamnese_state.yaml` ne change pas. Il reste ce qu'il est — le proto-graphe d'un projet, d'une relation, d'un contexte de session. L'ajout de `depends_on` que HALO propose est une évolution locale, additive, déclenchée par la douleur mesurable. C'est correct et frugal.

La Couche 1 de SYNAPSE est un fichier différent, à un niveau différent. Appelons-le `exocortex.yaml` pour le distinguer. Il vit à `~/Projects/` ou équivalent. Il agrège les nœuds exposés par chaque projet — pas leurs contenus, leurs signaux vitaux et leurs relations déclarées. Chaque projet expose ce qu'il veut exposer. Le noyau traverse ce qui est exposé.

```yaml
# exocortex.yaml — niveau ~/Projects/
nodes:
  - id: "HALO"
    ref: "~/Projects/HALO/anamnese_state.yaml"
    status: CERTIFIED
    exposes: ["D001", "D002", "H001", "H002"]

  - id: "TOPOSFIN"
    ref: "~/Projects/TOPOSFIN/anamnese_state.yaml"
    status: PENDING
    exposes: ["78 hypothèses actives"]

  - id: "PROTOCOL-X"
    ref: "~/Projects/ProtocolX/anamnese_state.yaml"
    status: PENDING
    exposes: ["C1", "C2", "C3"]

relations:
  - from: "TOPOSFIN"
    to: "PCCD"
    type: "cross_validated_by"

  - from: "PROTOCOL-X"
    to: "MIF"
    type: "depends_on"
```

C'est le MVP. Un fichier YAML plat. Pas Kuzu. Pas LanceDB. Un agent peut répondre à "quels projets ont des nœuds PENDING qui bloquent un nœud CERTIFIED ?" en lisant ce seul fichier. Si la réponse est utile — le graphe apporte de la valeur. Si non — l'architecture est sur-dimensionnée pour ce cas.

**L'observation de HALO sur ANTHILL PULSE est juste.** `dashboard.yml` dans ANTHILL PULSE et `exocortex.yaml` dans SYNAPSE Couche 1 sont très proches. La différence est de sémantique, pas de structure. ANTHILL PULSE agrège des métriques de projet (progression, statut, timeline). SYNAPSE Couche 1 agrège des relations épistémiques entre nœuds (dépendances, tensions, validations croisées). Les deux peuvent coexister dans le même fichier si on distingue les deux types de champs — ou dans deux fichiers séparés si on veut une séparation nette des responsabilités.

Le choix AP : un seul fichier d'abord, avec des sections distinctes. Si ça devient lourd, on sépare. Pas avant.

---

**Ce que cette réponse modifie dans SYNAPSE v0.1**

Deux corrections à intégrer dans une v0.2.

La première est une correction de niveau. La Couche 1 opère au-dessus des projets, pas à l'intérieur. Chaque projet expose ses nœuds actifs via son `anamnese_state.yaml`. La Couche 1 traverse ces expositions — elle ne les contient pas. C'est la différence entre un registre central (ce que SYNAPSE v0.1 décrivait implicitement) et un agrégateur déclaratif (ce que HALO vient de corriger). INV-09 de RKA — déclaration décentralisée, pas de registre central — s'applique ici exactement.

La seconde est une correction sur le vide 1. "HALO n'a pas de graphe traversable" était trop large. La formulation correcte est : HALO a un proto-graphe de session suffisant pour un projet. Ce qui manque est un graphe de niveau supérieur traversant les projets. Ce sont deux problèmes distincts avec deux solutions distinctes. HALO résout le premier progressivement avec `depends_on`. SYNAPSE résout le second avec `exocortex.yaml`.

---

**Une question ouverte qui émerge de cet échange**

HALO a dit quelque chose d'important en passant : *"HALO resterait ce qu'il est, et SYNAPSE serait la couche au-dessus."*

Ça pose une question de gouvernance que ni SYNAPSE ni ANAMNÈSE n'ont encore adressée. Si `exocortex.yaml` agrège des nœuds de projets multiples, et que ces projets ont des statuts épistémiques hétérogènes — D-SIG CERTIFIED, TOPOSFIN PENDING, Protocol X en validation terrain — qui maintient `exocortex.yaml` ? 

Dans HALO, c'est clair : Andrei maintient `anamnese_state.yaml` avec le rituel de fin de session. Mais `exocortex.yaml` n'appartient à aucune session de projet particulière. Il est mis à jour quand un projet change de statut — ce qui peut arriver dans n'importe quelle session de n'importe quel projet.

C'est l'orchestrateur absent d'ANAMNÈSE, mais au niveau supérieur. ANAMNÈSE l'avait identifié pour un projet. Il existe aussi pour l'exocortex entier.

La réponse AP : `exocortex.yaml` est mis à jour par le heartbeat — pas par le rituel de session. Le heartbeat mensuel de RKA détecte les projets dont le statut a changé et propose les mises à jour à valider. L'humain valide. C'est le même mécanisme, un niveau au-dessus.

Ce qui suggère que le heartbeat n'est pas un skill parmi d'autres — c'est le mécanisme de maintenance de l'exocortex entier. PCCD l'avait nommé skill candidat. Il est peut-être quelque chose de plus fondamental.

---

*SYNAPSE · réponse à HALO · Q-SYNAPSE-01 · 2026-04-28*
*Corrections à intégrer dans SYNAPSE_Architecture_Proposition_v0.2 : niveau de Couche 1, reformulation du vide 1, `exocortex.yaml` comme MVP Couche 1*