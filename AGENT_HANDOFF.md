# AGENT_HANDOFF.md
# Fichier de coordination Jules ↔ Claude Code
# Andrei lit ce fichier chaque matin avant le démarrage de la journée.
# Les deux agents écrivent ici — ne pas créer de fichier séparé.

---

## INITIALISATION — Andrei (21 mai 2026)

```yaml
date: 2026-05-21
agent: Andrei
action: initialisation
repo_structure_cible:
  - thesis/
  - poc/
  - corpus/frameworks/    ← copier les fichiers du corpus ici
  - corpus/references/    ← créer refs.bib
  - MASTER_BRIEF.md       ← présent
  - AGENT_HANDOFF.md      ← ce fichier
instructions_jules: |
  Lire MASTER_BRIEF.md SECTION 0 en premier.
  Produire confirmation bootstrap.
  Lire les fichiers corpus/frameworks/ listés en SECTION 4.
  Démarrer ch0_genese.md et ch1_probleme.md.
instructions_claude_code: |
  Lire MASTER_BRIEF.md SECTION 0 en premier.
  Produire confirmation bootstrap.
  Démarrer poc/claim/structures.py et poc/claim/validator.py.
  Tests unitaires avant tout commit.
questions_ouvertes: []
bloquants: NON
```

---

## J0 — Jules (21 mai 2026)

```yaml
date: 2026-05-21
agent: Jules
jour: J0
livrables_produits:
  - README.md : 65 lignes
  - MASTER_BRIEF.md : 230 lignes
  - Structure de fichiers : 24 fichiers créés
questions_ouvertes:
  - Où se trouvent les fichiers sources du corpus ? → Andrei (RÉSOLU : synchronisés via git)
prochaine_action: Démarrer J1.
bloquants: NON
```

---

## J1 — Jules (22 mai 2026)

```yaml
date: 2026-05-22
agent: Jules
jour: J1
livrables_produits:
  - thesis/ch0_genese.md : ~600 mots
  - thesis/ch1_probleme.md : ~750 mots
questions_ouvertes:
  - Les chapitres respectent-ils le ton "première personne du pluriel de recherche" attendu ? → Andrei
prochaine_action: Démarrer J2 (Chapitres 2 et 3).
bloquants: NON
```

---

## J2 — Jules (22 mai 2026)

```yaml
date: 2026-05-22
agent: Jules
jour: J2
livrables_produits:
  - thesis/ch2_convergence.md : ~700 mots
  - thesis/ch3_formalisation.md : ~750 mots
questions_ouvertes:
  - Les références à la validation externe (FDA, NATO, NIH) sont-elles assez détaillées pour ch2 ? → Andrei
  - Doit-on intégrer les nouveaux fichiers du répertoire corpus/frameworks/CLAIM/ dans ch3 dès maintenant ? → Andrei
prochaine_action: Démarrer J3 (Chapitres 4 et 5 + Assemblage).
bloquants: NON
```
