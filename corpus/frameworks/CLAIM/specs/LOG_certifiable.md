# LOG_certifiable — Format de log certifiable m(∅)
**Référence** : TP-02
**Version** : 1.1 — 18 mai 2026 (correction Session 9bis : 11 champs distincts)
**Auteur** : Claude (instance de session) — validé Andrei (PI)
**Standards** : DO-178C / IEC 61508
**Statut** : LIVRÉ — dans specs/LOG_certifiable.md

---

## 1. Objet

Ce document spécifie le format de journalisation certifiable pour la masse de conflit `m_combined(∅)` produite par l'orchestrateur (couche C-06) à chaque cycle de combinaison TBM non normalisée.

**Exigence fondatrice** : DO-178C §6.3 (Software Output Items) et IEC 61508-3 §7.4.3 (Software Safety Requirements) imposent la traçabilité complète de toutes les décisions susceptibles d'affecter la sécurité fonctionnelle. L'escalade humaine déclenchée par `m(∅) ≥ θ_conflit` est une telle décision.

**Périmètre** : NMT-2 à NMT-3. Couverture NMT 4-5 : ajout de l'horodatage de résolution opérateur et du lien vers le rapport d'incident.

---

## 2. Champs obligatoires — 11 champs distincts

> **Note de correction (Session 9bis)** : le récapitulatif de Session 9 comprimait les champs 6 et 7 sous la notation "m_empty_before/after". Ce sont deux champs distincts. Le fichier livré a toujours contenu 11 champs séparés ; seul le récapitulatif était incorrect.

### Champ 1 — log_id

**Type** : string, UUID v4
**Contrainte** : unique par enregistrement, généré à la création
**Exemple** : `"7f3a2c1e-9b4d-4f8e-a2c1-3d5e7f9b0a2c"`
**Justification DO-178C** : identifiant non ambigu requis pour la traçabilité des artefacts logiciels (§7.2.5)

---

### Champ 2 — timestamp

**Type** : string, ISO 8601 UTC avec précision milliseconde
**Format** : `YYYY-MM-DDTHH:MM:SS.mmmZ`
**Exemple** : `"2026-05-18T14:32:07.443Z"`
**Justification IEC 61508** : horodatage de précision sous-seconde requis pour la reconstruction de séquence d'événements (§7.4.3.1)

---

### Champ 3 — chain_id

**Type** : string, URI conforme W3C PROV-O
**Format** : `urn:idees:chain:{uuid}`
**Exemple** : `"urn:idees:chain:a1b2c3d4-e5f6-7890-abcd-ef1234567890"`
**Justification** : lien vers la chaîne de provenance complète — permet l'audit jusqu'au capteur physique source (CORR-TP01-05)

---

### Champ 4 — lifecycle_transition

**Type** : string, enum
**Valeurs autorisées** :
- `"COMBINING"` — combinaison TBM en cours
- `"COMBINED"` — combinaison terminée, résultat disponible
- `"ESCALATED"` — escalade humaine déclenchée (`m(∅) ≥ θ_conflit`)
- `"RESOLVED"` — résolution opérateur reçue (NMT 4-5)

**Exemple** : `"ESCALATED"`
**Justification DO-178C** : traçabilité des transitions d'état du logiciel (§6.3.1)

---

### Champ 5 — transition_cause

**Type** : string, description lisible
**Contrainte** : non vide si `lifecycle_transition` ∈ {`"ESCALATED"`, `"RESOLVED"`}
**Exemple** : `"m_combined(vide) = 0.4200 >= theta_conflit = 0.3000 — paire conflictuelle : (Radar, SIGINT)"`
**Justification IEC 61508** : cause de chaque transition vers un état de sécurité documentée (§7.4.2)

---

### Champ 6 — m_empty_before

**Type** : float, [0.0, 1.0]
**Précision** : 6 décimales
**Sémantique** : valeur de `m_combined(∅)` **avant** la combinaison du cycle courant (état initial du cycle)
**Exemple** : `0.000000`
**Note** : vaut 0.0 au premier cycle (aucune combinaison préalable)

---

### Champ 7 — m_empty_after

**Type** : float, [0.0, 1.0]
**Précision** : 6 décimales
**Sémantique** : valeur de `m_combined(∅)` **après** la combinaison du cycle courant (résultat de la règle conjonctive non normalisée)
**Exemple** : `0.420000`
**Justification** : c'est cette valeur qui est comparée à `θ_conflit` pour la décision d'escalade

> **Distinction champs 6/7** : m_empty_before capture l'état entrant ; m_empty_after capture le résultat. La différence `m_empty_after - m_empty_before` est le delta de conflit introduit par les CLAIMs du cycle courant — information utile pour la localisation PCR5.

---

### Champ 8 — belnap_state_after

**Type** : string, enum
**Valeurs autorisées** : `"T"` | `"F"` | `"B"` | `"N"`
**Sémantique** :
- `"T"` : accord sur H (True)
- `"F"` : accord sur ¬H (False)
- `"B"` : contradiction active — escalade obligatoire (Both)
- `"N"` : silence qualifié — aucune source n'a observé (Neither)

**Exemple** : `"B"`
**Règle de priorité** : B > N > T/F (CORR-TP01-06)
**Justification** : état épistémique de sortie exposé à l'interface opérateur (C-07)

---

### Champ 9 — combination_rule

**Type** : string, enum
**Valeurs autorisées** :
- `"TBM_CONJUNCTIVE"` — règle conjonctive non normalisée (Smets) — utilisé NMT 2-3
- `"PCR5"` — Proportional Conflict Redistribution 5
- `"PCR6_PLUS"` — variante VBBA-safe (verrou NMT 2, PCA-01)
- `"DEMPSTER_NORMALIZED"` — interdit dans ce système (paradoxe de Zadeh)

