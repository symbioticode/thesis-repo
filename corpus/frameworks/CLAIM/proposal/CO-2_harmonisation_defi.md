# CO-2 — Harmonisation de la solution proposée avec le défi IDEeS
**Version** : 3.2 — 17 mai 2026
**Statut** : FINAL — prêt pour saisie portail PID
**Corps formulaire** : ~2 445 caractères (avec retours de ligne — comptage portail PID)

---

## PARTIE A — Corps formulaire (≤ 2 950 caractères, comptage avec retours de ligne)

Le résultat essentiel du défi exige un modèle d'IA capable de fusionner au moins deux modalités hétérogènes. Cette exigence est satisfaite par l'architecture neuro-symbolique hybride proposée : les agents spécialisés par modalité constituent la couche de fusion apprenante, et le protocole d'échange épistémique — dont le CLAIM est l'unité atomique — standardise les sorties de ces agents pour que l'orchestrateur puisse les combiner de façon cohérente, traçable et certifiable. La démonstration analytique sur données synthétiques (radar + SIGINT, scénario S-01) satisfait le critère éliminatoire sans données classifiées (Q3/R4).

Le défi 13 demande la fusion de données multimodales hétérogènes pour des décisions explicables et traçables. Ce projet adresse la couche sans laquelle cette fusion ne peut pas être rendue explicable : le contrat d'interface entre agents spécialisés et orchestrateur. Les systèmes ISR actuels produisent des sorties incomparables — probabilités sur des échelles différentes, silences ambigus entre absence de détection et capteur non consulté. L'orchestrateur manque du langage pour combiner ces sorties de façon cohérente. Le CLAIM est ce langage : unité atomique du protocole portant confiance quantifiée, provenance traçable, statut illocutionnaire et silence qualifié.

Le projet s'aligne sur quatre exigences du défi : (1) fusion d'au moins deux modalités hétérogènes, démontrée analytiquement sur données synthétiques ; (2) explicabilité via l'EPISTEMIC_STATE avec localisation PCR5 de l'origine des conflits ; (3) traçabilité par chaîne de provenance W3C PROV-O du capteur à la décision ; (4) approche hybride déterministe et probabiliste conforme à Q5/R5.

L'architecture neuro-symbolique hybride retenue — agents experts apprenants alimentant un orchestrateur symbolique déterministe (TBM+AGM+PCR5) — comble le gap d'interface entre niveaux de fusion que le modèle JDL (référence doctrinale NATO) reconnaît sans résoudre : Steinberg et al. (1999) identifient explicitement l'absence de standards d'interface comme impediment majeur à l'intégration. Le déterminisme de l'orchestrateur est une exigence de certification (DO-178C, IEC 61508), non une lacune.

Hypothèse de travail (DEC-S2-08) : l'alignement spatio-temporel (C-02) et la résolution d'entités (C-03) sont supposés résolus en amont. Trajectoire : NMT-2 (spécification formelle), NMT-3 en six mois (validation sur données synthétiques).

---

## PARTIE B — Annexe GitHub (hors formulaire PID)

**Références**
- Q3/R4 AP6-défi-13 — données synthétiques autorisées
- Q5/R5 AP6-défi-13 — hybride déterministe + probabiliste
- Steinberg et al. (1999) — Revisions to the JDL Data Fusion Model
- W3C PROV-O — traçabilité
- DO-178C / IEC 61508 — certification
- DEC-S2-08 — hypothèse C-02/C-03 amont

**Note vocabulaire (DEC-S4-02)**
- "Le CLAIM" = unité atomique d'échange (structure de données)
- "Le protocole d'échange épistémique" = l'ensemble des règles d'émission, validation, combinaison et escalade
- "Le contrat d'interface" = l'engagement formel entre émetteur et orchestrateur
- "La spécification" = le document formalisant le protocole
- Ne pas écrire "le protocole CLAIM" — écrire "le CLAIM, unité atomique du protocole d'échange épistémique"

**Note marge**
Marge ~505 chars disponible. Option : ajouter la composabilité hiérarchique
(EPISTEMIC_STATE → CLAIM entrant pour orchestrateur supérieur) si l'évaluateur
valorise l'aspect évolutivité dès CO-2.
