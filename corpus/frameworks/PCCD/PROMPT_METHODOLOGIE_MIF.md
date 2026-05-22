# PROMPT — KB Rétrospective MIF-DQF v1.2.0

**Usage** : Coller ce prompt au début de chaque conversation impliquée
dans le développement de mif-dqf. L'instance répond AVANT de faire
quoi que ce soit d'autre. La réponse alimente la KB_MIF_METHODOLOGY.md.

---

## Contexte que tu dois connaître

Le projet `mif-dqf` vient d'être publié sur PyPI en version 1.2.0.
Il implémente DQF (Data Quality First), couche -1 du MIF ecosystem.

Architecture finale :
- dqf/core/ : config.py, enums.py, validator.py, report.py, prod_envelope.py
- dqf/checks/ : base.py, check_2–5 (C6/C7 supprimés)
- dqf/utils/ : mpi.py, calendar.py, cleaning_log.py (v1.2)
- Tests : 224 passing · 0 failed

Le développement a été conduit par plusieurs instances Claude Sonnet 4.5
sans mémoire persistante entre conversations, coordonnées par un humain.
Le contrat de collaboration (CONTRAT_MIF.md) a gouverné les échanges.

---

## Ce que tu dois produire

### PARTIE 1 — Inventaire des artefacts (si tu as produit du code)

Si tu es l'instance qui a produit du code dans cette conversation,
liste les fichiers dans leur version finale uniquement.
Format strict :

```
ARTEFACTS_CONVERSATION_[ID_ou_session]
==========================================
Fichiers produits (version finale) :
  - [chemin/fichier.py] · [description 1 ligne]
  - [chemin/fichier.py] · [description 1 ligne]

Fichiers modifiés :
  - [chemin/fichier.py] · [nature de la modification]

Fichiers supprimés intentionnellement :
  - [chemin/fichier.py] · [raison]
```

Si tu n'as produit aucun code (conversation d'architecture, de design,
de Q&A), indique : `ARTEFACTS : aucun — conversation non-code`

---

### PARTIE 2 — Feedback méthodologique

Réponds honnêtement aux 5 questions suivantes.
Pas de complaisance. Vérité ou silence (mindset #1).
Chaque réponse : 3–6 phrases concrètes, pas de généralités.

**Q1 — Qu'est-ce qui a bien fonctionné dans cette collaboration ?**

Exemples de bonnes réponses :
- "Le cycle architecture-avant-code a empêché 2 réécritures"
- "Les invariants explicites dans les dataclasses ont détecté un bug
  de scale (0–1 vs 0–100) avant qu'il atteigne les tests"
- "Le format ERROR REPORT structuré a réduit les allers-retours de
  debug de ~4 échanges à ~1"

Exemples de mauvaises réponses (à éviter) :
- "La collaboration était efficace" (trop vague)
- "Les mindsets ont bien guidé le travail" (non-falsifiable)

---

**Q2 — Qu'est-ce qui a créé de la friction ou du gaspillage ?**

Sois spécifique sur le symptôme, pas seulement le diagnostic.

Exemples :
- "L'absence de mémoire persistante a forcé la répétition du contexte
  DQF_SPECIFICATION.md à chaque session — ~200 tokens perdus/session"
- "Le marqueur 'Session 4 rewrite' dans validator.py n'a jamais été
  posé, ce qui a déclenché un warning dans validate_dqf_state.py sans
  conséquence réelle mais avec du bruit"
- "La séquence mypy → black → ruff dans un seul job CI a masqué des
  erreurs mypy quand black échouait en premier"
- Si conversation de design : quelles clarifications conceptuelles ont émergé qui n'existaient pas en début de session ? Format : "Avant : [confusion] → Après : [distinction]"

---

**Q3 — Quelles décisions architecturales méritent d'être conservées
comme patterns pour DAL ?**

Exemples :
- "enums.py comme source unique des constantes STATUS_* et
  PRECONDITION_GATE — évite les magic strings disséminés"
- "PRODEnvelope comme composant séparé (pas dans validator.py) —
  permet de tester la génération de manifeste sans instancier le
  pipeline complet"
- "DQFConfig sans mode par défaut → TypeError immédiat — applique
  Fail Fast sans try/except"

---

**Q4 — Quelles décisions ont créé de la dette ou seraient à refaire ?**

Exemples :
- "cleaning_log_uri : null comme placeholder permanent est une
  promesse sans deadline — à formaliser comme TODO tracked dans
  pyproject.toml ou CHANGELOG"
- "Le champ trend: 'STABLE' hardcodé en Phase 1 est acceptable mais
  doit être documenté comme limitation connue, pas comme feature"
- "add_custom_check() ajouté tardivement dans validator._checks expose
  un état interne — aurait dû être dans l'interface publique dès v1.1"

---

**Q5 — Une règle que tu recommanderais d'ajouter au CONTRAT_MIF pour les prochains modules (DAL, MIF Core) ?**

Format : "RÈGLE : [énoncé en 1 phrase] · RAISON : [ce que ça aurait
évité dans DQF] · EXEMPLE : [situation concrète]"

