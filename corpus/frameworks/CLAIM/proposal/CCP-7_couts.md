# CCP-7 — Alignement des coûts de la solution proposée
**Version** : 1.1 — 17 mai 2026
**Statut** : v1.1 — à valider par Andrei (taux horaires et frais indirects institutionnels)
**Corps formulaire** : ~2 623 caractères (avec retours de ligne — comptage portail PID)

---

## PARTIE A — Corps formulaire (≤ 2 950 caractères, comptage avec retours de ligne)

La proposition cible un contrat de 6 mois à 250 000 dollars canadiens, structuré en deux jalons. Les coûts sont dominés par le temps humain de recherche, de spécification et de validation — aucun prototype logiciel déployable n'est requis à NMT 1-3. Les taux horaires sont des estimations à confirmer selon le régime contractuel retenu.

Jalon 1 (mois 1 à 3, 70 % du budget, soit 175 000 dollars). Livrable : spécification formelle du protocole d'échange épistémique, revue de littérature documentant le gap d'interface, et protocole de validation sur données synthétiques.

Poste 1 — Chercheur principal (Andrei) : conception, formalisation mathématique (TBM, PCR5, AGM, Belnap), rédaction de la spécification, coordination. Estimation : 300 heures à 200 dollars = 60 000 dollars.

Poste 2 — Collaborateur technique (Thierry) : revue de littérature, scénarios synthétiques (Python/pyds), schéma JSON Schema. Estimation : 200 heures à 150 dollars = 30 000 dollars.

Poste 3 — Conseiller scientifique (Ebenezer, doctorat en mathématiques) : validation formelle de la spécification, cohérence des fondements DS/Belnap/AGM. Estimation : 100 heures à 200 dollars = 20 000 dollars.

Poste 4 — Accès bases de données académiques (IEEE, ACM, Springer) : 5 000 dollars.

Poste 5 — Infrastructure cloud légère pour scénarios synthétiques S-01 à S-03 (CPU, aucun GPU) : 2 000 dollars.

Poste 6 — Frais généraux (15 % sur main-d'oeuvre) : 16 500 dollars.

Total J1 avant contingence : 133 500 dollars. Contingence 10 % : 13 350 dollars. Sous-total J1 : 146 850 dollars. Complété à 175 000 dollars par frais indirects institutionnels.

Jalon 2 (mois 4 à 6, 30 % du budget, soit 75 000 dollars). Livrable : validation analytique sur données synthétiques, format de log certifiable m(vide) conforme DO-178C/IEC 61508, rapport final et trajectoire NMT 4-5.

Poste 1 — Chercheur principal : validation scénarios S-02/S-03, calibration theta_conflit, rapport final. Estimation : 150 heures à 200 dollars = 30 000 dollars.

Poste 2 — Collaborateur technique : exécution des scénarios, logs, relecture. Estimation : 100 heures à 150 dollars = 15 000 dollars.

Poste 3 — Conseiller scientifique : révision finale de la spécification et du rapport. Estimation : 40 heures à 200 dollars = 8 000 dollars.

Poste 4 — Frais généraux (15 % sur main-d'oeuvre) : 7 950 dollars.

Total J2 avant contingence : 60 950 dollars. Contingence 10 % : 6 100 dollars. Sous-total J2 : 67 050 dollars. Complété à 75 000 dollars par frais indirects institutionnels.

Total : 250 000 dollars canadiens. Contenu canadien : 100 %. Conformité clause A3050T : attestée.

---

## PARTIE B — Annexe GitHub (hors formulaire PID)

### Tableau de ventilation détaillé (vérifié algébriquement — R-CALC-01)

| Poste | J1 (175 k$) | J2 (75 k$) | Total |
|-------|------------|-----------|-------|
| Chercheur principal (300h + 150h × 200 $/h) | 60 000 $ | 30 000 $ | 90 000 $ |
| Collaborateur technique (200h + 100h × 150 $/h) | 30 000 $ | 15 000 $ | 45 000 $ |
| Conseiller scientifique (100h + 40h × 200 $/h) | 20 000 $ | 8 000 $ | 28 000 $ |
| Bases de données académiques | 5 000 $ | — | 5 000 $ |
| Infrastructure cloud (S-01→S-03 / S-04 opt.) | 2 000 $ | — | 2 000 $ |
| Frais généraux (15 % main-d'oeuvre) | 16 500 $ | 7 950 $ | 24 450 $ |
| **Sous-total avant contingence** | **133 500 $** | **60 950 $** | **194 450 $** |
| Contingence (10 % sur total avant cont.) | 13 350 $ | 6 100 $ | 19 450 $ |
| Frais indirects institutionnels | 28 150 $ | 7 950 $ | 36 100 $ |
| **Total jalon** | **175 000 $** | **75 000 $** | **250 000 $** |

**Vérification** : 146 850 + 28 150 = 175 000 ✓ — 67 050 + 7 950 = 75 000 ✓

### Hypothèses à valider par Andrei avant commit

[QO-CCP7-01] Taux horaire chercheur principal : 200 $/h estimatif. À confirmer selon régime (contrat personnel, taux NRC, ou autre). 300h J1 = 50h/mois sur 3 mois (~12,5 jours/mois) — compatible avec congé partiel NRC.

[QO-CCP7-02] Taux horaire collaborateur Thierry : 150 $/h estimatif. À confirmer selon régime PI/contrat (ADM-04 ouvert).

[QO-CCP7-03] Taux horaire conseiller Ebenezer : 200 $/h estimatif (doctorat en mathématiques). Accord formel en attente. Si non disponible, profil équivalent à identifier avant J14.

[QO-CCP7-04] Frais indirects institutionnels : 36 100 $ (14,4 % du total). Taux estimatif — à vérifier administration NRC si soumission via entité institutionnelle.

[QO-CCP7-05] Devise CAD — à confirmer dans le formulaire PID.

### Charges horaires par collaborateur

| Collaborateur | J1 | J2 | Total | Durée équivalente |
|---|---|---|---|---|
| Andrei | 300h | 150h | 450h | ~75h/mois — temps partiel (~19j/mois) |
| Thierry | 200h | 100h | 300h | ~50h/mois — temps partiel |
| Ebenezer | 100h | 40h | 140h | ~23h/mois — conseil ponctuel |

### Note sur le régime de travail d'Andrei

300h en J1 sur 3 mois = 100h/mois = ~25 jours/mois. Attention : si taux NRC applicable,
vérifier si les 300h J1 sont compatibles avec un congé partiel ou sans solde. À affiner
dans Sprint 7 (structure d'entreprise et régime PI). Pour l'instant : chiffres cohérents
et dans les limites du contrat. Décision finale avant J14.
