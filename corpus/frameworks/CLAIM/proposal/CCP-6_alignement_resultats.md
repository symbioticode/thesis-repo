# CCP-6 — Alignement des résultats souhaités
**Version** : 1.2 — 16 mai 2026
**Statut** : FINAL — prêt pour saisie portail PID
**Corrections** : CORR-CCP6-01 (intitulés verbatim AP), CORR-CCP6-02 (liste narrative), CORR-CCP6-03 (recalibrage portail)
**Corps formulaire** : ~2 568 caractères (avec retours de ligne — comptage portail PID)

---

## PARTIE A — Corps formulaire (≤ 2 950 caractères, comptage avec retours de ligne)

Les cinq résultats souhaités requièrent qu'un orchestrateur combine les sorties d'agents hétérogènes. Sans format d'échange standardisé, chaque résultat reste dépendant d'une intégration ad hoc non certifiable. Le CLAIM est ce format — la couche zéro sans laquelle aucune architecture de fusion ne peut être rendue auditable.

Résultat 1 — Architectures avancées pour la propagation de l'incertitude et l'évaluation de la confiance entre modalités. Le CLAIM fournit le format unifié : belief_mass (TBM de Smets, m(vide) conservé) exprime la croyance de chaque agent sur 2^Theta, ignorance résiduelle incluse. Sans ce format, les masses hétérogènes ne peuvent être combinées de façon cohérente. Hors périmètre : alignement spatio-temporel (C-02), supposé résolu en amont (DEC-S2-08).

Résultat 2 — Résolution d'entités et suivi persistant entre domaines. Le CLAIM reçoit des propositions sur des entités déjà résolues (DEC-S2-08). La provenance PROV-O trace la chaîne de traitement de chaque proposition. Hors périmètre : l'algorithme de résolution d'entités (NMT 4-5).

Résultat 3 — Fusion tenant compte des politiques, provenance IA, traçabilité complète entre niveaux de classification. Le champ illocution distingue mesure physique et inférence sans accéder aux mécanismes internes de l'agent. La provenance PROV-O constitue une chaîne d'audit du capteur à la décision (DO-178C, IEC 61508). Hors périmètre : la politique d'accès est appliquée par règle explicite (CC-02, Q5/R5), non apprise — choix délibéré de certification.

Résultat 4 — Architecture évolutive temps réel avec résultats explicables pour la confiance des opérateurs. L'EPISTEMIC_STATE expose l'état Belnap, m_combined(vide) et la localisation PCR5 des agents en désaccord. Règle cardinale : si m(vide) dépasse le seuil, toute décision automatique est suspendue. La composabilité hiérarchique — un EPISTEMIC_STATE devient CLAIM entrant pour l'orchestrateur supérieur — rend l'architecture évolutive sans redéfinir le protocole. Hors périmètre : interface C-07 spécifiée mais non implémentée (NMT 4-5).

Résultat 5 — Intégration des contraintes SWaP pour déploiement en périphérie. Le CLAIM est stateless, JSON sous 1 Ko, calcul O(2^|Theta|) avec |Theta| borné à 20 — quelques millisecondes sur ARM Cortex-M. Hors périmètre : optimisation bas niveau pour matériels très contraints (NMT 4-5).

Hypothèse de travail (DEC-S2-08) : alignement spatio-temporel (C-02) et résolution d'entités (C-03) supposés résolus en amont. Sans cette couche zéro, certifiabilité et interopérabilité restent impossibles.

---

## PARTIE B — Annexe GitHub (hors formulaire PID)

**Intitulés verbatim AP (pour vérification)**
1. Architectures avancées d'apprentissage profond pour l'alignement spatio-temporel, la propagation de l'incertitude et l'évaluation de la confiance entre les différentes modalités
2. Résolution d'entités et intégration dynamique de graphes de connaissances pour le suivi persistant d'objets entre différents domaines
3. Fusion tenant compte des politiques, s'appuyant sur un suivi de la provenance basé sur l'IA pour une intégration sécurisée entre les différents niveaux de classification, avec une traçabilité complète
4. Une architecture évolutive pour des pipelines de fusion en temps réel basés sur l'IA dans des environnements opérationnels, incluant des résultats explicables afin de gagner la confiance des opérateurs
5. Intégrer les contraintes liées à la taille, au poids et à la puissance ainsi que les limites de calcul dans les pipelines de fusion destinés au déploiement en périphérie

**Schéma logique de l'argument "couche zéro"**
Prémisse 1 : Les 5 résultats nécessitent qu'un orchestrateur combine des sorties d'agents hétérogènes.
Prémisse 2 : Toute combinaison cohérente exige un format d'échange commun.
Prémisse 3 : Aucun standard existant ne couvre les 5 dimensions simultanément (QO-S2-01, consensus 4/4 IA).
Conclusion : Le CLAIM est un prérequis structurel à tous les 5 résultats.
Nuance : Le CLAIM ne résout pas l'intérieur de chaque résultat — il fournit le conteneur dans lequel le résultat s'exprime et peut être audité.

**Références**
- Smets et Kennes (1994) — TBM, m(vide) conservé
- Belnap (1977) — états épistémiques quatre valeurs
- Dezert et Smarandanche — PCR5, localisation du conflit
- W3C PROV-O (2013) — traçabilité provenance
- DO-178C / IEC 61508 — certification, auditabilité
- Q5/R5 AP6-défi-13 — hybride déterministe + probabiliste
- DEC-S2-06 — stratégie couche zéro nécessaire
- DEC-S2-08 — hypothèse C-02/C-03 amont
- CC-02 — policy-aware hybride
