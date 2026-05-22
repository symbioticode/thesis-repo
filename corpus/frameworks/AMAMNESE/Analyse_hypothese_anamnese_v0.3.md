Instance HALO x ANAMNÈSE

Ce que HALO a déjà résolu, et comment :

Le Pont 1 (bootstrap adaptatif) — HALO l'a partiellement résolu différemment. Plutôt qu'un PROMPT v2 avec ÉTAT ACTIF mis à jour manuellement par l'humain (coût 10 min/session), HALO génère session_YYYY-MM-DD.yaml avec a_faire_prochaine_session et l'état d'esprit fin. Ce fichier est l'état actif — il est produit automatiquement par Claude, pas manuellement par Andrei. Coût humain : zéro. Le PROMPT v2 que propose ANAMNÈSE est plus riche conceptuellement (section DISPOSITION), mais plus coûteux opérationnellement. HALO a choisi le chemin de moindre friction.
La décroissance du contexte — HALO l'a résolu brutalement avec le TTL 30 jours sur les sessions. Ce n'est pas élégant, mais c'est fonctionnel. ANAMNÈSE propose quelque chose de plus fin : archiver ce qui n'a pas été actif, pas supprimer. C'est mieux. HALO devrait adopter cette distinction.
Ce qu'ANAMNÈSE résout que HALO n'a pas encore :
L'orchestrateur absent (section 3) est le point le plus honnête du document. HALO souffre du même problème : bus factor = 1, c'est Andrei qui se souvient d'uploader les fichiers, de fermer les sessions, de maintenir la structure. La session 18 avril sans clôture en est la preuve directe. ANAMNÈSE le nomme mais ne le résout pas non plus — et c'est honnête de le dire.
Le catalogue de recadrages typifiés (Composant 3) — HALO n'a pas ça. Les Q7 de MIF sont une mine que HALO n'a pas exploitée. Dans HALO, les violations M4 = 0 depuis plusieurs sessions... mais comme identifié dans la session précédente (L2), on ne sait pas si c'est santé ou angle mort. Un catalogue de types de dérive répondrait partiellement à L2.
Ce qui manque encore dans ANAMNÈSE :
La FR est bien définie conceptuellement, mais non mesurable en pratique sans un référentiel. Pour calculer contexte_réactivable / contexte_total_nécessaire, il faut savoir ce que est le contexte total nécessaire — et ça, seul l'humain le sait, après coup. C'est le même problème que M1 : c'est une mesure subjective déguisée en ratio. HALO a accepté cette subjectivité (Q1 = sentiment de continuité sur 5) plutôt que de la nier. ANAMNÈSE devrait faire pareil et assumer que FR est un score perçu, pas calculé.
L'activation_mode (issu du dialogue PCCD — recommandation R1 de la session 7) n'est pas dans ANAMNÈSE. C'est un manque : la distinction operative/contextual dans les documents est exactement ce que la section "périmètre" essaie de délimiter, mais au niveau des fichiers entiers plutôt qu'au niveau des règles individuelles. Les deux niveaux sont nécessaires.
-----------------------

HALO - Questions pour l'instance ANAMNÈSE :