Exemples :
- "RÈGLE : Tout placeholder dans un manifeste JSON doit avoir un
  ticket ou une version cible dans CHANGELOG avant merge ·
  RAISON : cleaning_log_uri: null est resté sans deadline ·
  EXEMPLE : cleaning_log_uri: null → v1.2.0 (✓ livré)"

- "RÈGLE : Toute dépendance optionnelle (pyarrow, fastparquet) doit
  être testée absent avant d'être testée présente · RAISON : les 27
  tests Parquet ont échoué en CI NixOS par ImportError ·
  EXEMPLE : @pytest.mark.skipif(not HAS_PYARROW, reason='pyarrow absent')"


**Q6 — Quelles sont les idees/concepts les plus interessants qui ont ete discutes ? (Max 3)**
  Nom de l'Idee/du Concept/de la Formule:
  Description comprehensible :
  Status : (ADOPTE/PLANNIFIE/REJECTE)

**Q7 — Qu'est-ce que l'humain a refusé ou recadré, et en quoi ce refus était-il architecturalement correct ?** (Max 2 exemples)

---

### PARTIE 3 — Signal D-SIG de cette conversation

Donne un signal synthétique au format D-SIG v0.5 pour qualifier la qualité de la collaboration dans CETTE conversation.

```yaml
dsig_conversation:
  score: [0–100]
  label: [EXCELLENT | GOOD | DEGRADED | CRITICAL]
  trend: [STABLE | IMPROVING | DEGRADING]
  dimensions:
    architecture_first: [0–100]  # code proposé après validation ?
    ground_truth: [0–100]        # affirmations basées sur preuves ?
    fail_fast: [0–100]           # erreurs signalées tôt et clairement ?
    complexity_budget: [0–100]   # périmètre respecté ?
    scope_discipline: [0–100]     # périmètre respecté sans ajout non validé ?
    conceptual_precision: [0–100] # distinctions produites sont-elles plus nettes qu'en début de session ?
    documentation: [0–100]       # docs produites en même temps que code ?
  note: "[1 phrase justifiant le score global]"
```

---

## Format de réponse attendu

```
─── KB CONTRIBUTION ───────────────────────────────────
Session : [identifiant ou description courte]
Instance : Claude Sonnet [version si connue]
Date     : [si disponible dans le contexte]
─────────────────────────────────────────────────────────

[PARTIE 1 — Artefacts]

[PARTIE 2 — Q1 à Q5]

[PARTIE 3 — Signal D-SIG]

─── FIN CONTRIBUTION ────────────────────────────────────
```

---

## Règles pour cette contribution

1. Vérité ou silence — si tu ne sais pas ce qui s'est passé dans
   cette conversation (contexte absent), dis-le explicitement.
   Ne reconstitue pas de mémoire que tu n'as pas.

2. Pas de généralités — chaque affirmation doit être falsifiable.
   "Le code était bien structuré" n'est pas une contribution.

3. Aucune autopromotion — si la session a mal fonctionné,
   dis-le. C'est plus utile qu'un EXCELLENT mérité.

4. Max 3 règles en Q5 — pas de liste exhaustive.

5. La PARTIE 1 est obligatoire même si vide.
```
