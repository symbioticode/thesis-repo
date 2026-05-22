# CertiFi — Spécification de Vision v0.1

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

DQF est axomatique parce qu'il s'applique à des propriétés physiques observables des données brutes (cohérence OHLCV, absence de sauts impossibles, alignement temporel), indépendamment de tout modèle ou de toute stratégie. Ces propriétés peuvent être vérifiées sans référence à d'autres composants de l'écosystème.

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
    Périmètre : une fonction Python, ses propriétés statistiques, son comportement sur données synthétiques et réelles

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

## 7. Recommandations pour étoffer le concept

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

## 8. Feuille de route contrainte

Les priorités sont ordonnées par leur impact sur la **falsifiabilité du projet**, pas par leur visibilité ou leur facilité d'implémentation.

| Priorité | Action | Critère de succès |
|----------|--------|-------------------|
| 1 | Publier `mif-dqf` avec spécification complète des checks CORE et ADVISORY | Un utilisateur tiers peut reproduire un verdict DQF sur ses propres données |
| 2 | Définir le format de rapport CertiFi (YAML) pour les 4 composants | Les rapports produits par des implémentations indépendantes sont interopérables |
| 3 | Documenter un cas d'échec complet de chaque composant (données réelles qui échouent DQF, métrique qui échoue MIF, etc.) | La spécification est testée adversarialement par des cas réels |
| 4 | Séparer formellement la spécification CertiFi (standard) de QAAF Studio (implémentation) | Les deux documents existent indépendamment et ne se référencent que dans une direction |
| 5 | Proposer le standard à un premier pair externe (académique ou praticien) pour revue | La première validation externe est documentée dans la KB |

---

## 9. La formule

CertiFi est une méthode pour transformer des résultats quantitatifs en affirmations défendables, par une certification en couches dont chaque niveau est indépendamment testable, versionné, et délimité.

La norme n'est pas ce qui est certifié. La norme est la méthode de certification.

---

*CertiFi Vision Specification v0.1.0 — Avril 2026*
*Produit après analyse critique adversariale de la conversation de co-construction*
