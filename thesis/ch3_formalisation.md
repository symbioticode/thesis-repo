# Chapitre 3 — Formalisation : Le contrat d'interface épistémique

## 3.1 L'invariant de séparation épistémique

Le principe unificateur de ce travail est l'**invariant de séparation émetteur/interpréteur**. Formulé pour la première fois dans PCCD (INV-01), il stipule qu'un nœud de connaissance ne doit jamais être le juge de son propre état.

Concrètement, un fichier `note.md` ne contient pas la mention "Ceci est important" ou "Ceci est expiré". Ces jugements sont des relations entre l'information et un observateur (humain ou agent) dans un contexte donné. Le fichier se contente d'émettre des faits objectifs (date de création, auteur, domaine, hash). La conclusion épistémique — le statut — est attribuée par l'orchestrateur du système.

Cette séparation résout le paradoxe de l'auto-référence et permet de construire des systèmes robustes où la confiance peut être recalculée dynamiquement sans modifier la source de l'information.

## 3.2 PCCD : La spécification abstraite

Le Protocole de Cohérence Cognitive Distribuée (PCCD) fournit la grammaire de cette formalisation. Il définit trois dimensions orthogonales :

1.  **Dimension spatiale** : Séparation entre la mémoire locale (active), distante (archive) et interférente (liens).
2.  **Dimension temporelle** : Distinction entre le présent (action), le passé proche (continuité) et le passé lointain (référence).
3.  **Dimension d'exécution** : Cascade de lecture à trois niveaux (Niveau 0 : Signal vital, Niveau 1 : Contexte minimal, Niveau 2 : Contenu sémantique).

PCCD est une "physique" de la connaissance. Il ne dit pas *quoi* écrire, mais *comment* l'écrire pour que ce soit observable et réutilisable par n'importe quel agent, présent ou futur.

## 3.3 CLAIM : L'instanciation temps-réel

Si PCCD est la spécification abstraite pour la connaissance persistante, le protocole **CLAIM** en est l'instanciation pour les flux de données en temps réel. Un CLAIM est une unité d'assertion atomique émise par un agent.

L'innovation majeure de CLAIM est l'utilisation du **Transferable Belief Model (TBM)** non normalisé. Dans un système classique, deux assertions contradictoires s'annulent ou produisent une moyenne. Dans CLAIM, la masse de conflit `m(∅)` est conservée et monitorée. Si le conflit dépasse un seuil `θ_conflit`, le système suspend la décision automatique et déclenche une escalade humaine.

C'est ici que le contrat d'interface devient opérationnel : il définit le moment exact où la machine doit passer la main à l'humain, non pas par manque de données, mais par détection formelle de contradiction épistémique.

## 3.4 Les ponts non résolus

Fidèles à notre principe de recherche par contrainte, nous nommons explicitement les gaps que notre formalisation n'a pas encore comblés :

*   **La couche de traduction RKA → CLAIM** : Comment transformer automatiquement une fiche de connaissance persistante (RKA) en une assertion dynamique utilisable par un agent multi-agents (CLAIM) ? Le passage de la structure Markdown/YAML à la masse de croyance TBM reste un processus largement heuristique.
*   **Le pont C1 ↔ C2 de SYNAPSE** : La synchronisation entre le graphe de connaissance structurel (Couche 1) et la mémoire épisodique de l'IA (Couche 2) n'est pas encore automatisée. Le drift sémantique est détectable au niveau 0 (hash), mais sa résolution demande une intervention humaine systématique.
*   **La portabilité des intentions** : Bien que nous ayons formalisé les faits, la capture et la transmission de l'**intention** de l'émetteur (le "pourquoi" derrière le "quoi") restent fragiles et dépendantes de la prose en langage naturel.

Ces gaps ne sont pas des échecs, mais les frontières actuelles de la recherche. Ils définissent la roadmap des futurs travaux sur l'interface épistémique.
