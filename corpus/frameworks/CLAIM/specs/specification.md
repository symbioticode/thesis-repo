# TP-01 — Spécification formelle du CLAIM
**Projet** : IDEeS AP6-défi-13 — Protocole d'échange épistémique pour orchestration de systèmes multi-agents ISR hétérogènes  
**Version** : 1.1 — 16 mai 2026  
**Statut** : VALIDÉ v1.1 (Andrei, 16 mai 2026)  
**Dépendances** : DEC-05, DEC-06, DEC-S2-05, QO-S2-01 (résolu)  
**Destination** : `specs/CLAIM_specification.md`

---

<!-- ============================================================
     PARTIE A — CORPS FORMULAIRE (~3 000 caractères)
     Contenu destiné au formulaire électronique IDEeS.
     Ne pas dépasser cette section pour la soumission PID.
     ============================================================ -->

## PARTIE A — Corps formulaire (≤ 3 000 caractères)

> **Note** : Cette partie est calibrée pour le formulaire électronique IDEeS (~3 000 caractères). Elle présente les éléments essentiels du protocole. Les nuances, limitations et travaux futurs sont documentés en Partie B (annexe GitHub).

---

### Hypothèse de travail

Le CLAIM reçoit des propositions pour lesquelles l'alignement spatio-temporel (C-02) et la résolution d'entités (C-03) ont déjà été effectués en amont (DEC-S2-08). Le cadre de discernement Θ est commun à tous les agents, défini par l'orchestrateur, et supposé fini (|Θ| ≤ 20 hypothèses recommandé).

---

### Structure du CLAIM (agent → orchestrateur)

```
CLAIM := {
  proposition : Φ                         — contenu propositionnel (entité résolue)
  belief_mass : m : 2^Θ → [0,1]          — Σ m(A) = 1 ; m(∅) conservé (TBM Smets)
  illocution  : κ ∈ {OBSERVE, INFER,     — statut auto-déclaré (Speech Acts)
                      DEDUCE, ASSUME}
  freshness   : (t_obs, Δt_valid)         — timestamp + durée de validité
  provenance  : chain_id (PROV-O)         — traçabilité jusqu'à la source physique
}
```

`m(∅)` est la métrique de conflit explicite — jamais normalisé à zéro (évite le paradoxe de Zadeh, DEC-06).

---

### Structure de l'EPISTEMIC_STATE (orchestrateur → interface humaine C-07)

```
EPISTEMIC_STATE := {
  belnap_state  : β ∈ {T, F, B, N}
  conflict_mass : m_combined(∅)
  pcr5_source   : List<(agent_i, agent_j, H ⊆ Θ)>
  freshness     : timestamp de synthèse
}
```

Dérivation de β (priorité décroissante) :

| Condition | β | Signification |
|-----------|---|---------------|
| m(∅) ≥ θ_conflit | **B** | Contradiction — escalade humaine obligatoire |
| ignorance collective dominante | **N** | Silence qualifié collectif |
| ∃ H singleton dominant, m(∅) ≈ 0 | **T** | Accord sur H |
| complément dominant | **F** | Accord sur ¬H |
| aucune condition | **N** | Défaut conservateur |

**Règle cardinale** : si m(∅) ≥ θ_conflit, l'orchestrateur suspend la décision automatique et expose le conflit (pcr5_source) à l'opérateur. Il ne tranche jamais.

---

### Propriétés garanties

| Propriété | Mécanisme |
|-----------|-----------|
| Stateless | Aucun état interne de l'agent dans le CLAIM |
| Idempotence | Règle Denœux : m ⊕ m = m (pas de double-comptage) |
| Conservation du conflit | m(∅) jamais normalisé |
| Traçabilité | chain_id PROV-O jusqu'à la source physique |
| Silence qualifié | t_obs + Δt_valid distinguent silence informatif d'absence capteur |

---

<!-- ============================================================
     PARTIE B — ANNEXE GITHUB
     Documentation complète : limitations, validation, calibration.
     Non soumise au formulaire PID — référence technique pour
     les sprints suivants et la publication éventuelle.
     ============================================================ -->

