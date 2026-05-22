# CO-1 — Description de l'activité de R&D (NMT de la solution proposée)
**Version** : 2.1 — 16 mai 2026
**Statut** : FINAL — prêt pour saisie portail PID
**Caractères (sans retours de ligne)** : ~2 500
**Note** : paragraphe NMT migré vers CO-1b (QO-FORM-04 fermé)

---

## Corps formulaire (≤ 3 000 caractères, cible 2 800)

Par « échange épistémique », on entend le partage structuré de ce qu'un système sait, de ce qu'il ignore, et de ce sur quoi il est en désaccord — de sorte qu'un coordinateur humain puisse décider en connaissance de cause.

Les architectures neuro-symboliques hybrides constituent la réponse la plus prometteuse au défi de la fusion multimodale explicable : une couche perceptive apprenante (modèles de langage multimodaux, VLMs, agents spécialisés par modalité) produit des inférences que une couche de raisonnement symbolique combine, arbitre et expose à l'opérateur. Sarker et al. (2021) confirment que cette famille répond aux exigences d'explicabilité et de traçabilité inaccessibles aux modèles monolithiques. Cependant, le même corpus identifie un gap structurel : aucun système de cette famille ne spécifie le protocole d'échange entre ses couches pour des agents hétérogènes distribués. Steinberg et al. (1999), dans leur révision du modèle JDL (référence doctrinale NATO pour la fusion ISR), identifient explicitement l'absence de standards d'interface entre niveaux de fusion comme impediment majeur à l'intégration — JDL est un modèle fonctionnel, pas un modèle de processus. Ce projet comble ce gap.

Le CLAIM est l'unité atomique de ce protocole : message structuré minimal qu'un agent émet pour que l'orchestrateur raisonne sur sa fiabilité sans accéder à son fonctionnement interne. Il porte cinq invariants : contenu propositionnel, fonction de masse de croyance sur 2^Θ (TBM de Smets, m(∅) conservé comme métrique de conflit non normalisé), statut illocutionnaire auto-déclaré (OBSERVE/INFER/DEDUCE/ASSUME), horodatage de validité, et identifiant de provenance PROV-O. L'orchestrateur combine les CLAIMs par règle conjonctive non normalisée, localise les conflits via PCR5, et produit un EPISTEMIC_STATE (état Belnap : vrai/faux/contradiction/silence qualifié) transmis à l'interface humaine. Si m(∅) dépasse un seuil configurable, toute décision automatique est suspendue et le conflit exposé à l'opérateur.

Hypothèse de travail (DEC-S2-08) : le CLAIM reçoit des propositions pour lesquelles l'alignement spatio-temporel (C-02) et la résolution d'entités (C-03) ont été effectués en amont. Cette délimitation définit l'interface d'entrée du protocole et sera inscrite explicitement dans toutes les sections de la proposition. Le livrable est une spécification formelle adoptable par tout pipeline de fusion multimodale — la justification de la trajectoire NMT-2 → NMT-3 est développée dans la section suivante.

---

## Références

- Sarker et al. (2021) — Neuro-Symbolic AI: The 3rd Wave (AI Communications)
- Steinberg et al. (1999) — Revisions to the JDL Data Fusion Model
- Smets & Kennes (1994) — TBM, règle conjonctive non normalisée
- Dezert & Smarandanche — PCR5, localisation des conflits
- Belnap (1977) — états épistémiques quatre valeurs
- Austin (1962), Searle (1969) — Speech Acts, illocution
- W3C PROV-O (2013) — traçabilité provenance
- Q&R AP6-défi-13 Q3/R4 — données synthétiques autorisées
