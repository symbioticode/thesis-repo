# Chapitre 1 — Le problème : Le gap de l'interface épistémique

## 1.1 L'état de l'art et ses limites

Pour comprendre le problème que nous adressons, il est nécessaire d'analyser les systèmes actuels de gestion de connaissance assistés par IA. Trois approches dominent le paysage, chacune résolvant une partie de l'équation mais laissant un vide critique.

### 1.1.1 LLM Wiki (Approche Documentaire)
Inspiré par les travaux d'Andreï Karpathy sur la maintenance de corpus par LLM, ce système utilise des agents pour structurer et mettre à jour un wiki.
*   **Ce qu'il résout** : La propreté du corpus et la synthèse de documents.
*   **Ce qu'il laisse ouvert** : L'absence de mémoire inter-sessions et de statuts épistémiques. Le wiki est une "photo" statique de la connaissance. Il n'y a pas de distinction entre une hypothèse fragile et une certitude validée, ni de mécanisme pour porter le contexte de compréhension d'une session à l'autre.

### 1.1.2 GraphRAG (Approche Structurelle)
Le GraphRAG de Microsoft Research combine la recherche vectorielle avec des graphes de connaissances extraits.
*   **Ce qu'il résout** : La capacité à répondre à des questions globales en synthétisant des communautés de nœuds dans le graphe.
*   **Ce qu'il laisse ouvert** : L'absence de ce que nous nommons la "Couche 2" (mémoire IA). GraphRAG traite les données comme des objets froids. Il ne détecte pas le "drift" sémantique (quand la signification d'un terme évolue silencieusement entre deux modèles ou deux époques) et ne possède pas de notion de provenance épistémique granulaire.

### 1.1.3 Graphify (Approche Inférentielle)
Graphify se concentre sur l'extraction automatique de graphes à partir de documents textuels via des LLM.
*   **Ce qu'il résout** : L'automatisation de la création de structures.
*   **Ce qu'il laisse ouvert** : Le problème de la sémantique inférée. Les arêtes du graphe sont dérivées par le modèle au moment de l'extraction. Si le modèle change, la sémantique des relations change sans que le système ne s'en aperçoive. Il manque un contrat d'interface où le producteur de l'information déclare ses propres relations (provenance).

## 1.2 Le modèle JDL comme cartographie du gap

Le modèle JDL (Joint Directors of Laboratories), standard historique de la fusion de données, définit plusieurs niveaux de fusion : du Niveau 0 (données brutes) au Niveau 4 (gestion du processus).

En projetant les systèmes existants sur cette cartographie, nous observons un gap systématique. Les systèmes actuels opèrent soit au niveau de la connaissance persistante (Niveau 2/3 : fusion d'objets et de situations), soit au niveau de l'agent en temps réel (Niveau 1 : détection et suivi).

Le **chaînon manquant** est l'interface entre ces deux mondes. Comment une assertion produite par un agent en temps réel (un "CLAIM") peut-elle être intégrée de manière certifiée dans un système de connaissance persistante (RKA) sans perdre sa nuance épistémique ?

## 1.3 L'interface épistémique : le cœur du problème

Le gap commun à LLM Wiki, GraphRAG et Graphify peut être résumé en une question : **quel est le contrat d'interface entre la connaissance et l'agent qui agit dessus ?**

Aujourd'hui, l'agent "lit" le document et "devine" sa pertinence. Il n'y a pas de protocole où le document émet un signal de sa propre vitalité et de son statut. Cela crée trois tensions majeures :

1.  **Le bruit de la fusion** : Sans statut explicite, les systèmes combinent aveuglément des informations contradictoires, produisant des résultats "moyens" mais faux, avec une haute confiance apparente.
2.  **L'amnésie de session** : L'incapacité à transmettre l'état de l'interprète (l'IA) d'une session à l'autre oblige à des reconstructions constantes de contexte.
3.  **L'indécidabilité des conflits** : En l'absence d'un cadre formel pour mesurer le conflit (comme le m(∅) du Transferable Belief Model), les systèmes ne savent pas quand s'arrêter et demander l'arbitrage humain.

Le problème n'est donc pas la quantité de données, ni la puissance des modèles de langage, mais l'absence d'un **contrat d'interface épistémique**. C'est ce vide que cette thèse se propose de combler en formalisant les invariants observés lors de la convergence de nos six frameworks.