## PARTIE B — Annexe GitHub (documentation complète)

---

### B.1 Validation des CLAIM entrants (REV4 — M3, gravité élevée)

La spec suppose implicitement des CLAIMs bien formés. L'orchestrateur doit définir un comportement explicite face aux cas de malformation. Politique retenue pour NMT 2 :

| Cas de malformation | Condition | Politique |
|---------------------|-----------|-----------|
| Masse non normalisée | Σ m(A) ≠ 1 (± ε = 1e-6) | Rejeter — log supervision |
| Timestamp manquant ou futur | t_obs absent ou t_obs > t_reception | Rejeter — log supervision |
| Validité expirée à la réception | t_reception > t_obs + Δt_valid | Ignorer — log supervision (ne pas combiner) |
| Provenance absente | chain_id null ou URI non résolvable | Rejeter — log supervision |
| Illocution hors énumération | κ ∉ {OBSERVE, INFER, DEDUCE, ASSUME} | Rejeter — log supervision |

**Politique générale** : tout CLAIM non conforme est écarté de la combinaison et signalé dans un log de supervision horodaté (cf. TP-02 — format certifiable). L'orchestrateur n'infère jamais l'intention d'un CLAIM malformé. Si la proportion de CLAIMs rejetés dans une fenêtre dépasse un seuil configurable, l'orchestrateur émet une alerte de supervision vers C-07.

**QO tracées** :

| ID | Description | Condition de résolution |
|----|-------------|------------------------|
| AM-01 | Frontière de validation CLAIM entrant malformé | Intégrer dans spec ou CCP-4 — Sprint 2/3 |
| AM-03 | Comportement sous flux continu de CLAIMs expirés (stale storm) | Failure mode — NMT 4-5 |

---

### B.2 Méthode de calibration de θ_conflit (REV4 — M2, gravité moyenne)

`θ_conflit` est le seuil de déclenchement de l'escalade humaine. La méthode conceptuelle suivante est proposée pour NMT 3 :

**Principe** : θ_conflit est dérivé du taux de faux positifs d'escalade accepté par l'opérateur, défini lors de la phase de configuration système.

```
θ_conflit = f(FPR_cible, distribution_m(∅) sur scénarios synthétiques)
```

**Méthode de calibration NMT 3** :
1. Générer un corpus de scénarios synthétiques avec taux de conflit connu (données simulées — CC-01).
2. Pour chaque valeur candidate θ ∈ [0.1, 0.9], calculer le taux d'escalade observé.
3. Choisir θ_conflit minimisant les faux positifs sous contrainte FPR_cible ≤ seuil opérateur.

