# CCP-1 — Mérite scientifique ou technique de la solution proposée
**Version** : 3.1 — 16 mai 2026
**Statut** : FINAL — prêt pour saisie portail PID
**Caractères (sans retours de ligne)** : ~2 780

---

## Corps formulaire (≤ 3 000 caractères, cible 2 800)

Ce projet synthétise six cadres théoriques éprouvés dans un contrat d'interface unique, inédit pour les systèmes multi-agents ISR hétérogènes.
Transferable Belief Model (Smets, 1990) — La règle conjonctive non normalisée préserve m(∅) comme métrique de conflit explicite, évitant le paradoxe de Zadeh (1979) où la règle classique de Dempster efface le conflit entre agents contradictoires. Dans un contexte ISR, cette contradiction est une information de premier rang.
PCR5/PCR6 (Dezert-Smarandanche) — Identifie quel agent est en désaccord avec quel autre sur quelle hypothèse. Sans cette localisation, l'orchestrateur ne peut pas exposer le conflit à l'opérateur de façon actionnable.
Logique de Belnap à quatre valeurs (1977) — Distingue vrai, faux, contradiction diagnostique (Both) et silence qualifié (Neither). Neither représente « je n'ai pas observé », distinct de « j'ai observé l'absence » — distinction absente de la logique classique, critique en ISR. Belnap est appliqué en sortie de l'orchestrateur (EPISTEMIC_STATE), pas en entrée.
Postulats AGM (Alchourrón, Gärdenfors, Makinson, 1985) — L'orchestrateur n'efface jamais un conflit : il l'expose par révision AGM.
Speech Act Theory (Austin, Searle) — Le champ illocutionnaire du CLAIM (OBSERVE / INFER / DEDUCE / ASSUME) empêche l'orchestrateur d'inférer l'intention de l'émetteur.
Règle prudente de Denœux (2008) — Idempotente (m⊕m=m), évite le double-comptage entre sources corrélées non déclarées.
Ces six cadres s'inscrivent dans la taxonomie des architectures neuro-symboliques hybrides, illustrée par DeepProbLog (Manhaeve et al., 2018) et le Neuro-Symbolic Concept Learner (MIT, 2019). Notre contribution se distingue de ces systèmes intégrés : au lieu de fusionner apprentissage et raisonnement dans un seul modèle, nous définissons l'interface standardisée qui permet à tout agent ML d'opérer dans une architecture distribuée et auditable. Sarker et al. (2021) confirment qu'aucun système neuro-symbolique majeur ne spécifie de protocole d'échange pour architectures distribuées hétérogènes — c'est précisément ce gap que ce projet adresse.
Hypothèse de travail (DEC-S2-08) : alignement spatio-temporel (C-02) et résolution d'entités (C-03) supposés résolus en amont.

---

## Références

- Smets & Kennes (1994) — TBM
- Zadeh (1979) — paradoxe
- Dezert & Smarandanche — PCR5/PCR6
- Belnap (1977) — logique quatre valeurs
- Alchourrón, Gärdenfors, Makinson (1985) — AGM
- Austin (1962), Searle (1969) — Speech Acts
- Denœux (2008) — règle prudente
- Manhaeve et al. (2018) — DeepProbLog
- Sarker et al. (2021) — Neuro-Symbolic AI: The 3rd Wave (AI Communications)
