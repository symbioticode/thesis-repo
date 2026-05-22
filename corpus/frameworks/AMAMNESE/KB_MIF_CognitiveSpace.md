# L'Espace Cognitif Partagé — Vers une Formalisation
## Ce qui reste à matérialiser pour simplifier la gestion de la connaissance

**Date :** Avril 2026  
**Référence :** KB_MIF_Value_Analysis.md · PCCD Hypothesis v0.3 · RKA_Formalisation_v4.md

---

## Préambule : ce que le corpus MIF a révélé

PCCD, RKA, et les 7 conversations MIF tournent autour du même problème sans jamais l'énoncer
directement. Le voici :

**Dans une collaboration humain-IA sur plusieurs mois, il existe un espace où la connaissance
productive vit — ni dans la mémoire de l'humain, ni dans la mémoire de l'IA, ni dans les
fichiers seuls. Cet espace n'a pas de nom. Il n'a pas de technologie. Il existe pourtant.**

La preuve de son existence : quand une session recommence, ni l'humain ni l'IA ne repart
à zéro. Le projet a une continuité qui transcende les deux. Cette continuité est réelle.
Le fait qu'elle soit fragile, coûteuse à maintenir, et partiellement perdue entre les sessions
ne la rend pas moins réelle.

Ce document propose un nom, une métrique, des acteurs, un périmètre, et des ponts
pour cet espace. C'est une hypothèse de travail, pas une théorie complète.

---

## 1. Le Nom

**ANAMNÈSE** (du grec ἀνάμνησις — "non-oubli")

En médecine, l'anamnèse est le recueil des antécédents du patient — ce qui s'est passé avant
la consultation et qui conditionne le diagnostic. En philosophie platonicienne, c'est la
théorie selon laquelle apprendre est se souvenir de ce qu'on savait déjà.

Les deux sens convergent ici. L'anamnèse d'un projet collaboratif humain-IA est :
- L'ensemble des antécédents qui conditionnent la prochaine session (sens médical)
- La connaissance que le projet a produite et qui peut être réactivée (sens philosophique)

Ce n'est pas de la documentation. C'est du **contexte activable**.

La distinction est critique : une documentation peut être lue par quelqu'un qui n'a jamais
touché au projet. Une anamnèse ne peut être activée que par quelqu'un qui a un contexte
minimal — qui sait pourquoi ce projet existe, dans quel état il est, et ce qui compte en ce
moment. L'anamnèse présuppose un lecteur partiellement informé. C'est sa force (concision)
et sa limite (non-portabilité totale).

**Alternatives considérées et rejetées :**
- *Memory Bank* — trop associé aux systèmes de fichiers simples
- *Context Layer* — trop technique, pas de sens philosophique
- *Living Knowledge Base* — redondant avec ce qui existe déjà
- *Inter-Session Continuity Layer (ISCL)* — précis mais froid
- *Collaborative Memory Substrate* — lourd

**ANAMNÈSE** est retenu. Court, précis, avec une profondeur philosophique qui justifie
son usage au-delà de la technique.

---

## 2. La Métrique

**La fidélité de réactivation (FR)**

Définition opérationnelle : la proportion du contexte nécessaire à une session productive
qui peut être reconstituée sans re-lecture complète des archives.

```
FR = (contexte_réactivable_sans_archive) / (contexte_total_nécessaire)
```

FR = 1.0 : une nouvelle instance IA peut commencer à travailler immédiatement avec le
même niveau de pertinence qu'une instance qui a participé à la session précédente.

FR = 0.0 : chaque session recommence à zéro, tous les antécédents doivent être
réinjectés explicitement.

**État actuel du projet MIF :** FR ≈ 0.3-0.5

Le PROMPT_METHODOLOGIE_MIF injecte le contexte statique (architecture, fichiers clés).
Il ne capture pas : la disposition mentale, les hypothèses actives non encore testées,
le "pourquoi ce moment est différent des précédents". Ces éléments doivent être
reconstitués par l'humain à chaque session — coût cognitif réel.

**Ce qui fait monter FR :**
- Bootstrap adaptatif (ce qui est actif maintenant > ce qui est archivé)
- Tag de disposition sur chaque session KB
- Artefacts KB annotés par type de valeur (RICH_PATTERNS, RICH_ANTIPATTERNS)
- Recadrages catalogués avec leur type de déviation