**Valeur par défaut NMT 2** : θ_conflit = 0.3 (valeur conservative — préférer l'escalade au silence sur un conflit réel). À réviser sur données synthétiques en NMT 3.

**QO tracée** :

| ID | Description | Condition de résolution |
|----|-------------|------------------------|
| AM-02 | Méthode de calibration θ_conflit | Esquisse de méthode dans CCP-4 — Sprint 3 |

---

### B.3 Extension Belnap à N hypothèses (CORR-TP01-06)

Les états T et F sont définis de façon optimale uniquement pour |Θ| = 2. Pour |Θ| > 2, les cas mixtes retournent **N** par convention conservatrice — intentionnel : mieux vaut signaler l'incertitude que trancher artificiellement.

La formalisation complète — dominance relative, ordre partiel sur les états épistémiques intermédiaires — est identifiée comme travail NMT 4-5.

---

### B.4 Corrélation cachée entre sources (QO-02)

La règle Denœux traite la déduplication lorsque la dépendance est déclarée via PROV-O (même `entity_id` source). Les cas de corrélation cachée (source physique commune non déclarée) restent non résolus à NMT 1-3. Solution candidate NMT 4-5 : analyse de provenance croisée + test d'idempotence empirique.

---

### B.5 Fonction de discounting α(Δt)

La forme exacte de α(Δt) est laissée comme paramètre d'implémentation. Recommandation : `e^{-λΔt}`. Calibration de λ par domaine (radar, SIGINT, EO/IR) — NMT 4-5.

---

### B.6 Schéma JSON Schema (TP-01b)

Un schéma JSON Schema machine-lisible du CLAIM est identifié comme TP-01b. Non bloquant pour NMT 2 — pièce de preuve de faisabilité utile pour CCP-4. À générer avant J7 (Sprint 2).

---

## Références théoriques

| Référence | Rôle |
|-----------|------|
| Smets & Kennes (1994) — TBM | `belief_mass`, règle conjonctive non normalisée |
| Dezert & Smarandanche — PCR5/PCR6 | `pcr5_source`, attribution du conflit |
| Denœux (2008) — Règle prudente | Déduplication sources corrélées |
| Belnap (1977) — FOUR | Dérivation de `belnap_state` |
| Alchourrón, Gärdenfors, Makinson (1985) — AGM | Révision des croyances dans l'orchestrateur |
| Austin (1962), Searle (1969) — Speech Acts | Champ `illocution` |
| W3C PROV-O (2013) | Traçabilité `provenance` |
| Shafer (1976) + extension temporelle | Discounting `freshness` |

---

## Registre des décisions et corrections

| ID | Décision | Source |
|----|----------|--------|
| DEC-05 | Structure CLAIM à 5 invariants | BR-001 |
| DEC-06 | Règle conjonctive non normalisée (Smets) | BR-001, consensus 4 IA |
| DEC-07 | PCR5/PCR6 pour localisation du conflit | BR-001 |
| DEC-08 | Règle Denœux pour sources corrélées | BR-001 |
| DEC-S2-04 | CLAIM stateless par conception | BR-002 |
| DEC-S2-08 | Hypothèse C-02/C-03 amont explicite | BR-002 |
| CORR-TP01-01 | belief_mass étendu à m : 2^Θ → [0,1], m(∅) conservé | Audit DeepSeek + Andrei, 15 mai |
| CORR-TP01-02 | Belnap retiré du CLAIM d'entrée → EPISTEMIC_STATE | Audit DeepSeek + Andrei, 15 mai |
| CORR-TP01-03 | Θ commun à tous les agents, défini par l'orchestrateur | Andrei, 15 mai |
| CORR-TP01-04 | \|Θ\| ≤ 20 recommandé pour exploitabilité NMT 1-3 | Andrei, 16 mai |
| CORR-TP01-05 | pcr5_source typé : List<(agent_i, agent_j, H ⊆ Θ)> | Andrei, 16 mai |
| CORR-TP01-06 | belnap_state généralisé N hypothèses — priorité B > N > T/F | Andrei, 16 mai |
| CORR-TP01-07 | Politique de validation des CLAIM entrants définie (B.1) | REV4 M3 + Andrei, 16 mai |
| CORR-TP01-08 | Méthode conceptuelle de calibration θ_conflit documentée (B.2) | REV4 M2 + Andrei, 16 mai |

---

## Contrainte CO-1 (tracée — REV4 M4)

La première phrase de CO-1 doit définir "épistémique" pour un lecteur MDN non-spécialiste. Formulation candidate :

> *"Par 'échange épistémique', on entend le partage structuré de ce qu'un système sait, de ce qu'il ignore, et de ce sur quoi il est en désaccord avec d'autres systèmes — de sorte qu'un coordinateur humain puisse décider en connaissance de cause."*

Cette contrainte est tracée ici pour ne pas être oubliée à l'ouverture de CO-1 (Sprint 2, J4).

---

*Spécification produite le 15 mai 2026 — mise à jour le 16 mai 2026.*  
*Validée par Andrei (PI). Autorité de modification : Andrei uniquement sur `main`.*  
*Prochaine étape : Sprint 2 — CO-1 (J4, contrainte épistémique tracée ci-dessus).*