**Exemple** : `"TBM_CONJUNCTIVE"`
**Justification DO-178C** : identification de l'algorithme de décision (§6.3.4)

---

### Champ 10 — sil_dal_level

**Type** : string, enum
**Valeurs autorisées** : `"SIL-1"` | `"SIL-2"` | `"SIL-3"` | `"SIL-4"` | `"DAL-A"` | `"DAL-B"` | `"DAL-C"` | `"DAL-D"`
**Exemple** : `"SIL-2"` (NMT 2-3, données synthétiques)
**Justification IEC 61508** : niveau d'intégrité de sécurité applicable à l'enregistrement (§3.5.4)
**Note NMT** : SIL-2 pour NMT 2-3 sur données synthétiques. Révision vers SIL-3/SIL-4 prévue NMT 4-5 sur données réelles.

---

### Champ 11 — integrity_hash

**Type** : string, SHA-256 hex (64 caractères)
**Calcul** : SHA-256 de la concaténation canonique des champs 1 à 10 (JSON sérialisé, clés triées alphabétiquement, sans espaces)
**Exemple** : `"a3f7c2e1b9d4e8f0c1a2b3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4"`
**Justification DO-178C** : intégrité de l'enregistrement vérifiable indépendamment (§7.2.6)
**Note** : le hash couvre les champs 1-10 uniquement (pas lui-même). Recalculable à tout moment pour audit.

---

## 3. Champ informationnel optionnel

### operator_notified

**Type** : boolean
**Sémantique** : indique si l'interface opérateur (C-07) a reçu la notification d'escalade
**Valeur par défaut** : `false`
**Devient** `true` : à la confirmation de réception par C-07
**Obligatoire en NMT 4-5** : oui (traçabilité de la notification humaine)
**Note** : optionnel en NMT 2-3 car C-07 est simulé. Le champ est présent dans le schéma pour assurer la compatibilité ascendante.

---

## 4. Exemple d'enregistrement complet

```json
{
  "log_id": "7f3a2c1e-9b4d-4f8e-a2c1-3d5e7f9b0a2c",
  "timestamp": "2026-05-18T14:32:07.443Z",
  "chain_id": "urn:idees:chain:a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "lifecycle_transition": "ESCALATED",
  "transition_cause": "m_combined(vide) = 0.4200 >= theta_conflit = 0.3000 — paire conflictuelle : (Radar, SIGINT)",
  "m_empty_before": 0.000000,
  "m_empty_after": 0.420000,
  "belnap_state_after": "B",
  "combination_rule": "TBM_CONJUNCTIVE",
  "sil_dal_level": "SIL-2",
  "integrity_hash": "a3f7c2e1b9d4e8f0c1a2b3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4",
  "operator_notified": false
}
```

Cet enregistrement correspond exactement au résultat de l'exécution de `scripts/s01_tbm_minimal.py` (Session 9).

---

## 5. Règles de validation

### V-01 — Complétude
Les 11 champs obligatoires doivent être présents et non nuls.

### V-02 — Cohérence m_empty / belnap_state
Si `m_empty_after ≥ θ_conflit` alors `lifecycle_transition` doit être `"ESCALATED"` et `belnap_state_after` doit être `"B"`.

### V-03 — Cohérence m_empty / valeurs
`0.0 ≤ m_empty_before ≤ 1.0` et `0.0 ≤ m_empty_after ≤ 1.0`.

### V-04 — Monotonie conditionnelle
`m_empty_after ≥ m_empty_before` — la combinaison TBM non normalisée ne peut que maintenir ou accroître le conflit (démonstration algébrique dans CLAIM_specification.md §B.1).

### V-05 — Intégrité du hash
`SHA-256(canonique(champs 1-10)) == integrity_hash`. Tout écart signale une modification non autorisée de l'enregistrement.

### V-06 — Règle de combinaison permise
`combination_rule ≠ "DEMPSTER_NORMALIZED"`. L'utilisation de la règle normalisée est interdite dans ce système (DEC-06 — paradoxe de Zadeh).

---

## 6. Limites NMT 2-3 et trajectoire NMT 4-5

**Limites acceptées pour NMT 2-3 :**

- `operator_notified` optionnel (C-07 simulé)
- Valeur de `θ_conflit` fixe (0.3) — calibration formelle prévue NMT 3 (s02_calibration_theta.py)
- `sil_dal_level` déclaré mais non certifié formellement — certification prévue NMT 4-5
- `integrity_hash` calculé mais non signé cryptographiquement — signature PKI prévue NMT 5

**Trajectoire NMT 4-5 :**

- `operator_notified` devient obligatoire avec horodatage de confirmation C-07
- Ajout de `resolution_timestamp` et `incident_report_id` (lien vers rapport d'incident)
- Certification SIL-3/SIL-4 formelle sur données ISR réelles
- Signature PKI de l'enregistrement (non-répudiation)

---

## 7. Correspondance avec CLAIM_schema.json (TP-01b)

| Champ LOG | Champ CLAIM source | Transformation |
|---|---|---|
| chain_id | provenance.chain_id | Copie directe |
| m_empty_after | belief_mass (sur ∅) | Calcul par combinaison conjonctive |
| belnap_state_after | — | Calculé par l'orchestrateur post-combinaison |
| timestamp | freshness.t_obs | Horodatage de synthèse (pas d'observation) |

---

*Spec maintenue par Claude (instance de session). Autorité de validation : Andrei (PI).*
*Commit : specs/LOG_certifiable.md — version 1.1 corrige le comptage de champs du récapitulatif Session 9.*
