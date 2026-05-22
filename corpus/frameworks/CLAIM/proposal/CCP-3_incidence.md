# CCP-3 — Incidence de la solution proposée
**Version** : 1.1 — 16 mai 2026
**Statut** : FINAL — prêt pour saisie portail PID
**Corps formulaire** : ~2 790 caractères (sans retours de ligne)

---

## PARTIE A — Corps formulaire (≤ 2 950 caractères)

Le défi de la fusion ISR hétérogène est un défi de langage. Sans format d'échange commun entre agents spécialisés et orchestrateur, aucune architecture de fusion standardisée et certifiable ne peut produire des décisions traçables ou explicables. Le CLAIM est ce langage — la couche zéro sans laquelle toutes les couches supérieures restent dépendantes d'accords ad hoc non certifiables.

L'incidence directe est structurelle. Chaque agent de fusion — radar, SIGINT, EO/IR, texte — peut aujourd'hui être performant mais incapable de déclarer son incertitude dans un format que l'orchestrateur peut traiter sans accéder à ses mécanismes internes. Le CLAIM résout ce problème : un agent qui respecte le contrat expose sa masse de croyance sur 2^Theta, son statut illocutionnaire (OBSERVE, INFER, DEDUCE, ASSUME), son horodatage de validité et sa provenance tracée PROV-O. L'orchestrateur reçoit des contributions comparables sans dépendre de l'architecture interne de chaque agent. Cette propriété est la condition nécessaire à toute certification (DO-178C, IEC 61508) : un système dont les interfaces ne sont pas spécifiées ne peut pas être audité.

La composabilité hiérarchique démultiplie l'incidence. Un EPISTEMIC_STATE produit par un orchestrateur tactique peut devenir un CLAIM entrant pour un orchestrateur opérationnel, sans redéfinir le protocole. Une force peut ainsi construire des architectures distribuées à plusieurs niveaux sur la même spécification. L'interopérabilité avec les alliés en bénéficie directement.

L'incidence sur les cinq résultats souhaités est celle d'un prérequis structurel. Pour la propagation de l'incertitude (résultat 1), le CLAIM fournit le format unifié — sans lui, les sources hétérogènes ne peuvent être combinées de façon cohérente. Pour le suivi persistant (résultat 2), l'hypothèse de travail (DEC-S2-08 : alignement spatio-temporel C-02 et résolution d'entités C-03 résolus en amont) montre que leur résultat n'est exploitable que s'il est exprimé en CLAIM bien formé. Pour la traçabilité et la politique d'accès (résultat 3), la provenance PROV-O et le champ illocutionnaire permettent un filtrage par niveau de classification et une chaîne d'audit du capteur à la décision. Pour l'explicabilité temps réel (résultat 4), l'EPISTEMIC_STATE avec état Belnap expose le désaccord et son origine à l'opérateur. Pour le déploiement en périphérie (résultat 5), le CLAIM stateless est exécutable sur matériel embarqué léger.

L'incidence transversale est celle d'une spécification adoptable par tout pipeline de fusion multimodale — défense, sécurité publique, infrastructure critique — sans modifier les agents existants.

Hypothèse de travail (DEC-S2-08) : l'alignement spatio-temporel (C-02) et la résolution d'entités (C-03) sont supposés résolus en amont.

---

## PARTIE B — Annexe GitHub (hors formulaire PID)

**Références**
- Steinberg et al. (1999) — Revisions to the JDL Data Fusion Model
- W3C PROV-O (2013) — traçabilité provenance
- Belnap (1977) — états épistémiques quatre valeurs
- Dezert et Smarandanche — PCR5, localisation du conflit
- DO-178C / IEC 61508 — certification, auditabilité
- DEC-S2-06 — stratégie couche zéro
- DEC-S2-08 — hypothèse C-02/C-03 amont