**Ce qui fait baisser FR :**
- Corpus trop volumineux (dilution du signal dans le bruit archivé)
- Sessions non rétrospectées (trous dans la continuité)
- Artefacts sans statut (on ne sait pas si c'est actif, archivé, ou supplanté)

---

## 3. Les Acteurs

L'anamnèse implique trois acteurs aux rôles distincts et non substituables.

### Acteur 1 — L'Humain (porteur de l'intention)

L'humain porte ce que l'anamnèse ne peut pas capturer :
- Le **sens** du projet (pourquoi ça compte, pas juste quoi et comment)
- La **disposition temporelle** (ce qui est urgent maintenant, ce qui peut attendre)
- Le **jugement de qualité contextuel** ("c'est correct pour ce moment")
- La **tolérance au risque** (quelle dette est acceptable, laquelle ne l'est pas)

L'humain est aussi le seul acteur capable de recadrage architecturalement fondé
(comme documenté dans les Q7). Ce rôle ne peut pas être délégué à l'IA.

### Acteur 2 — L'IA (moteur d'exécution)

L'IA apporte :
- La **capacité de production** (code, documentation, patterns) à haute vitesse
- La **cohérence locale** dans les limites du contexte de session
- La **détection de patterns** dans le corpus existant
- L'**implémentation des contraintes** via les Mindsets

L'IA est fondamentalement amnésique entre les sessions. Ce n'est pas un bug —
c'est une propriété à prendre en compte dans l'architecture du système.

### Acteur 3 — Les Documents (tissu connectif)

Les documents ne sont pas un troisième acteur intelligent — ils sont le médium physique
de l'anamnèse. Mais leur rôle est actif, pas passif.

Un document bien formé (avec signal vital, contexte minimal, relations déclarées) réduit
la charge cognitive de réactivation. Un document mal formé (sans statut, sans date, sans
relation) augmente le bruit et dilue FR.

Les documents sont les acteurs les moins intelligents et les plus durables.
Quand l'humain oublie et que l'IA ne se souvient pas, les documents restent.
C'est leur valeur unique.

### L'Absent : l'Orchestrateur

Ce qui manque dans le système actuel est un quatrième acteur : quelque chose (humain,
IA dédiée, script, protocole) dont le rôle est de maintenir l'anamnèse elle-même.

Actuellement, ce rôle est assuré de façon informelle par l'humain (qui se souvient de
coller le PROMPT_METHODOLOGIE_MIF, qui archive les KB articles, qui maintient le D-SIG).
C'est du travail cognitif invisible qui s'accumule. La TALK-001 le nomme : bus factor = 1.

---

## 4. Le Périmètre

L'anamnèse ne couvre pas tout. Elle a une frontière précise.

**Dans le périmètre :**
- Les décisions architecturales et leurs raisons (le POURQUOI, pas seulement le QUOI)
- Les patterns nommés et validés (réutilisables dans une autre session)
- Les anti-patterns documentés (les pièges que ce projet a rencontrés)
- Les recadrages humains et leur type de déviation
- L'état épistémique actif (hypothèses en cours, questions ouvertes)
- La disposition de la session (tags optionnels)

**Hors périmètre :**
- Le code lui-même (géré par git)
- La documentation technique de l'API (géré par les docs formelles)
- Les données brutes et résultats de tests (géré par le système de fichiers)
- La vision long terme et la stratégie du projet (géré par un document de vision séparé)

**La frontière critique :**

L'anamnèse n'est pas un résumé du projet. Elle n'est pas non plus une archive.
C'est une **interface entre sessions** — ce qui permet à une session N+1 d'être productive
sans relire les sessions 1 à N-1.

PCCD a nommé ce périmètre "Niveau 1 — Contexte minimal". RKA l'a formalisé dans le template
YAML. Mais ni l'un ni l'autre n'a répondu à la question temporelle : quelle anamnèse pour
quelle session ? Le contexte actif change. Ce qui était critique en TALK-003 (les 7 checks
DQF) est archivé en TALK-007 (DQF est livré). Un système d'anamnèse statique accumule du
bruit. Il faut un mécanisme de **décroissance du contexte** : ce qui n'a pas été actif
depuis N sessions est archivé, pas supprimé.

---

## 5. Les Ponts

Ce sont les éléments existants qui construisent déjà l'anamnèse, même de façon imparfaite.

### Pont 1 — PROMPT_METHODOLOGIE_MIF

**Ce qu'il fait :** Bootstrap statique. Injecte le contexte de projet en début de session.

**Sa limite :** Il est figé. Il injecte toujours le même volume, quelle que soit la phase.

**Son évolution possible :** Un prompt adaptatif avec un "état actif" mis à jour à chaque
session. Le PROMPT v2 serait :
```
[CONTEXTE STABLE] (architecture, conventions, mindsets)
[ÉTAT ACTIF] (ce qui est en cours, hypothèses ouvertes, décision en suspens)
[DISPOSITION] (tag humain : exploration / exécution / validation / urgence)
```

### Pont 2 — Les fiches KB_MIF_TALK

**Ce qu'elles font :** Artefacts de rétrospective. Capturent ce qui s'est passé et ce
qui en a été extrait.

**Leur limite :** Chronologiques. Difficiles à naviguer thématiquement. Mélangent la haute
densité (TALK-003) et la basse densité (TALK-004 en patterns réutilisables).

**Leur évolution possible :** Tags de type de valeur + status épistémique (comme RKA/PCCD).
Un KB article avec `type_valeur: RICH_PATTERNS` est consulté différemment d'un article
`type_valeur: RICH_ANTIPATTERNS`.

### Pont 3 — Le D-SIG

**Ce qu'il fait :** Métrique de qualité de la collaboration. Signal historique.

**Sa limite :** Calculé post-session, donc non préventif.

**Son évolution possible :** D-SIG intermédiaire à mi-session, déclenché par des signaux
préventifs (volume de production élevé sans validation, accumulation de TODOs,
propositions répétées sans acceptation humaine). Equivalent d'un circuit-breaker.

### Pont 4 — Les Mindsets

**Ce qu'ils font :** Contraintes comportementales de l'IA. Épistémologie de session.

**Leur limite :** Injectés en bloc (15 mindsets), alors que 3-4 sont actifs par phase.

**Leur évolution possible :** Profils de Mindsets par phase (design, implémentation, debug,
documentation). Chaque profil injecte seulement les Mindsets pertinents.

### Pont 5 — Les recadrages Q7

**Ce qu'ils font :** Documentent les moments de basculement humain.

**Leur limite :** Dispersés dans les artefacts KB. Non agrégés. Pas typifiés.

**Leur évolution possible :** Un catalogue de recadrages avec leur type de déviation.
5 types probables à identifier empiriquement sur un corpus plus large :
- Dérive vers l'over-engineering
- Optimisation locale au détriment de la cohérence globale
- Production avant validation
- Promesse sans implémentation
- Invisibilisation de la dette

---

## 6. Ce qui reste à matérialiser

Pour que l'anamnèse devienne un système plutôt qu'une pratique informelle, quatre
composants doivent être formalisés :

**COMPOSANT 1 — Le PROMPT_METHODOLOGIE v2 (adaptatif)**  
Un template de bootstrap avec section ÉTAT ACTIF mis à jour à chaque session.
Coût : un rituel de 10 min en fin de session pour mettre à jour l'état actif.
Bénéfice : FR augmente de ~0.2 sur les sessions suivantes.

**COMPOSANT 2 — Le tag de type de valeur sur les KB articles**  
Un champ `type_valeur: RICH_PATTERNS | RICH_ANTIPATTERNS | RICH_DECISIONS | RICH_CONTEXT`
sur chaque artefact KB.
Coût : 30 secondes par article.
Bénéfice : navigation thématique possible dans le corpus.

**COMPOSANT 3 — Le catalogue de recadrages typifiés**  
Un document `RECADRAGES_CATALOGUE.md` avec les types de déviation et leurs signaux préventifs.
Coût : extraction et classification des Q7 existants (1-2h une fois).
Bénéfice : détection préventive des dérives avant le seuil de recadrage.

**COMPOSANT 4 — Les profils de Mindsets par phase**  
Trois fichiers : `MINDSETS_DESIGN.md`, `MINDSETS_IMPLEMENTATION.md`, `MINDSETS_DEBUG.md`.
Coût : 1h pour répartir les 15 Mindsets actuels.
Bénéfice : injection de contexte pertinent, réduction du bruit.

---

## 7. La question de PCCD

PCCD (Protocole de Cohérence Cognitive Distribuée) répond partiellement à ces questions.
Ses invariants (INV-01 à INV-08) sont directement applicables à l'anamnèse. Ses statuts
épistémiques (PENDING, CERTIFIED, DEPRECATED) sont exactement ce dont les KB articles
ont besoin.

Ce que PCCD n'adresse pas encore :
- La **dimension temporelle de la pertinence** (décroissance du contexte actif)
- La **couche de disposition** (état mental de l'humain comme signal épistémique)
- Le **D-SIG préventif** (signal en temps réel, pas post-session)
- Le **rôle de l'orchestrateur** (qui maintient l'anamnèse elle-même ?)

Ces quatre éléments sont les questions ouvertes qui conduiraient PCCD de PENDING à CERTIFIED
dans le domaine de la collaboration humain-IA sur projets longs.

---

## Conclusion provisoire

L'espace cognitif partagé existe. Il a un nom (ANAMNÈSE), une métrique (fidélité de
réactivation), trois acteurs permanents (humain, IA, documents) et un acteur absent
(l'orchestrateur). Son périmètre est l'interface entre sessions. Ses ponts existent déjà
en embryon (PROMPT, KB articles, D-SIG, Mindsets, Q7).

Ce qui manque n'est pas une technologie nouvelle. C'est une **discipline de maintenance**
appliquée à ce qui existe déjà, combinée à quatre composants formalisés.

L'investissement est modeste. Le gain est une réduction de la charge cognitive de
réactivation — chaque session démarre plus vite, avec moins d'ambiguïté, et l'humain
dépense moins d'énergie à reconstruire ce qui existait déjà.

C'est, au fond, ce que MIF-DQF a tenté de faire pour les métriques financières :
**rendre reconstructible ce qui était tacite.**

---

*ANAMNÈSE v0.1 · hypothèse de travail · Avril 2026*  
*Status : PENDING — à soumettre aux instances concernées*
