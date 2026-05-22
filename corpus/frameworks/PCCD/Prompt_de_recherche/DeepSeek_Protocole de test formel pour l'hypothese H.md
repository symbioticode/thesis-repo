### Protocole de test formel pour l'hypothèse d'universalité du pattern structurel tridimensionnel

**Objet** : Tester l'hypothèse H selon laquelle *tout système de gestion de connaissance cohérent présente invariablement les neuf composantes du pattern tridimensionnel (3 couches spatiales × 3 états temporels × 3 modes de lecture)*.

**Principe directeur** : Le protocole est conçu pour être exécuté par un tiers n'ayant aucune connaissance préalable de l'hypothèse H, à partir d'une spécification opérationnelle complète.

---

## Composante 1 — Opérationnalisation en variables mesurables et observables

Chaque dimension du pattern doit être traduite en critères observables binaires (présent/absent) sans ambiguïté. La procédure d'observation est normée pour garantir la reproductibilité.

### 1.1 Opérationnalisation des couches spatiales

**Définition opérationnelle préalable** : On appelle *couche* un sous-ensemble identifiable et fonctionnellement distinct de l'architecture du système, dont la fonction principale est le traitement de l'information selon une relation spécifique à l'espace de connaissance.

| Couche | Définition opérationnelle | Indicateurs de présence (tous nécessaires) | Indicateurs d'absence (un seul suffit) |
|--------|---------------------------|--------------------------------------------|---------------------------------------|
| **Locale** | Sous-système ou module gérant des informations dont le périmètre d'action est strictement interne au système, sans référence à une source externe ni à une interaction entre sources. | 1. Existence d'un stockage ou traitement portant sur des entités définies *uniquement par le système lui-même* (ex. identifiants internes, règles de normalisation endogènes).<br>2. Aucun mécanisme de synchronisation ou d'import depuis une source externe pour cette couche.<br>3. Les modifications dans cette couche n'affectent pas d'autres couches directement (absence d'effet de bord). | Le système ne possède aucune donnée qui ne soit pas issue d'une source externe ou d'une interaction entre sources. |
| **Distante** | Sous-système ou module dont la fonction exclusive est l'import, l'export ou la projection d'informations depuis/vers une source extérieure au système, sans traitement structurel interne. | 1. Présence d'interfaces documentées (API, connecteurs, parseurs) vers des systèmes externes.<br>2. Les données traitées dans cette couche conservent leur identifiant ou schéma d'origine externe.<br>3. Aucune fusion ou résolution de conflits avec d'autres sources n'y est effectuée (fonction de simple transit). | Le système n'échange jamais d'information avec l'extérieur (système clos) OU les échanges sont immédiatement fusionnés sans passer par une couche dédiée. |
| **Interférente** | Sous-système ou module dédié à la résolution des conflits, à la fusion, ou à l'alignement sémantique entre au moins deux sources d'information distinctes (internes et/ou externes). | 1. Présence d'algorithmes de *record linkage*, de résolution d'entités, de gestion de versions concurrentes ou de détection de doublons entre sources.<br>2. La couche produit une nouvelle entité informationnelle (ex. "vue consolidée", "identifiant pivot") qui n'existe dans aucune des sources originales.<br>3. Un log ou une trace de décision de fusion est présent. | Le système gère plusieurs sources mais les traite de manière cloisonnée sans jamais tenter de les réconcilier en une représentation unique. |

**Protocole d'observation spatial** :
1. Auditer l'architecture documentée du système (diagrammes de flux de données, documentation technique).
2. Si la documentation est absente ou insuffisante, analyser le code source (si disponible) ou interroger l'administrateur système à l'aide du questionnaire standardisé en Annexe A (non reproduit ici).
3. Coder chaque couche comme **Présente** (tous les indicateurs positifs) ou **Absente** (au moins un indicateur négatif).

### 1.2 Opérationnalisation des états temporels

**Définition opérationnelle** : Un *état temporel* est défini par la fenêtre de temps pendant laquelle l'information est considérée comme pertinente pour l'action ou la requête principale du système.

