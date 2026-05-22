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

BRIEF CHARGÉ.
Agent         : Jules
Périmètre     : THÈSE
Livrable J1   : ch0_genese.md, ch1_probleme.md
Question avant démarrage : OUI — Les fichiers du corpus listés en SECTION 4 sont-ils disponibles ? Ils manquent dans le répertoire /corpus/frameworks/.

---

# AGENT_HANDOFF.md
date: 2026-05-21
agent: Jules
jour: J0
livrables_produits:
  - README.md : 65 lignes
  - MASTER_BRIEF.md : 230 lignes
  - Structure de fichiers : 24 fichiers créés (incluant .gitignore, .gitkeep)
questions_ouvertes:
  - Où se trouvent les fichiers sources du corpus (PCCD, RKA, etc.) pour commencer J1 ? → Andrei
prochaine_action: Démarrer J1 (Chapitres 0 et 1) dès réception du corpus.
bloquants: OUI — Corpus manquant.
