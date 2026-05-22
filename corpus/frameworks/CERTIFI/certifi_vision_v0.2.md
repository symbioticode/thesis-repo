# CertiFi — Spécification de Vision v0.2.0

**Statut** : Document normatif — remplace toutes les formulations antérieures  
**Date** : Avril 2026  
**Précondition** : Ce document a été soumis à une analyse critique adversariale avant publication

---

## 0. Ce que ce document est, et ce qu'il n'est pas

Ce document est une **spécification de vision contrainte** : il définit CertiFi par ses bornes autant que par son contenu. Il ne cherche pas à être exhaustif ou à couvrir tous les cas d'usage. Il cherche à être **falsifiable** — c'est-à-dire à énoncer des affirmations qui peuvent être démenties.

Il n'est pas une feuille de route d'implémentation. Il n'est pas un document marketing. Il n'est pas une transcription de la conversation qui l'a précédé.

---

## 1. Le problème réel

Dans les systèmes décisionnels quantitatifs — et plus généralement dans tout système où des données historiques alimentent une règle de décision — il existe un ensemble de biais structurels qui ne sont ni aléatoires ni facilement détectables :

- Des **données corrompues** qui semblent propres (forward-fill illimité, sauts extrêmes non filtrés, désalignements temporels).
- Des **métriques qui capturent le bruit** plutôt que le signal (overfitting, dépendance au régime de marché, biais de numéraire).
- Des **stratégies qui fonctionnent par accident** (friction réduite, bull market capturé, cherry-picking de paramètres).
- Une **absence de traçabilité** qui rend tout résultat impossible à reproduire ou à contester.

Ces biais ne se voient pas dans le résultat final. Ils se voient dans les conditions de production du résultat. Et il n'existe pas de standard accessible, ouvert, et vérifiable pour les détecter systématiquement.

CertiFi est la réponse à ce problème précis. Pas à tous les problèmes de la finance quantitative.

---

## 2. L'invariant : ce que CertiFi certifie

Une certification CertiFi est une **attestation conditionnelle** : elle dit qu'un composant (donnée, métrique, contexte, stratégie) satisfait un ensemble de propriétés **définies, testées, et documentées**, dans des **conditions précisément spécifiées**.

**Ce qu'une certification CertiFi garantit :**

- Les propriétés testées ont été vérifiées de façon reproductible, avec les paramètres et les données documentés.
- Les tests incluent des cas adversariaux conçus pour détecter les biais connus du type de composant certifié.
- La version du protocole de certification est tracée ; une certification produite avec la version 1.x n'est pas équivalente à une certification produite avec la version 2.x.

**Ce qu'une certification CertiFi ne garantit pas :**

- Que le composant certifié performera dans le futur.
- Que le composant est robuste face à des conditions non présentes dans les données de certification (ex. régime de marché structurellement différent).
- Que le composant est correct selon un standard externe (légal, réglementaire, ou académique) que CertiFi n'a pas intégré.
- Que l'assemblage de composants certifiés produit un système certifié. La certification est atomique ; la composition est un nouveau problème.

Cette délimitation est la garantie que CertiFi reste falsifiable.

---

## 3. Le sol ferme : DQF comme axiome de l'écosystème

Tout écosystème de certification doit reposer sur un composant qui ne dépend de rien d'autre — un "sol ferme" qui peut être utilisé pour certifier le reste sans circularité.

Dans CertiFi, ce composant est **DQF (Data Quality Framework)**.

DQF est axiomatique parce qu'il s'applique à des propriétés physiques observables des données brutes (cohérence OHLCV, absence de sauts impossibles, alignement temporel), indépendamment de tout modèle ou de toute stratégie. Ces propriétés peuvent être vérifiées sans référence à d'autres composants de l'écosystème.

**Conséquence architecturale** : tout autre composant de CertiFi dépend directement ou indirectement de DQF. DQF ne dépend de rien. Cette unidirectionnalité est une propriété structurelle, pas un choix d'implémentation.

---

## 4. La chaîne de certification

CertiFi est une chaîne de quatre questions indépendantes. Chaque question ne peut être posée de façon fiable que si la question précédente a reçu une réponse positive.