| État | Définition opérationnelle | Indicateurs de présence | Indicateurs d'absence |
|------|---------------------------|-------------------------|-----------------------|
| **Passé lointain** | Ensemble d'informations explicitement archivées, compressées ou placées dans un stockage "froid", avec une politique de rétention définie et une latence d'accès significativement plus élevée que les données courantes. | 1. Politique de *tiered storage* (ex. migration vers bande ou cloud archive).<br>2. Interface de requête distincte (ex. "archive search", "historical reports").<br>3. Métadonnée indiquant la date d'obsolescence ou de mise en archive. | Le système ne conserve pas les données au-delà de leur durée d'utilisation active immédiate (purge sans archive). |
| **Passé proche** | Ensemble d'informations disponibles en lecture rapide et accessibles en ligne, mais dont la date de validité ou de création est antérieure à l'instant présent de traitement. | 1. Capacité à interroger l'état du système à une date précise antérieure (fonction *point-in-time recovery* ou *time travel*).<br>2. Existence d'un journal de modifications (*changelog*, *audit trail*) accessible en temps réel.<br>3. Ces données sont requêtables conjointement avec les données présentes. | Le système ne conserve que l'état le plus récent (*last write wins* sans historique accessible). |
| **Présent** | État actif du système, modifiable en temps réel, sur lequel portent les transactions courantes. | 1. Présence d'une zone de travail ou d'une table "live" en cours de mise à jour.<br>2. Les verrous transactionnels ou mécanismes de cohérence forte y sont appliqués.<br>3. L'horodatage correspond à la dernière transaction validée. | Le système est strictement en lecture seule (*append-only* ou archive pure sans capacité de modification courante). |

**Protocole d'observation temporel** :
1. Tester les capacités de requête du système : exécuter une requête retournant l'état à `T-1 jour` (passé proche) et une requête retournant l'état à `T-365 jours` (passé lointain).
2. Vérifier si ces requêtes sont techniquement possibles et si le temps de réponse est cohérent avec la latence attendue pour l'état correspondant.
3. Coder chaque état comme **Présent** ou **Absent**.

### 1.3 Opérationnalisation des modes de lecture

**Définition opérationnelle** : Un *mode de lecture* est une interface ou une représentation structurée distincte de l'information, identifiable par le type de requête qu'elle supporte.

| Mode | Définition opérationnelle | Indicateurs de présence | Indicateurs d'absence |
|------|---------------------------|-------------------------|-----------------------|
| **Narratif** | Présentation de l'information sous forme de séquence linéaire temporelle ou causale, avec un début et une fin explicites. | 1. Fonctionnalité de type "journal d'événements", "historique chronologique", "flux d'activité" (*audit log* textuel).<br>2. Possibilité de parcourir "l'histoire" d'une entité étape par étape.<br>3. L'interface restitue un texte lisible ou une frise chronologique. | Le système ne présente jamais les données sous forme de séquence temporelle ; l'information est uniquement agrégée ou statique. |
| **Vectoriel** | Capacité à retrouver des informations par similarité, analogie ou distance dans un espace latent ou catégoriel, sans recourir à un identifiant exact ou une structure hiérarchique prédéfinie. | 1. Présence d'une fonction de recherche sémantique, de recommandation (*similar items*) ou de clustering non supervisé.<br>2. Le système fournit un score de pertinence ou de distance pour des éléments non liés par une relation explicite.<br>3. Utilisation de techniques comme TF-IDF, embeddings, *k-NN*. | La recherche se limite aux correspondances exactes (SQL exact match) ou à la navigation dans un arbre de catégories prédéfini. |
| **Structuré** | Navigation explicite via un schéma, une ontologie, un graphe de relations typées ou une hiérarchie de dossiers fixe. | 1. Présence d'un explorateur d'objets par type/relation.<br>2. Possibilité de formuler une requête formelle de type *pattern matching* sur le schéma (ex. "trouver tous les nœuds de type X reliés à Y").<br>3. Le schéma est visible et interrogeable par l'utilisateur ou l'API. | Le système est un *flat file* ou un magasin clé-valeur sans relations explicites entre entités. |

**Protocole d'observation des modes** :
1. Tester l'interface utilisateur ou l'API.
2. Tenter d'obtenir une séquence temporelle (narratif).
3. Tenter une requête de similarité (vectoriel).
4. Tenter une requête relationnelle sur le schéma (structuré).
5. Coder chaque mode **Présent** ou **Absent** selon les résultats.

---

## Composante 2 — Critères de réfutation

Pour qu'un test soit scientifique, les conditions de réfutation de H doivent être spécifiées *a priori*. Un système examiné constitue une réfutation de H si et seulement si **il satisfait la définition d'un système de gestion de connaissance cohérent ET il présente au moins une des neuf composantes absente.**

### 2.1 Critère d'inclusion dans la classe "système de gestion de connaissance cohérent" (préalable à l'évaluation de H)

Avant de vérifier la présence du pattern, il faut s'assurer que le système testé appartient bien à la catégorie visée par l'hypothèse. Un système est qualifié de **Système de Gestion de Connaissance Cohérent (SGCC)** si et seulement si il vérifie les trois conditions minimales suivantes :

