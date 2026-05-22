# CO-1b — Justification NMT état final (NMT-3)
**Version** : 1.0 — 18 mai 2026
**Statut** : FINAL — prêt pour saisie portail PID
**Corps formulaire** : ~2 327 caractères (avec retours de ligne — comptage portail PID)

---

## PARTIE A — Corps formulaire (champ "Justification NMT état final prévu")

La solution proposee atteint le NMT-3 — validation analytique et experimentale en environnement pertinent — par demonstration formelle sur donnees synthetiques, modalite explicitement autorisee (Q3/R4).

Le scenario de validation de reference (S-01) met en oeuvre deux agents specialises, Radar et SIGINT, partageant un cadre de discernement commun Theta = {H1 : objet militaire, H2 : objet civil, H3 : inconnu}. Les masses de croyance initiales sont : m_radar({H1}) = 0.7, m_radar(Theta) = 0.3 ; m_sigint({H2}) = 0.6, m_sigint(Theta) = 0.4. H1 et H2 etant disjointes, la regle conjonctive non normalisee (TBM de Smets) donne m_combined(vide) = 0.7 x 0.6 = 0.42, superieur au seuil theta_conflit = 0.3. L'orchestrateur declenche l'escalade humaine. La localisation PCR5 identifie le conflit comme issu de la paire (Radar, SIGINT) sur les hypotheses H1 et H2. L'EPISTEMIC_STATE produit : belnap_state = B (contradiction diagnostique), conflit expose a l'interface C-07.

Ce resultat est reproductible sans infrastructure externe. Le script de demonstration (zero dependance hors bibliotheque standard) a ete execute et valide les valeurs ci-dessus. Le temps de calcul est inferieur a une milliseconde pour un cadre de taille 3. Pour |Theta| = 20, quelques millisecondes sur processeur ARM standard, compatible avec les contraintes SWaP du Resultat 5.

La validation NMT-3 sur six mois generalise ce scenario en trois etapes. Mois 1 a 2 : extension a trois agents et quatre hypotheses, calibration de theta_conflit selon la methode B.2 de la specification, validation de la politique de rejet des CLAIM malformes (B.1). Mois 3 a 4 : validation de la composabilite hierarchique, un EPISTEMIC_STATE devenant CLAIM entrant pour un orchestrateur de niveau superieur sans modification du protocole. Mois 5 a 6 : rapport de validation analytique et format de log certifiable m(vide) conforme DO-178C et IEC 61508.

L'ensemble est conduit sur donnees synthetiques generees algorithmiquement, sans donnees classifiees ni infrastructure cloud obligatoire.

---

## PARTIE B — Annexe GitHub (hors formulaire PID)

**Note de calibrage**
Corps : 2 327 caractères avec retours de ligne (comptage portail).
Marge disponible : ~473 caractères.
Option : ajouter une phrase sur l'architecture neuro-symbolique hybride si CO-1b
est lu indépendamment de CO-1 par l'évaluateur.

**Références**
- Q3/R4 AP6-défi-13 — données synthétiques autorisées
- CLAIM_specification.md v1.1 §B.1 (validation), §B.2 (calibration theta_conflit)
- CORR-CCP4-01 — m_combined(vide) = 0.42 (correction auditée DeepSeek + Andrei)
- DEC-S2-08 — hypothèse C-02/C-03 amont
- DO-178C, IEC 61508 — certification du log m(vide)