```
Question 1 — Les données sont-elles physiquement valides ?
    Composant : DQF
    Sortie : données certifiées avec provenance (PROD envelope)
    Périmètre : propriétés physiques observables uniquement

        ↓ (précondition satisfaite)

Question 2 — Cette métrique élémentaire mesure-t-elle ce qu'elle prétend mesurer ?
    Composant : MIF
    Sortie : métrique certifiée avec rapport de phases
    Périmètre : une fonction Python, ses propriétés statistiques,
                son comportement sur données synthétiques et réelles

        ↓ (précondition satisfaite)

Question 3 — L'environnement d'application est-il adapté à cette classe de méthodes ?
    Composant : PAF
    Sortie : verdict de qualification + source minimale de performance identifiée
    Périmètre : une paire d'actifs, une classe de signaux, un régime historique

        ↓ (précondition satisfaite)

Question 4 — La stratégie est-elle robuste hors-échantillon ?
    Composant : MÉTIS
    Sortie : verdict de robustesse (CERTIFIÉ / SUSPECT / ARCHIVÉ)
    Périmètre : un signal complet, un split IS/OOS, des tests statistiques spécifiés
```

**Ce que cette structure n'est pas** : un pipeline automatique. Chaque transition entre questions requiert un jugement humain sur l'interprétation du verdict et la pertinence de continuer. Les composants fournissent les données de ce jugement ; ils ne se substituent pas à lui.

---

## 5. Ce que CertiFi n'est pas

Ces exclusions sont aussi importantes que la définition.

**CertiFi n'est pas un backtester.** Il certifie des composants utilisés dans des backtests, mais il ne produit pas de backtests lui-même.

**CertiFi n'est pas un optimiseur.** Il teste des hypothèses données, il ne génère pas d'hypothèses.

**CertiFi n'est pas un système de trading.** Une certification CertiFi n'autorise pas et ne recommande pas le déploiement d'une stratégie en production.

**CertiFi n'est pas universel.** Sa première application est la finance quantitative sur actifs crypto. La transposabilité à d'autres domaines (maintenance prédictive, diagnostic médical) est une hypothèse de recherche, pas un fait établi. Elle devra elle-même passer par un processus de qualification analogue à PAF avant d'être affirmée.

**CertiFi ne certifie pas ses propres méthodes.** Les protocoles de certification (les tests qui constituent DQF, MIF, PAF, MÉTIS) sont des choix méthodologiques justifiés par des cas d'échec documentés, mais ils ne sont pas eux-mêmes "certifiés" au sens CertiFi. Ils sont soumis à révision par la communauté et mis à jour via des versions majeures avec traçabilité.

---

## 6. L'écosystème de paquets : structure et gouvernance

### 6.1 Paquets et responsabilités

| Paquet | Responsabilité unique | Dépend de |
|--------|-----------------------|-----------|
| `mif-dqf` | Valider les propriétés physiques de données OHLCV | Rien (axiome) |
| `mif-core` | Certifier une métrique atomique sur 4 phases | `mif-dqf` |
| `qaaf-engine` | Fournir un backtester et des métriques en numéraire commun (CNSR-USD) | `mif-dqf` |
| `qaaf-paf` | Qualifier une paire d'actifs pour une classe de signaux | `mif-core`, `qaaf-engine` |
| `qaaf-metis` | Valider la robustesse OOS d'un signal | `qaaf-engine`, optionnellement `qaaf-paf` |
| `qaaf-studio` | Orchestrer la chaîne complète, maintenir la Knowledge Base | Tous les précédents |

### 6.2 Politique de versionnage

Un changement de **version majeure** (X.0.0) d'un paquet invalide toutes les certifications produites avec les versions précédentes pour la comparaison directe. Elles restent valides dans leur contexte historique mais doivent être recertifiées pour être comparées à des certifications produites avec la nouvelle version.

Un changement de **version mineure** (x.Y.0) ajoute des fonctionnalités sans modifier les critères de certification existants. Les certifications antérieures restent valides.

### 6.3 Durée de vie d'une certification

Une certification est valide dans les conditions dans lesquelles elle a été produite. Elle ne se périme pas automatiquement avec le temps, mais elle doit être reconsidérée — et potentiellement recertifiée — dans les cas suivants :