- **Cohérence fonctionnelle** : Le système a pour objectif déclaré la collecte, l'organisation, le stockage et la restitution d'informations destinées à la prise de décision ou à la production de savoir.
- **Cohérence logique interne** : Le système applique des règles de validation ou des contraintes d'intégrité garantissant que deux requêtes identiques dans des conditions identiques retournent des résultats non contradictoires.
- **Pérennité de l'information** : Le système est conçu pour conserver l'information au-delà d'une session unique ou d'un traitement jetable.

*Si un système ne satisfait pas ces trois prérequis, il n'appartient pas au domaine de validité de H et son examen est exclu du test.*

### 2.2 Critères de réfutation stricte de H

**H est réfutée si et seulement si** :
> Un observateur indépendant, appliquant strictement le protocole d'observation de la Composante 1, établit qu'au sein d'un **SGCC** (défini en 2.1), **au moins une des neuf variables binaires suivantes est codée comme ABSENTE :** `Locale`, `Distante`, `Interférente`, `Passé Lointain`, `Passé Proche`, `Présent`, `Narratif`, `Vectoriel`, `Structuré`.

La réfutation est **unitaire** : un seul SGCC présentant une seule absence d'une des neuf composantes suffit à falsifier l'affirmation "tout système présente invariablement les neuf".

**Exemple de scénario de réfutation concret** :
> *Observation* : Le système "Gestionnaire de Fichiers Versionnés de l'Entreprise X" (SGCC validé) ne dispose pas de recherche vectorielle (mode Vectoriel absent). Il possède les huit autres composantes.
> *Conclusion* : H est **réfutée**.

### 2.3 Critère de non-applicabilité (Sauvegarde méthodologique)

Pour éviter l'écueil du "No True Scotsman", tout argument visant à disqualifier un SGCC constaté comme contre-exemple *a posteriori* est rejeté par principe. La seule exception concerne la **non-cohérence** du système. Si un contre-exemple apparent est un SGCC mais que sa documentation révèle une incohérence logique majeure (ex. base de données corrompue acceptant deux états contradictoires simultanément), il doit être exclu **avant** le test, sur la base du critère 2.1, et non après l'observation de l'absence du pattern.

---

## Composante 3 — Plan d'échantillonnage visant la falsification

L'objectif n'est pas de confirmer H là où on l'attend (ce qui renforcerait le biais de confirmation), mais de maximiser la probabilité de trouver un contre-exemple si H est fausse.

### 3.1 Stratégie d'échantillonnage adversariale

Le principe est de sélectionner des domaines et des systèmes qui, structurellement, sont les plus susceptibles de violer l'hypothèse en raison de leur nature minimaliste, de leur ancienneté ou de leur spécialisation extrême.

**Critères de sélection prioritaire des systèmes à tester :**

1.  **Systèmes pré-numériques ou archaïques** : Si H est réellement universelle, elle doit se vérifier dans des systèmes analogiques ou anciens. Priorité aux archives papier, aux bibliothèques traditionnelles (classification Dewey sans informatique), aux systèmes de comptabilité manuelle en partie double.
    - *Raison* : Ces systèmes n'ont pas été conçus avec les concepts modernes d'architecture logicielle qui pourraient avoir influencé les 5 cas initiaux.

