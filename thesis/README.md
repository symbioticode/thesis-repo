# Thèse : Le contrat d'interface épistémique dans les systèmes cognitifs distribués

## Résumé (Abstract)

Cette thèse explore l'émergence d'une architecture cognitive commune au travers de six frameworks développés indépendamment pour répondre à des contraintes opérationnelles de gestion de connaissance, de continuité inter-sessions et de fusion d'informations en temps réel. Nous démontrons que ces systèmes convergent inévitablement vers trois invariants structurels : la séparation émetteur/interpréteur, le cycle de vie épistémique explicite et l'escalade humaine systématique en cas de conflit non résolu. Cette convergence est validée par une comparaison avec des standards industriels et militaires (FDA, NATO, NIH). Nous proposons le "Contrat d'Interface Épistémique" comme formalisation unifiée pour combler le gap entre la connaissance persistante et les agents agissant en temps réel. Une implémentation de référence (MIF-DAL) et une preuve de concept (CLAIM) valident l'efficacité de cette approche pour réduire le bruit de fusion et prévenir les dérives décisionnelles des systèmes multi-agents.

---

## Table des matières

### [Chapitre 0 — Genèse : L’émergence par la contrainte](ch0_genese.md)
*   Une trajectoire non planifiée
*   La chronologie des frameworks (PCCD, RKA, ANAMNÈSE, HALO, SYNAPSE, CLAIM)
*   La découverte des invariants

### [Chapitre 1 — Le problème : Le gap de l'interface épistémique](ch1_probleme.md)
*   L'état de l'art (LLM Wiki, GraphRAG, Graphify)
*   Le modèle JDL comme cartographie du gap
*   L'interface épistémique comme cœur du problème

### [Chapitre 2 — Convergence observée : La preuve empirique](ch2_convergence.md)
*   Les six frameworks : domaines et contraintes
*   Synthèse de la convergence (les 5 champs invariants)
*   Validation externe (FDA 21 CFR Part 11, NATO STANAG 4559, NIH PMC7372873)

### [Chapitre 3 — Formalisation : Le contrat d'interface épistémique](ch3_formalisation.md)
*   L'invariant de séparation épistémique
*   PCCD : La spécification abstraite
*   CLAIM : L'instanciation temps-réel
*   Les ponts non résolus

### [Chapitre 4 — Implémentation de référence : HALO et MIF-DAL](ch4_implementation.md)
*   Le terrain d'expérimentation
*   Résultats quantitatifs et score D-SIG
*   Pathologies observées (Fake Code, Docs-avant-code)

### [Chapitre 5 — Preuve de Concept : Le protocole CLAIM](ch5_poc.md)
*   Scénario A : Le problème de la fusion naïve
*   Scénario B : La solution par le protocole CLAIM
*   Conclusion du PoC

---

**Auteur** : Jules (Agent)
**Supervision** : Andrei (PI)
**Date** : Mai 2026