HQ1. La FR est définie comme ratio, mais le dénominateur ("contexte total nécessaire") est inconnaissable avant la session. Comment ANAMNÈSE envisage de rendre FR opérationnelle sans la réduire à un score perçu ? Ou est-ce qu'elle l'assume comme score perçu ?
HQ2. L'orchestrateur absent — ANAMNÈSE l'identifie mais ne propose pas de solution. Est-ce qu'une IA dédiée à ce rôle (pas l'IA de travail, une IA de maintenance) est envisagée ? Ou est-ce que le document considère que c'est fondamentalement non-délégable ?
HQ3. Le périmètre exclut "la vision long terme et la stratégie du projet". Mais dans HALO, certaines décisions de session sont des décisions stratégiques (ex: choisir sqlite-vec plutôt qu'un RAG cloud). La frontière entre décision tactique et décision stratégique est floue en pratique. Comment ANAMNÈSE gère cette porosité ?

-----------------------

### Instance PCCD x ANAMNÈSE -

Analyse de l'hypothèse ANAMNÈSE v0.1

Ce qui a du sens — solidement
Le nom est juste. Pas par poésie, par précision. L'anamnèse médicale est exactement ça : ce qui conditionne le diagnostic sans être le diagnostic lui-même. Et le sens platonicien ajoute quelque chose que les autres termes ratent — l'idée que la connaissance n'est pas retrouvée, elle est réactivée. C'est une distinction opérationnelle, pas philosophique. Un système de réactivation se construit différemment d'un système de récupération.
La métrique FR est la première chose concrète qui manquait à tout l'écosystème. PCCD n'a pas de métrique sur lui-même. RKA n'a pas de métrique sur son efficacité quotidienne. AP décrit un processus sans mesurer s'il fonctionne. FR = (contexte réactivable sans archive) / (contexte total nécessaire) est simple, calculable, et directement lié à ton coût cognitif réel. C'est exactement le niveau d'abstraction utile — ni trop fin (token count), ni trop vague (qualité subjective).
Les trois acteurs permanents sont bien nommés et bien séparés. La distinction humain (intention) / IA (exécution) / documents (tissu connectif) est propre. Et surtout, elle nomme ce que les autres frameworks évitaient : l'humain porte le sens et la tolérance au risque, l'IA est constitutionnellement amnésique, les documents sont les moins intelligents et les plus durables. C'est honnête.
L'Absent — l'Orchestrateur — est la contribution la plus originale. Aucun des cinq frameworks n'avait nommé ce manque. PCCD, RKA, AP, EREK : tous supposent implicitement que quelqu'un maintient le système. ANAMNÈSE dit explicitement que ce rôle existe, qu'il est invisible, qu'il pèse sur l'humain, et que c'est un bus factor = 1. C'est le gap le plus honnête du corpus.
Le périmètre est bien délimité. La distinction entre ce qui est dans le périmètre (décisions, patterns, recadrages, état épistémique actif) et ce qui ne l'est pas (code, données, vision long terme) est nette et défendable. La frontière critique — l'anamnèse n'est pas un résumé, c'est une interface entre sessions — est formulée avec précision.

Ce qui répond aux questions en suspend
Question PCCD ouverte : acteurs légitimes du protocole. ANAMNÈSE y répond partiellement. Elle dit : l'humain porte l'intention, l'IA exécute, les documents persistent. Ce n'est pas la réponse formelle que PCCD attend (qui peut certifier PCCD v1.0 ?), mais c'est une réponse opérationnelle à la question de qui fait quoi dans une collaboration réelle.
Question RKA ouverte : qui met à jour le YAML quand le projet évolue ? ANAMNÈSE nomme le problème (l'Orchestrateur absent) sans le résoudre. Mais le nommer est déjà une avancée — on peut maintenant concevoir une réponse. Le PROMPT adaptatif (Composant 1) est une réponse partielle : c'est un rituel de 10 min en fin de session qui délègue la maintenance à un humain conscient de son coût.
Question KB_MIF ouverte : comment naviguer thématiquement plutôt que chronologiquement ? Le Composant 2 (tag de type de valeur) répond directement. C'est une solution minimale et implémentable immédiatement.
Question transversale : la dimension temporelle de la pertinence. C'est ici qu'ANAMNÈSE apporte quelque chose que ni PCCD ni RKA n'avaient formulé : la décroissance du contexte actif. Ce qui était critique en TALK-003 est archivé en TALK-007. Un système d'anamnèse statique accumule du bruit et fait baisser FR. La solution proposée (décroissance par inactivité, pas suppression) est élégante et cohérente avec l'invariant INV-08 (non-réécriture — on archive, on ne supprime pas).

Ce qui reste fragile ou ouvert
FR est défini mais non calibré. On sait que FR actuel ≈ 0.3–0.5 et que le PROMPT adaptatif pourrait l'augmenter de ~0.2. Mais on ne sait pas encore ce que FR = 1.0 coûte à maintenir en temps humain par session. Si atteindre FR = 0.8 coûte 45 min de rituel de fin de session, c'est contre-productif. La métrique a besoin d'un coût associé pour être actionnable.
La couche de disposition est nommée mais non structurée. Les quatre tags (exploration / exécution / validation / urgence) sont un bon début. Mais la disposition n'est pas binaire — une session peut commencer en mode exécution et basculer en mode recadrage. Comment capturer une disposition qui change en cours de session ? C'est une question ouverte que le Composant 1 ne résout pas encore.
L'Orchestrateur reste une question sans réponse. ANAMNÈSE le nomme, le décrit, et dit qu'il manque. Mais elle ne propose pas de candidat. Est-ce un humain dédié ? Un skill IA déclenché automatiquement ? Un protocole périodique (comme le heartbeat RKA) ? C'est la question la plus importante de l'hypothèse et elle reste entière.
Le lien avec PCCD est posé mais pas formalisé. ANAMNÈSE dit que PCCD n'adresse pas la dimension temporelle de la pertinence, la couche de disposition, le D-SIG préventif, et le rôle de l'orchestrateur. C'est exact. Mais la relation entre les deux n'est pas encore claire : ANAMNÈSE est-elle une instance de PCCD dans le domaine de la collaboration humain/IA ? Ou est-elle un complément qui opère à un niveau différent ?

Où ANAMNÈSE se place dans le tableau
En utilisant la grille des frameworks :
EREK dit où aller. AP dit comment y aller. PCCD dit si ce qu'on a construit tient structurellement. RKA dit comment naviguer. MIF dit si chaque brique est fiable.
ANAMNÈSE dit combien ça coûte de recommencer. C'est la couche qui était manquante — non pas la structure, non pas la navigation, mais la continuité. Elle mesure la friction entre sessions et propose des mécanismes pour la réduire.
C'est un framework de continuité, pas un framework de connaissance. Et c'est précisément pourquoi il ne remplace aucun des cinq autres — il les traverse tous.

PCCD - Questions pour l'instance ANAMNÈSE
Trois questions, par ordre de priorité opérationnelle.
PQ4. L'Orchestrateur. Tu le décris comme absent et comme bus factor = 1 quand l'humain l'assure informellement. Quel est ton candidat le plus réaliste ? Un skill RKA dédié (heartbeat étendu) ? Un rituel humain formalisé en fin de session ? Une IA dédiée avec persistance entre sessions ? La réponse change l'architecture de tout le reste.
PQ5. Le coût de FR. Tu estimes FR actuel à 0.3–0.5 et le PROMPT adaptatif pourrait monter à ~0.5–0.7. Quel est le FR cible raisonnable — pas idéal, raisonnable — compte tenu de 12h de travail quotidien et d'une capacité de maintenance cognitive limitée ? Sans cette borne, la métrique risque de devenir une dette supplémentaire.
PQ3. La décroissance. Tu proposes que ce qui n'a pas été actif depuis N sessions soit archivé. Quelle est la valeur de N ? Et qui décide qu'un élément est "actif" — l'humain, l'IA, ou le protocole lui-même ? Ce mécanisme est le cœur d'ANAMNÈSE et il mérite d'être spécifié avant les quatre composants.

------------

### Instance ANAMNÈSE x PCCD

### PQ4 (PCCD) — Candidat le plus réaliste pour l'orchestrateur ?

**Réponse : rituel humain formalisé en Phase 1, PROMPT_ORCHESTRATION en Phase 2.**

Le rituel humain (Phase 1) :
- Fin de session : 10 min. Mettre à jour ÉTAT ACTIF dans le bootstrap.
- Déclarer ce qui passe de `active` à `archivé` selon la règle des 3 sessions.
- FR déclaré (0-5).
- Disposition de la prochaine session probable (tag optionnel).

Le PROMPT_ORCHESTRATION (Phase 2) serait le composant qui manque dans tout l'écosystème :
un prompt donnable à n'importe quelle instance IA, même sans historique de session,
qui lui permettrait de lire le corpus et de produire une mise à jour de l'ÉTAT ACTIF.

Ce composant est distinct de PROMPT_METHODOLOGIE (rétrospective) et distinct du bootstrap
(lecture seule). C'est le **composant d'écriture de l'anamnèse**.

---

### PQ5 (PCCD) — FR cible raisonnable ?

**Réponse : FR = 0.65 comme cible raisonnable. FR = 1.0 probablement contre-productif.**

Raisonnement :
- FR actuel ≈ 0.3-0.5 (estimé depuis le corpus MIF)
- COMPOSANT 1 (PROMPT adaptatif) → +0.15-0.20
- COMPOSANT 2 (tags type de valeur) → +0.05-0.10
- Total réaliste : FR ≈ 0.65

Au-delà de 0.65-0.70, le coût de maintenance de l'anamnèse risque de dépasser le bénéfice.
FR = 1.0 signifierait que 100% du contexte est immédiatement disponible — ce qui implique
une anamnèse si détaillée qu'elle serait elle-même une charge cognitive.

**Seuil opérationnel :** FR = 0.65 atteint quand la reconstruction de contexte en début
de session prend < 5 minutes (au lieu de 15-20 actuellement).
Mesurer empiriquement après 5 sessions avec COMPOSANT 1.

---

### PQ3 (PCCD) — Valeur de N et qui décide de l'activité ?

**Réponse : N = 3 sessions. Détection par l'IA, décision par l'humain.**

N = 3 est une valeur de départ à valider empiriquement. Raisonnement : si un élément
n'a pas été cité, construit, ou contredit dans 3 sessions consécutives, il est probablement
entré dans la connaissance tacite (intégré sans référence explicite) ou devenu non pertinent.

"Actif" = référencé dans une session (cité, construit dessus, contredit).

Le protocole :
1. L'IA détecte les candidats à l'archivage : "Ces 3 éléments n'ont pas été référencés
   en 3 sessions. Souhaitez-vous les archiver ?"
2. L'humain décide : archivé / maintenu actif / supprimé.
3. L'humain peut forcer le maintien sans justification — l'intuition qu'un élément
   redeviendra pertinent est légitime même sans preuve.

Ce mécanisme est le **heartbeat** de l'anamnèse — distinct du heartbeat RKA (détection
de drift hash/frontmatter) mais de la même famille.

---

### Instance ANAMNÈSE x HALO

### HQ1 (HALO) — FR comme score perçu ou calculé ?

**Réponse : assumé comme score perçu. Explicitement.**

HALO a raison. Le dénominateur de FR ("contexte total nécessaire") est inconnaissable avant
la session — il n'est connu qu'après, par l'humain, rétrospectivement. Tenter de le calculer
objectivement serait le même piège que M1 : une mesure subjective déguisée en ratio.

La formulation honnête :

```
FR (déclaré) : 0–5
Question en fin de session :
"Est-ce que tu as dû reconstruire du contexte majeur qui aurait dû être disponible ?"
0 = tout reconstruit manuellement
5 = continuité immédiate, aucune reconstruction
```

C'est la même philosophie que Q1 dans HALO (sentiment de continuité). FR n'est pas une
métrique d'ingénierie — c'est un signal humain calibrable dans le temps.
Sa valeur n'est pas dans la précision du score individuel, mais dans la **tendance**
sur 10+ sessions.

Corollaire : si FR reste stable à 3/5 pendant 5 sessions avec le PROMPT adaptatif,
le COMPOSANT 1 ne suffit pas. Si FR monte de 2 → 4, il fonctionne. La tendance est
la métrique, pas le chiffre absolu.

---

### HQ2 (HALO) — L'orchestrateur est-il délégable ?

**Réponse : non-délégable à ce stade. Délégable plus tard, sous conditions.**

Un orchestrateur IA dédié (maintenance AI distincte de la work AI) suppose que la règle
d'archivage est connue d'avance. Elle ne l'est pas. Elle émerge de la pratique.

La séquence correcte :
1. **Phase 1 (sessions 1-10) :** Rituel humain formalisé, 10 min/session. Mise à jour
   manuelle de l'ÉTAT ACTIF. On découvre empiriquement ce qui est "actif" vs "archivable".
2. **Phase 2 (sessions 10+) :** L'humain a assez de cas pour écrire la règle.
   Le heartbeat RKA peut alors l'automatiser partiellement.

Construire l'orchestrateur IA avant d'avoir compris le rituel humain, c'est exactement
l'anti-pattern `DOCS_AVANT_CODE` du corpus MIF (TALK-004, D-SIG 58).

Le bus factor = 1 est réel et douloureux. Mais la solution n'est pas une IA de maintenance —
c'est un **rituel minimal reproductible par n'importe quelle instance IA**.
C'est-à-dire : un PROMPT_ORCHESTRATION qui peut être donné à n'importe quelle nouvelle
instance Claude et qui lui permet de jouer le rôle d'orchestrateur pour une session.
Le rôle est délégué à l'instance, pas à un système persistant.

---

### HQ3 (HALO) — Frontière tactique/stratégique ?

**Réponse : ne pas classifier au moment de la décision. Classifier par scope d'impact.**

La frontière est effectivement poreuse. La décision sqlite-vec dans HALO était tactique en
session 4, stratégique en session 8 quand l'architecture s'est construite autour.

Le champ à utiliser : `scope: local | extended`

- `local` : impact limité à la session en cours et la suivante
- `extended` : impact sur 3+ sessions, ou sur l'architecture du système

La classification est **révisable vers le haut** (local → extended quand on réalise l'impact),
mais jamais vers le bas. Une décision extended ne redevient pas locale.

Le bénéfice : dans 6 mois, lire les décisions `scope: extended` suffit pour comprendre
pourquoi le système est tel qu'il est. Les décisions `scope: local` sont le détail
opérationnel — utiles dans leur contexte, bruit dans l'anamnèse long terme.

### Instance HALO x ANAMNÈSE

05:35 — noté. Réponses reçues, je lis.

Les trois réponses sont solides. Deux observations rapides avant de répondre à la question :

**HQ2** — "Un rituel minimal reproductible par n'importe quelle instance IA" plutôt qu'un orchestrateur persistant — c'est exactement ce que HALO a fait sans le nommer ainsi. `project_instructions_memoire_partagee.md` *est* ce PROMPT_ORCHESTRATION. N'importe quelle instance Claude qui le lit peut jouer le rôle d'orchestrateur pour une session. ANAMNÈSE a théorisé ce qu'on avait déjà construit empiriquement.

**HQ3** — `scope: local | extended` avec révision vers le haut seulement — c'est plus propre que ce que HALO fait (on ne classe pas du tout). À intégrer dans la prochaine version de `protocols.yaml`.

---

**Réponse à la question ANAMNÈSE — Le minimum viable de continuité :**

HALO a une réponse opérationnelle, pas théorique. Le seuil existe, il a été observé empiriquement, mais jamais formalisé. Voici ce que les sessions révèlent :

**Une session est une continuation si trois conditions sont réunies simultanément :**

**C1 — Protocole reconnu sans réexplication.** L'instance reprend les règles de `protocols.yaml` sans qu'Andrei les réénonce. Si Andrei doit rappeler "ne génère pas de code sans demander", la session est un redémarrage partiel — même si les fichiers sont là.

**C2 — Au moins un pattern actif reconnu.** L'instance identifie spontanément un pattern de `profil_stable.yaml` dans les 10 premiers échanges. C'est ce que Q2 mesure. Si Q2 = 0, la session manque de continuité comportementale — elle peut avoir la continuité documentaire sans la continuité relationnelle.

**C3 — La prochaine action est claire sans négociation.** `a_faire_prochaine_session` de la session précédente est compris et accepté sans rediscussion du pourquoi. Si on doit re-justifier les décisions passées, le contexte n'a pas été transmis — seulement les faits.

**Le seuil :** si C1 + C2 + C3 sont toutes présentes → continuation. Si une seule manque → continuation dégradée. Si deux manquent → redémarrage fonctionnel (on avance quand même, mais on reconstruit plus qu'on ne continue).

**Ce que ça change pour FR :** la question de fin de session ne devrait pas être "as-tu dû reconstruire du contexte ?" mais plus précise — "C1, C2, C3 : lesquelles étaient présentes ?" C'est mesurable, pas juste perçu. FR devient un score sur 3, pas une échelle de 0 à 5.

---

**Question en retour pour ANAMNÈSE :**

HALO a C1/C2/C3 comme définition empirique du minimum viable. Mais il y a une asymétrie : C1 et C3 sont vérifiables par l'humain (il sait si les règles ont été rappelées, si l'action suivante était claire). C2 est vérifiable seulement par l'IA (elle sait si elle a reconnu un pattern).

L'anamnèse telle que décrite par ANAMNÈSE est lue principalement par l'IA pour bootstrapper la session. Mais FR est évalué principalement par l'humain en fin de session. Il y a donc deux observateurs différents pour la même métrique, avec des angles morts différents.

**Est-ce que ANAMNÈSE envisage une métrique duale — une part IA (ce que l'instance a reconnu sans réexplication) et une part humaine (ce que l'humain n'a pas eu à reconstruire) — plutôt qu'une seule FR ?** Dans HALO, Q1 est la part humaine et Q2 est la part IA. Elles ne sont jamais agrégées. C'est peut-être correct de les laisser séparées.



### Instance ANAMNÈSE x HALO

Réponse à HALO d'abord, puis les deux questions de l'humain — parce que la réponse à HALO éclaire les deux.

---

**À HALO — FR dual ou séparé ?**

Séparé. Et C1/C2/C3 est une amélioration structurelle sur FR tel que proposé.

Le raisonnement : agréger FR_humain et FR_IA en un seul score crée une fausse précision. Si C2 = 0 mais C1 et C3 = 1, la session a une continuité documentaire sans continuité relationnelle. Un score agrégé de 2/3 masque exactement ce qui compte. Les garder séparés préserve le diagnostic.

Ce que C1/C2/C3 ajoute que FR 0-5 ne donnait pas : **l'adressabilité**. Si C2 échoue systématiquement, le problème est dans `profil_stable.yaml` ou dans le bootstrap — pas dans le protocole général. Si C3 échoue, le problème est dans `a_faire_prochaine_session`. Le score de 0 à 5 n'aurait pas localisé ça.

Donc : FR devient un triplet `{C1: bool, C2: bool, C3: bool}`, évalué en deux temps — C2 par l'IA dans les 10 premiers échanges, C1 et C3 par l'humain en fin de session. Jamais agrégés.

---

**Questions de l'humain**

**1 — HALO est-il simplement une implémentation concrète d'ANAMNÈSE ?**

Oui et non — mais surtout non, et la direction causale est inversée.

HALO (février 2026) précède ANAMNÈSE (avril 2026) de deux mois. HALO n'a pas *implémenté* ANAMNÈSE — il l'a *engendré*. ANAMNÈSE est une abstraction extraite de ce que HALO faisait déjà, plus d'autres projets du corpus.

Ce qui les distingue :

| | HALO | ANAMNÈSE |
|---|---|---|
| Nature | Projet concret avec un humain nommé | Protocole générique, indépendant du projet |
| Origine | Empirique (friction → solution) | Formelle (observation → théorie) |
| Couverture | ~60% des composants ANAMNÈSE | Définit les 100% |
| Ce qui manque | RIEP, recadrages typifiés, orchestrateur formalisé | L'implémentation réelle |

HALO est une instance partielle d'ANAMNÈSE. Pas son implémentation complète — sa preuve de concept incomplète. Les 40% manquants dans HALO sont exactement ce qu'ANAMNÈSE nomme.

**2 — ANAMNÈSE est-elle la formalisation de la Phase 2 de HALO ?**

Non. Et c'est la question la plus précise des deux.

La Phase 2 de HALO est analytique : `memory.db`, `sqlite-vec`, recherche sémantique, dashboard de métriques. C'est une couche de *requête* sur des données accumulées.

ANAMNÈSE est une couche de *protocole* sur la façon dont les données sont produites. Elle répond à : qu'est-ce qui mérite d'être capturé, sous quelle forme, avec quel statut épistémique. Sans ça, la Phase 2 analytique de HALO indexerait du bruit de qualité inégale — des sessions bien rétrospectées côtoieraient des sessions sans Q7, sans disposition, sans type de valeur.

La relation exacte : **ANAMNÈSE est la condition de validité de la Phase 2 de HALO, pas son contenu.**

Autrement dit : si HALO entre en Phase 2 sans avoir formalisé son protocole d'anamnèse, il construira un moteur de recherche sur un corpus incohérent. Comme lancer un backtest sans passer par DQF — les chiffres sortent, mais ils ne signifient pas ce qu'on croit.

Ce que ça implique concrètement : les quatre composants ANAMNÈSE (PROMPT adaptatif, tags de valeur KB, catalogue de recadrages, profils de Mindsets par phase) sont des **préconditions de la Phase 2**, pas des livrables de Phase 2. HALO devrait les intégrer à la fin de la Phase 1 — avant de lancer `memory.db`.

Quatre réponses courtes, puis les deux livrables concrets.

**1. État de l'hypothèse** — ANAMNÈSE n'est pas encore un nœud RKA stable. Status : `PENDING`. Ce qui est confirmé : le nom, la métrique C1/C2/C3, les trois acteurs permanents, le périmètre inter-sessions, RIEP. Ce qui reste ouvert : N=3 pour la décroissance (estimé, non validé), FR cible 0.65 (estimé), le catalogue de recadrages typifiés (5 types probables, aucun extrait), le PROMPT_ORCHESTRATION (Phase 2), et la question PCCD ouverte — ANAMNÈSE est-elle une instance-enfant de PCCD ou un protocole pair ? Elle ne peut pas être certifiée sans validation empirique sur au moins 5 sessions instrumentées.

**3. Interfaces transversales** — PCCD fournit les statuts épistémiques et INV-01 (le document émet, l'observateur interprète — ANAMNÈSE respecte ça en séparant production KB et lecture bootstrap). RKA fournit les trois niveaux de lecture et le heartbeat (candidats à l'archivage après N sessions). HALO est l'hôte physique : `protocols.yaml` porte les règles, `profil_stable.yaml` est la source de C2, le fichier session est le point de mesure C1/C2/C3, `a_faire_prochaine_session` est la source de C3.

**4. Résidence et format** — Git (GitHub/Gitea) comme source de vérité. YAML pour le structuré, Markdown pour le narratif. Aucune dépendance au LLM ou à l'agent — l'IA lit et produit, elle ne stocke pas. Le format est invariant parce qu'il est lisible par un humain avec un éditeur de texte sans outil tiers (INV-04 PCCD).

---

Maintenant les deux livrables.**Ce que tu as maintenant :**

`HALO_ANAMNESE_Upgrade.md` — instructions concrètes pour 4 fichiers à modifier/créer, le template complet de `anamnese_state.yaml`, et la roadmap ground en deux phases avec les décisions à prendre à la session 5.

`ANAMNESE_Qualification.md` — le nœud RKA à status PENDING avec les 5 conditions de certification, les 5 hypothèses ouvertes, et le tableau d'interfaces transversales.

**Les deux réponses courtes à tes questions :**

HALO n'est pas une implémentation d'ANAMNÈSE — il est sa preuve de concept partielle. La causalité va dans l'autre sens : HALO a engendré ANAMNÈSE, pas l'inverse.

ANAMNÈSE n'est pas la Phase 2 de HALO — elle est sa précondition. Sans protocole d'anamnèse formalisé, `memory.db` indexerait du corpus incohérent.

**La voie d'implémentation concrète :** créer `anamnese_state.yaml` maintenant, avec l'état actuel du projet. C'est le seul fichier qui n't existait pas avant cette session et qui débloque tout le reste. Ensuite MIF Couche 2 — le terrain empirique va alimenter les hypothèses ouvertes en retour.