2.  **Systèmes minimalistes et contraints** : Systèmes dont la fonction est extrêmement réduite et qui pourraient se passer d'une des couches.
    - Exemples : un simple fichier `README.md` dans un projet Git (SGCC ? non, car pas de pérennité au-delà de l'édition). Un **Wiki personnel statique** (sans historique de modification accessible). Un **Agenda papier**.
    - *Raison* : Si un système minimal remplit la fonction de "gestion de connaissance" sans avoir développé les trois couches spatiales (par exemple, pas de couche interférente car une seule source), H est falsifiée.

3.  **Systèmes hautement spécialisés en temps réel** : Systèmes de trading algorithmique, systèmes de supervision réseau.
    - *Raison* : La composante "Passé lointain" (archive froide) est souvent absente ou négligée dans les systèmes orientés flux. Si un superviseur réseau ne garde que 7 jours de logs sans archive (purge automatique), le "Passé lointain" est absent.

4.  **Systèmes purement relationnels stricts** : Bases de données SQL brutes sans couche applicative.
    - *Raison* : La composante "Vectoriel" (similarité) nécessite une surcouche spécifique. Une base de données relationnelle standard n'offre pas nativement le mode vectoriel sans extension (pgvector) ou application externe. Si le SGCC est "la base de données de production de l'ERP", le mode vectoriel est probablement absent.

### 3.2 Taille et composition de l'échantillon de test

Étant donné que la recherche d'universalité exige une absence de contre-exemple, le protocole préconise une stratégie **séquentielle avec règle d'arrêt**.

**Échantillon initial N=20 (hors corpus initial des 5)**

- **Groupe A (Ancien/Analogique)** : 5 systèmes (ex: Classification de la Bibliothèque du Congrès, un système de fiches Bristol de médecin de 1970, un registre d'état civil manuscrit).
- **Groupe B (Minimal/Outils personnels)** : 5 systèmes (ex: un Zettelkasten papier, un fichier Markdown unique dans un éditeur de texte, un tableau Excel sans macros ni relations).
- **Groupe C (Industriel/Spécialisé)** : 5 systèmes (ex: un logiciel de GMAO, un serveur de logs SNMP sans archivage, une base de données de capteurs IoT à fenêtre glissante).
- **Groupe D (Contrôle aléatoire)** : 5 systèmes tirés au sort parmi les logiciels de gestion de connaissance répertoriés sur Wikipedia (hors ceux déjà connus).

**Procédure de test** : Chaque système est évalué indépendamment par deux observateurs (fiabilité inter-juges). Un système est considéré comme **Testé** uniquement si les deux observateurs s'accordent sur le codage binaire des 9 variables.

---

## Composante 4 — Seuil de validation et distinction universalité/biais

L'universalité ("tous les X ont la propriété P") est une affirmation logique extrêmement forte qui ne peut être prouvée inductivement par simple énumération. Nous définissons donc un seuil pragmatique de **non-réfutation robuste**.

### 4.1 Critère logique d'arrêt des tests

La recherche de contre-exemples s'arrête dans deux cas :

1.  **Arrêt pour réfutation** : Dès qu'un premier SGCC valide présente une absence de composante. **Conclusion formelle : H est fausse.**
2.  **Arrêt pour saturation de l'effort de falsification** : Après avoir testé les 20 systèmes définis en 3.2 sans trouver de contre-exemple.

### 4.2 Distinction "Universalité probable" / "Biais de confirmation"

Pour distinguer une propriété réelle d'un artefact dû à un échantillon trop restreint ou biaisé, on applique la **Règle des Sous-Classes Opposées (RSO)** :

> **RSO** : H ne peut être considérée comme "universelle probable" que si et seulement si la totalité des systèmes du **Groupe B (Minimal/Outils personnels)** et du **Groupe A (Ancien/Analogique)** présentent **exhaustivement** les neuf composantes.

**Justification épistémologique** :
- Le corpus initial (5 cas) est constitué de systèmes modernes, complexes et conçus par des ingénieurs (supervision réseau, IA, finance).
- Si H est un biais de conception moderne ou un platonisme projeté par l'analyste, elle **échouera très probablement** sur le Groupe B (systèmes trop simples pour avoir développé la couche interférente ou le mode vectoriel) ou sur le Groupe A (systèmes trop anciens pour avoir conceptualisé l'archive "lointaine" distincte du "proche").
- Si, contre toute attente, un fichier Excel personnel ou un registre paroissial de 1850 exhibe les neuf couches/modes (par exemple, le mode vectoriel serait la recherche approximative dans l'index, le mode narratif la lecture chronologique des actes), alors l'hypothèse acquiert une **résistance à la falsification** qui dépasse le biais de confirmation trivial.

### 4.3 Conclusion du protocole

| Résultat | Interprétation formelle |
|----------|-------------------------|
| **Au moins 1 absence trouvée dans les 20 tests** | **H est réfutée**. Le pattern n'est pas universel. |
| **Aucune absence dans les 20 tests, y compris les Groupes A et B** | **H est robuste à la falsification minimale**. On peut parler de *"propriété invariante observée dans un échantillon diversifié incluant des cas adversariaux"*. L'universalité au sens strict ("tout") reste non prouvée mais l'hypothèse est **soutenue** comme guide d'architecture. |
| **Absence trouvée uniquement dans le Groupe B (Minimal)** | **H est falsifiée**, mais cela révèle une **condition limite** : le pattern n'émerge que dans les systèmes dépassant un certain seuil de complexité. L'hypothèse d'universalité stricte est fausse ; une hypothèse plus faible ("tout système au-delà de la complexité K présente le pattern") devient le nouveau sujet d'étude. |

**Recommandation finale pour l'exécution** : Ce protocole est conçu pour être exécuté en aveugle. L'observateur doit ignorer si le système a été choisi pour confirmer ou infirmer la théorie. L'Annexe B du protocole (non jointe ici) fournit la grille de saisie standardisée à utiliser pendant l'audit.