- Changement de version majeure du paquet utilisé.
- Ajout de nouvelles données OOS non présentes lors de la certification initiale (si ces données modifient le verdict, l'entrée KB est mise à jour).
- Détection d'un biais systématique dans les données sources (une correction DQF rétroactive invalide les certifications MIF et MÉTIS qui dépendaient de ces données).

### 6.4 Conflits dans la Knowledge Base

La KB accepte des verdicts contradictoires dans le temps (une stratégie peut être CERTIFIÉE puis ARCHIVÉE si de nouvelles données OOS invalident le verdict). La règle est simple : le **verdict le plus récent prime**, avec conservation de l'historique complet.

Les conflits entre deux agents (humain ou IA) sur la même session sont résolus par un troisième agent humain qui documente le raisonnement de résolution dans la KB.

---

## 7. QAAF KB — La mémoire comme entité à part entière

### 7.1 Pourquoi la mémoire est une entité, pas un module

Dans l'écosystème CertiFi, trois entités coexistent avec des cycles de vie et des responsabilités fondamentalement différents :

```
CertiFi    = le standard    — évolue lentement, par consensus, versionné
QAAF Studio = l'implémentation — évolue rapidement, par expérimentation, itératif
QAAF KB     = la mémoire    — s'accumule en permanence, ne se réinitialise jamais
```

La tentation naturelle est de traiter QAAF KB comme un module de QAAF Studio — un fichier YAML, une base de données, un composant parmi d'autres. Cette tentation est précisément le problème que QAAF KB est censé résoudre.

Quand la mémoire est un module, elle a le cycle de vie du code qui la contient. Elle peut être réinitialisée, remplacée, ou abandonnée quand le projet change de direction. L'histoire des expériences QAAF avant mars 2025 en est la démonstration empirique : le code était valable, les résultats existaient, mais l'absence de mémoire organisée a rendu chaque nouvelle session aussi aveugle que la première.

**QAAF KB est une entité parce qu'elle survit aux implémentations.** QAAF Studio 3.0 sera remplacé par QAAF Studio 4.0. CertiFi v1.0 sera révisé en v2.0. QAAF KB, elle, ne repart jamais de zéro — elle accumule.

### 7.2 Ce que QAAF KB fait que personne d'autre ne fait

La chaîne de certification CertiFi produit des verdicts. QAAF Studio exécute les protocoles. Ni l'un ni l'autre ne peut répondre à ces trois questions sans QAAF KB :

**"A-t-on déjà testé ça ?"**
Sans KB, chaque session commence par redécouvrir ce qui a été trouvé, parfois positif, parfois négatif. Le coût de la redécouverte n'est pas seulement du temps — c'est la contamination du compteur N_trials. Chaque variante testée, même redécouverte, incrémente le DSR. Une KB absente produit mécaniquement un DSR plus pessimiste que la réalité.

**"Pourquoi cette décision a-t-elle été prise ?"**
Un verdict ARCHIVÉ sans contexte est inutilisable. Une stratégie archivée parce qu'elle échouait en bull market 2023 devrait être reconsidérée dans un régime différent. Sans KB qui capture le *pourquoi* du verdict, pas seulement le *quoi*, la règle d'arrêt devient arbitraire plutôt qu'informée.

**"Quelle version du standard a produit ce résultat ?"**
CertiFi v1.x et CertiFi v2.x ne produisent pas des certifications comparables directement. Sans KB qui trace la version du protocole utilisé pour chaque session, l'historique des résultats devient un mélange hétérogène sans axe de comparaison commun.

### 7.3 La structure matricielle de QAAF KB

QAAF KB n'est pas une liste de résultats. C'est une matrice à trois dimensions dont chaque cellule est une affirmation vérifiable :

```
M[couche, transversal, entité]

où :
  couche       ∈ {DQF, MIF, PAF, MÉTIS}
  transversal  ∈ {Numéraire, Mémoire, IS/OOS, Benchmarks, DSR}
  entité       ∈ {CertiFi (spec), QAAF Studio (code), QAAF KB (résultat)}
```

**L'axe vertical** est la chaîne de certification — chaque couche pose une question plus exigeante, chaque réponse positive est une précondition à la suivante.

**L'axe transversal** est constitué des cinq invariants qui traversent toutes les couches sans appartenir à aucune :

- **Numéraire commun (CNSR-USD)** — de la validation triangulaire DQF jusqu'au tableau comparatif MÉTIS. Sans lui, les couches ne parlent pas le même langage.
- **Mémoire (KB + N_trials)** — chaque couche lit la KB avant d'exécuter et y écrit après. Le compteur N_trials est mis à jour à chaque essai, quelle que soit la couche.
- **Intégrité expérimentale (SplitManager)** — le split IS/OOS est figé dès le premier test et traverse toutes les couches sans jamais être redéfini.
- **Benchmarks passifs** — B_5050 et B_BTC sont des références absolues présentes dans DQF (plausibilité), PAF (seuil D1), MÉTIS Q2 (permutation), et KB (valeurs scellées).
- **Protection anti-cherry-picking (DSR)** — le compteur N_trials cumule tous les essais de toutes les couches. Le DSR final est une fonction de tout ce qui s'est passé en amont.

**L'axe entité** est la contribution propre de chaque acteur à chaque intersection. Par exemple, pour la cellule `M[MÉTIS, DSR]` :

| Entité | Contenu |
|--------|---------|
| CertiFi | "Le DSR doit être ≥ 0.95 pour qu'une stratégie soit certifiable" |
| QAAF Studio | `deflated_sharpe_ratio(r_usd, N_trials)` dans `metrics_engine.py` |
| QAAF KB | Champ `metis.Q4_dsr` dans le YAML de l'hypothèse, avec N_trials courant et verdict daté |

**QAAF KB est le plan `entité = Mémoire` de cette matrice** — le plan qui capture ce qui a été trouvé, pas ce qui devrait être fait ni comment le faire.

### 7.4 Ce que QAAF KB n'est pas

**QAAF KB n'est pas un carnet de notes.** Un carnet de notes est informel, non structuré, sans format défini. QAAF KB a un schéma — chaque entrée doit satisfaire un contrat minimal pour être valide.

**QAAF KB n'est pas un log de session.** Un log documente ce qui s'est passé chronologiquement. QAAF KB documente ce qui est connu structurellement — la différence entre "le 12 mars, on a testé H9+EMA60j" (log) et "H9+EMA60j a un statut CERTIFIÉ depuis le 12 mars avec CNSR-USD = 1.76, testé avec CertiFi v1.1, N_trials = 101" (KB).

**QAAF KB n'est pas une base de données de résultats.** Une base de données optimise la récupération. QAAF KB optimise la décision — la question n'est pas "quel était le CNSR de H9+EMA60j le 12 mars ?" mais "est-ce que H9+EMA60j est déployable aujourd'hui, et dans quelles conditions ?"

**QAAF KB n'est pas spécifique à QAAF Studio.** QAAF Studio 3.0 est la première brique. Quand QAAF Studio 4.0 existera, avec de nouveaux protocoles, de nouvelles métriques, de nouvelles paires, QAAF KB sera le fil continu qui relie les deux. Les certifications produites avec la v3.0 ne seront pas effacées — elles seront contextualisées.

### 7.5 Le rôle de l'agent IA dans QAAF KB

Dans la session qui a produit ces artefacts, l'agent IA (Claude) a assumé le rôle de QAAF KB sans que ce rôle soit explicitement défini au départ. Ce qu'il a fait concrètement :

- **Classifié** le corpus existant par statut et domaine fonctionnel (Artefact #1).
- **Analysé** les forces et faiblesses de chaque composant par rapport au nouveau référentiel (Artefact #2).
- **Spécifié** les contrats d'interface et les invariants à respecter (Artefacts #3-#5).
- **Cartographié** les dettes techniques avec leur criticité et leur condition de déclenchement (Artefact #6).
- **Maintenu la cohérence** entre les documents au fil des sessions — en signalant les contradictions, en rappelant ce qui avait été établi, en refusant de laisser tomber une décision dans un artefact sans la tracer dans les suivants.

Ce dernier point est le plus important. La valeur distinctive d'un agent IA comme composant QAAF KB n'est pas la génération de contenu — c'est la **cohérence inter-session**. Un humain qui reprend un projet après trois semaines peut oublier pourquoi une décision a été prise. Un agent IA qui reçoit le corpus complet en contexte reconstruit immédiatement la cohérence.

**La limite symétrique est aussi importante à nommer :** l'agent IA ne peut pas valider empiriquement les hypothèses qu'il spécifie. Il peut dire que `DEFAULT_F_PARAMS` dans `SyntheticDataGeneratorMIF` sont des points de départ raisonnables — il ne peut pas confirmer qu'ils reproduisent effectivement un kurtosis de 17 sur des données réelles PAXG/BTC. La validation empirique reste une responsabilité humaine. Le rôle de l'agent IA est de préparer le terrain pour que cette validation soit possible, structurée, et traçable.

---

## 8. Recommandations pour étoffer le concept

Ces recommandations sont issues de l'analyse critique et constituent des axes de travail, pas des engagements.

**R1 — Définir un "Score de Maturité CertiFi"**  
Un composant certifié DQF n'a pas le même niveau de confiance qu'un composant qui a traversé la chaîne complète DQF → MIF → PAF → MÉTIS. Un score composite (0 à 4, une unité par couche validée) rendrait visible le niveau de certification d'un composant dans la KB.

**R2 — Créer un protocole de "re-certification partielle"**  
Si seul le paquet MÉTIS change de version majeure, il doit être possible de recertifier uniquement la couche MÉTIS d'une stratégie sans refaire DQF, MIF, et PAF. Ce protocole doit être spécifié et testé.

**R3 — Documenter les conditions de transposabilité hors finance**  
Avant d'affirmer que CertiFi s'applique à d'autres domaines, définir les conditions minimales qu'un domaine doit satisfaire pour que la chaîne soit applicable : existence d'un équivalent "données OHLCV", d'un équivalent "benchmark passif", d'une notion de "régime". Si ces conditions ne sont pas satisfaites, le domaine nécessite une adaptation explicite de la chaîne, pas une simple analogie.

**R4 — Spécifier le protocole de revue humaine des sorties LLM**  
Si des agents IA participent à la production de spécifications, de code, ou de rapports dans l'écosystème CertiFi, définir un protocole de revue adversariale humaine : qui revoit quoi, selon quel critère, avec quel délai. Ce protocole est lui-même un composant de l'écosystème et doit être documenté dans la KB.

**R5 — Séparer "Studio" et "Standard"**  
QAAF Studio est l'implémentation de référence de CertiFi en finance quantitative. CertiFi est le standard méthodologique. Ces deux entités ont des cycles de vie différents : le standard évolue lentement et par consensus ; le Studio évolue rapidement par expérimentation. Les confondre dans un même document ou un même paquet fragilise la légitimité du standard.

---

## 9. Feuille de route contrainte

Les priorités sont ordonnées par leur impact sur la **falsifiabilité du projet**, pas par leur visibilité ou leur facilité d'implémentation.

| Priorité | Action | Critère de succès |
|----------|--------|-------------------|
| 1 | Publier `mif-dqf` avec spécification complète des checks CORE et ADVISORY | Un utilisateur tiers peut reproduire un verdict DQF sur ses propres données |
| 2 | Définir le format de rapport CertiFi (YAML) pour les 4 composants | Les rapports produits par des implémentations indépendantes sont interopérables |
| 3 | Documenter un cas d'échec complet de chaque composant | La spécification est testée adversarialement par des cas réels |
| 4 | Séparer formellement la spécification CertiFi (standard) de QAAF Studio (implémentation) | Les deux documents existent indépendamment et ne se référencent que dans une direction |
| 5 | Définir le contrat minimal d'une entrée KB valide (schéma YAML + champs obligatoires) | Une entrée KB produite par un agent différent est interopérable avec le reste de la KB |
| 6 | Proposer le standard à un premier pair externe pour revue | La première validation externe est documentée dans la KB |

---

## 10. La formule

CertiFi est une méthode pour transformer des résultats quantitatifs en affirmations défendables, par une certification en couches dont chaque niveau est indépendamment testable, versionné, et délimité.

QAAF KB est la mémoire qui rend cette méthode cumulative plutôt que répétitive.

La norme n'est pas ce qui est certifié. La norme est la méthode de certification. La KB est ce qui garantit que la méthode n'a pas à être réinventée à chaque session.

---

*CertiFi Vision Specification v0.2.0 — Avril 2026*  
*Produit après analyse critique adversariale de la conversation de co-construction*  
*Contributeurs : Andrei, Claude (Sonnet 4.6)*  
*QAAF Studio 3.0 est la première brique de la première itération de cette vision.*
