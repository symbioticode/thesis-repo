# CCP-4 — Faisabilité et approche de la solution proposée
**Version** : 1.1 — 16 mai 2026 (correction CORR-CCP4-01)
**Statut** : FINAL — prêt pour saisie portail PID
**Corps formulaire** : ~2 330 caractères (sans retours de ligne)

---

## PARTIE A — Corps formulaire (≤ 2 950 caractères)

La faisabilité repose sur trois piliers : une spécification formelle déjà produite (TP-01 — CLAIM_specification.md v1.1, validée le 16 mai 2026), un plan de validation sur données synthétiques sans dépendance à des données classifiées, et une démonstration que le protocole est calculable sur matériel embarqué léger.

Le plan de validation utilise des données synthétiques, modalité autorisée par Q3/R4. Le scénario de base (S-01) met en jeu deux agents — radar et SIGINT — sur un cadre de discernement Theta à trois hypothèses : objet militaire, objet civil, état inconnu (|Theta| = 3). Les masses : m_radar({H1}) = 0.7, m_radar(Theta) = 0.3 ; m_sigint({H2}) = 0.6, m_sigint(Theta) = 0.4. H1 et H2 étant disjointes, la règle conjonctive non normalisée (TBM de Smets) donne m_combined(vide) = 0.7 x 0.6 = 0.42, supérieur au seuil theta_conflit = 0.3. L'orchestrateur déclenche l'escalade humaine et expose le conflit via PCR5. Ce scénario est reproductible sans infrastructure externe : Python pur avec la librairie pyds, en moins de deux heures. Un scénario étendu à trois agents et quatre hypothèses testera la calibration de theta_conflit et la localisation PCR5 entre paires d'agents.

La calibration de theta_conflit suit la méthode B.2 de la spécification : générer des scénarios synthétiques avec taux de conflit connu, calculer le taux d'escalade pour chaque valeur candidate, retenir le seuil minimisant les faux positifs sous contrainte opérateur. Cette méthode constitue le mécanisme d'apprentissage léger du système — aucun GPU ni dataset classifié requis.

La structure du CLAIM démontre la faisabilité d'implémentation. Le schéma JSON (TP-01b, avant J7) représente un CLAIM en moins de 1 Ko. Le calcul TBM est en O(2^|Theta|) : pour |Theta| = 20, environ un million d'opérations — quelques millisecondes sur ARM Cortex-M. L'orchestrateur est déterministe et stateless. Il peut être colocalisé avec les agents ou réparti sur réseau tactique sans modifier l'interface.

La gestion des CLAIMs malformés est spécifiée en B.1 : masse non normalisée, timestamp absent ou futur, provenance non résolvable, illocution hors énumération — rejet et consignation dans le log de supervision. L'orchestrateur n'infère jamais l'intention d'un CLAIM malformé.

Hypothèse de travail (DEC-S2-08) : alignement spatio-temporel (C-02) et résolution d'entités (C-03) supposés résolus en amont.

Trajectoire : NMT-2 (spécification livrée), NMT-3 en six mois (validation sur données synthétiques).

---

## PARTIE B — Annexe GitHub (hors formulaire PID)

**Références**
- Smets et Kennes (1994) — TBM, règle conjonctive non normalisée
- Q3/R4 AP6-défi-13 — données synthétiques autorisées
- CLAIM_specification.md v1.1 §B.1 (validation entrante) et §B.2 (calibration theta_conflit)
- DEC-S2-08 — hypothèse C-02/C-03 amont
- CORR-CCP4-01 — correction m_combined(vide) = 0.42 (audit DeepSeek + Andrei, 16 mai 2026)

**Note de calibrage**
Corps à 2 330 caractères — marge de ~620 caractères disponible si Andrei souhaite enrichir
avec le détail du scénario S-02 (3 agents, 4 hypothèses) ou la topologie agnostique.
