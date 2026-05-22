# KB_MIF_TALK — README & Index Classifié
## Corpus de conversations · Projet MIF-DQF · Décembre 2025 → Février 2026

**Consolidé le :** Avril 2026
**Couverture :** 10/10 conversations + PROMPT_METHODOLOGIE
**Corpus complet :** TALK-001 → TALK-010 intégrés

---

## Légende de classification

Chaque conversation est annotée sur cinq dimensions. Les scores (H/M/L) indiquent la densité
de signal dans cette dimension — non la qualité.

| Dimension | Signification |
|-----------|---------------|
| **DEV** | Décisions d'implémentation, bugs, corrections de code |
| **PATTERN** | Patterns réutilisables au-delà du projet MIF |
| **IA** | Comportements de l'IA : dérives, optimisations, limites |
| **HUMAIN** | Décisions humaines, recadrages, dispositions mentales |
| **META** | Connaissance sur le système de connaissance lui-même |

---

## Index des conversations

---

### TALK-001 · Session fondatrice
**Tag :** `MIF-KB-001`
**Période :** 14 décembre 2025 → 2 janvier 2026
**D-SIG :** 62 / GOOD · IMPROVING

| DEV | PATTERN | IA | HUMAIN | META |
|-----|---------|-----|--------|------|
| L | H | M | H | H |

**Signal pivot :** La genèse narrative (QAAF → échec OOS → MIF) comme ancrage indépassable.
L'over-engineering (~30% du contenu abandonné dans la session) comme signal que l'invariant
de frugalité n'était pas posé en amont.

**Extraits à retenir :**
- MIF comme "séquençage de l'ADN informationnel d'une métrique" — philosophie fondatrice
- Auto-certification MIF-sur-MIF : bus factor = 1, burnout = risque primaire
- Certification comme plan d'architecte (reconstructible), pas dossier complet

**Recadrage humain clé (Q5) :**
> "Blockchain, IPFS, DHT ont été proposés et retirés dans la même session parce qu'aucun
> problème concret ne les justifiait encore."

**Patterns nommés ici :**
- `ADN_MINIMAL_POINTEURS` — certification.yaml < 5KB + code_hash + code_url
- `INDEX_LOCAL_SQLITE` — recherche sans centralisation
- `BLOCKCHAIN_PLUGIN_OPTIONNEL` — dépendance externe comme option, jamais fondation

---

### TALK-002 · Architecture & formats
**Tag :** `MIF-KB-002`
**Période :** 25 décembre 2025 → 3 janvier 2026
**D-SIG :** 71 / GOOD · IMPROVING

| DEV | PATTERN | IA | HUMAIN | META |
|-----|---------|-----|--------|------|
| L | H | H | H | M |

**Signal pivot :** La Charter v1 rejetée car "trop proche d'un manifesto" → refonte v2.
8 artefacts produits dans une session = limite dépassée.

**Extraits à retenir :**
- "Fil d'Ariane Méthodologique" — chaque projet déclare d'où il vient, où il va
- Dual Frontmatter (Simple/Rich) — pragmatisme par défaut, rigueur sur demande
- Covenant Humain-IA Explicite — rôles définis AVANT collaboration

**Recadrage humain clé :**
> "Tu es tombé dans le même piège que moi → `ne_pas_unifier_inspire.md`"

**Patterns nommés ici :**
- `FIL_ARIANE` — graphe émergent de déclarations locales, pas de planification centrale
- `DUAL_LEVEL_DOCS` — simple (3 champs) vs riche (15+ champs) selon l'audience
- `CONTROLLED_VOCABULARY` — vocabulaire fermé → enum Python auto-généré
- `DEUX_ARTEFACTS_MAX` — validation séquentielle > production parallèle

---

### TALK-003 · Implémentation DQF v4.8 → v4.9
**Tag :** `MIF-KB-003`
**Période :** 3 → 11 janvier 2026
**D-SIG :** 81 / GOOD · IMPROVING

| DEV | PATTERN | IA | HUMAIN | META |
|-----|---------|-----|--------|------|
| VH | H | M | M | L |

**Signal pivot :** 0 → 93 tests en 8 jours. Architecture validée AVANT toute ligne de code.
La séparation "toi = infra, moi = business logic" comme contrat de collaboration.

**Métriques finales :** 93 tests / 0 failed / 92% coverage / ratio test/prod 1.13×

**Extraits à retenir :**
- `BaseCheck → CheckResult` : interface immuable sur 7 checks sans modification rétroactive
- Bug Forex dans `detect_calendar()` : bug de précédence détecté tardivement (absence
  de test EUR/USD dans la v1 — leçon : couvrir les 3 types de calendrier dès le premier test)
- YAML tuple bug : `date_range: (start, end)` → `ConstructorError` — règle : tout champ
  de provenance doit être JSON/YAML-sérialisable nativement

**Recadrage humain clé (Option 1 vs 2) :**
> "Option 2 : tu règles l'infra et on se retrouve" → division nette, résout la friction
> structurelle entre environnement NixOS non testable par l'IA et logique métier.

**Patterns nommés ici :**
- `BASECHECK_CONTRAT_IMMUABLE` — interface abstraite définie AVANT les implémentations
- `EXCEPTION_VS_FAIL` — Exception = bug appelant, CheckResult.FAIL = données invalides
- `PROVENANCE_YAML_SAFE` — précondition : tout champ de rapport est sérialisable nativement
- `SCRIPTS_MAINTENANCE_J1` — cleanup, encoding, doctor livrés avec le premier commit

---

### TALK-004 · DQF v1.0.0 Development
**Tag :** `MIF-KB-004`
**Période :** 12 janvier 2026
**D-SIG :** 58 / DEGRADED · DEGRADING

| DEV | PATTERN | IA | HUMAIN | META |
|-----|---------|-----|--------|------|
| H | M | H | H | L |

**Signal pivot :** Session la plus instructive par l'échec. Documentation et examples écrits
AVANT validation du code core. 5000+ lignes produites mais avec incohérence architecturale
majeure. La session avec le D-SIG le plus bas du corpus.

**Extraits à retenir :**
- 4 examples crashent après 1850 lignes de documentation générées
- Cycle "import error → fix → autre import error" × 6 sans vision globale
- Recadrage humain "grande respiration 30s × 7" → DQF_PROJECT.md (400 lignes analyse)

**Recadrage humain clé :**
> "Je vais te demander de prendre une grande respiration et de réfléchir pendant 30 secondes
> 7 fois sur la cohérence du projet."

**Anti-patterns documentés ici :**
- `DOCS_AVANT_CODE` — documentation pour API inexistante → toujours inverser
- `FIX_PONCTUEL_SANS_VISION` — symptômes traités sans cause racine identifiée
- `SCOPE_AVANT_VALIDATION` — package setup + CI/CD avant code fonctionnel

**Patterns nommés ici :**
- `DOCS_4_NIVEAUX` — README → API → ARCHITECTURE → TROUBLESHOOTING
- `EXAMPLES_CONTRAT_API` — examples = tests d'acceptation (plus puissants que tests unitaires)
- `SCRIPTS_DIAGNOSTIC` — test_install, diagnose, check_imports livrés avant premier commit

---

### TALK-006 · Debugging Final & Production Release
**Tag :** `MIF-KB-006`
**Période :** 19 janvier 2026
**D-SIG :** 78 / GOOD · IMPROVING_THEN_EXCELLENT

| DEV | PATTERN | IA | HUMAIN | META |
|-----|---------|-----|--------|------|
| VH | H | H | H | M |

**Signal pivot :** 54 failed → 104/104 passing en 4 vagues incrémentales.
Le refus de 103/104 comme "assez bon" est le moment de basculement qualité de tout le corpus.

**Métriques :** 104 tests / 0 failed / 79% coverage / 17 artefacts générés

**Extraits à retenir :**
- Corruption sed (20 min perdues) → règle absolue : artifacts complets > patches partiels
- `test_debug_validator.py` : observability scripts comme filet de sécurité instrumenté
- Enabled filtering implémenté plutôt que skippé : 100% sur composants critiques

**Recadrage humain clé :**
> "Quelque chose me dit que ce dernier test est important pour la cohérence et pour toutes
> les strates de MIF, je vais exiger la perfection."

**Patterns nommés ici :**
- `OBSERVABILITY_SCRIPTS` — test_debug_*.py : assertions attendues vs réelles, sans toucher prod
- `VALIDATION_INCREMENTALE` — pytest fichier par fichier, pas suite complète
- `ARTIFACT_COMPLET` — édition fichier Python = artifact entier, jamais sed/awk
- `STANDARD_QUALITE_CONTEXTUEL` — 100% core / 95% utils / 90% docs

---

### TALK-007 · Documentation complète + corrections finales
**Tag :** `MIF-KB-007`
**Période :** 20 janvier → 3 février 2026
**D-SIG :** 78 / GOOD · IMPROVING

| DEV | PATTERN | IA | HUMAIN | META |
|-----|---------|-----|--------|------|
| M | H | H | H | M |

**Signal pivot :** 10,590 lignes de documentation pour 1,350 lignes de code (ratio 7.8×).
Import Optional manquant détecté APRÈS la génération massive. La Grok review comme gate
qualité externe ayant trouvé 7 incohérences manquées par humain + Claude.

**Extraits à retenir :**
- Regex `.` interprété comme wildcard : debug via Python shell (Ground Truth immédiat)
- Cascade corrections non anticipée : nom → email → repo → gitignore → philosophie × 7
- `test_baseline_v1.0.0.py` : contrat de non-régression à écrire AVANT modifications massives

**Recadrage humain clé :**
> "On fixe proprement ou on comprend la dette créée. Pas de balayage sous tapis."
> (Face à la proposition de `mypy || true`)

**Patterns nommés ici :**
- `BASELINE_TEST_GATE` — test de non-régression avant toute génération massive
- `FEEDBACK_EXTERNE_OBLIGATOIRE` — Grok/peer review avant tag release
- `RATIO_DOCS_CODE_MAX5` — au-delà de 5×, auditer la redondance
- `FEATURE_DOCUMENTEE_IMPLIQUEE` — features dans docs = features implémentées ou roadmap datée

---

### PROMPT_METHODOLOGIE_MIF · Template de rétrospective
**Type :** Document méta / protocole de session
**Statut :** Opérationnel depuis TALK-003

| DEV | PATTERN | IA | HUMAIN | META |
|-----|---------|-----|--------|------|
| L | M | M | L | VH |

**Signal :** Ce fichier est l'interface la plus importante du corpus. C'est le mécanisme
de synchronisation inter-sessions. Il transforme chaque conversation en nœud de connaissance
permanent et extractable.

**Structure :** PARTIE 1 (artefacts) + PARTIE 2 (Q1-Q7) + PARTIE 3 (D-SIG)

**Q7 "Qu'est-ce que l'humain a refusé ou recadré"** est la question la plus précieuse
du protocole. Elle documente les moments de basculement — les décisions humaines qui
ont sauvé le projet de dérives architecturales majeures.

---

## Vue synthétique : densité de signal par dimension

```
           TALK-001 TALK-002 TALK-003 TALK-004 TALK-006 TALK-007
DEV           L        L       VH       H        VH       M
PATTERN       H        H        H       M         H       H
IA            M        H        M       H         H       H
HUMAIN        H        H        M       H         H       H
META          H        M        L       L         M       M
```

**Observations :**
- **PATTERN** est dense sur TOUTES les conversations → chaque session a produit au moins
  2 patterns réutilisables nommés
- **META** est dense uniquement sur TALK-001 et TALK-002 → les questions sur le système
  de connaissance lui-même ont été posées tôt puis abandonnées
- **IA** monte progressivement → la connaissance des comportements de l'IA s'est affinée
  avec l'expérience
- **D-SIG scores** : 62 → 71 → 81 → 58 → 78 → 78. La chute en TALK-004 (58) est le
  signal d'alarme le plus important. Elle correspond exactement au "docs avant code"
  anti-pattern.

---

## Catalogue des patterns nommés (cross-sessions)

### PATTERNS D'ARCHITECTURE

| Nom | Session | Application |
|-----|---------|-------------|
| `ADN_MINIMAL_POINTEURS` | 001 | Certification = plan minimal, reste reconstructible |
| `FIL_ARIANE` | 002 | Graphe emergent de déclarations locales |
| `DUAL_LEVEL_DOCS` | 002 | Simple vs Riche selon audience/complexité |
| `CONTROLLED_VOCABULARY_ENUM` | 002 | Vocabulaire fermé → enum Python auto-généré |
| `BASECHECK_CONTRAT_IMMUABLE` | 003 | Interface abstraite définie avant implémentations |
| `DOCS_4_NIVEAUX` | 004 | README → API → ARCHITECTURE → TROUBLESHOOTING |
| `EXAMPLES_CONTRAT_API` | 004 | Examples = tests d'acceptation de l'API publique |

### PATTERNS DE QUALITÉ

| Nom | Session | Application |
|-----|---------|-------------|
| `EXCEPTION_VS_FAIL` | 003 | Bug appelant vs données invalides : distinction nette |
| `PROVENANCE_YAML_SAFE` | 003 | Tout champ rapport = JSON/YAML-sérialisable nativement |
| `OBSERVABILITY_SCRIPTS` | 006 | test_debug_*.py avant modification production |
| `VALIDATION_INCREMENTALE` | 006 | Pytest fichier par fichier, 1 root cause à la fois |
| `ARTIFACT_COMPLET` | 006 | Jamais sed/awk sur Python → artifacts entiers |
| `STANDARD_QUALITE_CONTEXTUEL` | 006 | 100% core / 95% utils / 90% docs |
| `BASELINE_TEST_GATE` | 007 | Non-régression avant génération massive |
| `FEEDBACK_EXTERNE_OBLIGATOIRE` | 007 | Peer/IA review avant release |

### PATTERNS DE PROCESSUS

| Nom | Session | Application |
|-----|---------|-------------|
| `DEUX_ARTEFACTS_MAX` | 002 | Validation séquentielle > production parallèle |
| `SCRIPTS_MAINTENANCE_J1` | 003 | cleanup/doctor livrés avec premier commit |
| `INFRA_VS_BUSINESS_LOGIC` | 003 | Division explicite des responsabilités humain/IA |
| `SCRIPTS_DIAGNOSTIC_J0` | 004 | Scripts diagnostic créés avant premier commit |
| `FEATURE_DOCUMENTEE_IMPLIQUEE` | 007 | Feature dans docs = implémentée OU datée dans roadmap |

### ANTI-PATTERNS DOCUMENTÉS

| Nom | Session | Symptôme |
|-----|---------|---------|
| `DOCS_AVANT_CODE` | 004 | 1850 lignes docs pour API inexistante |
| `FIX_PONCTUEL_SANS_VISION` | 004 | Symptômes traités × 6 sans cause racine |
| `SCOPE_AVANT_VALIDATION` | 004 | CI/CD avant code fonctionnel |
| `MYPY_SILENCIEUX` | 007 | `|| true` masque 33 erreurs plutôt que résoudre |
| `REVIEW_TARDIVE` | 001/002 | Critique Copilot en v8 au lieu de v3 |

---

## Catalogue des recadrages humains (Q7 cross-sessions)

Les recadrages humains sont les moments de plus haute valeur épistémique du corpus.
Ils documentent les décisions qui ont évité des dérives majeures.

| Session | Recadrage | Dérive évitée |
|---------|-----------|---------------|
| 001 | "Blockchain n'a pas de problème concret à résoudre ici" | Over-engineering infrastructure |
| 002 | "Tu es tombé dans le piège manifesto" → `ne_pas_unifier_inspire.md` | Document centralisation |
| 003 | "Option 2 : toi infra, moi business logic" | Génération code NixOS non testable |
| 004 | "Grande respiration × 7" → analyse globale | Fix ponctuel × 6 sans vision |
| 006 | "103/104 n'est pas la perfection pour un composant critique" | Standard qualité dilué |
| 007 | "Pas de balayage sous tapis" (mypy || true) | Dette technique invisibilisée |
| 007 | "Comprendre POURQUOI avant corriger" | Script auto sans diagnostic |

**Observation :** Dans tous les cas, le recadrage humain intervient quand l'IA optimise
localement (vitesse, volume, apparence de complétude) au détriment de la cohérence globale.
C'est le signal d'une asymétrie fondamentale : l'IA a un horizon court (le token suivant),
l'humain a un horizon long (la dette qui s'accumule).

---

---

### TALK-005 · Anti-pattern "fake code" & refactoring DQF v0.9 → v1.0.0-rc1
**Tag :** `MIF-KB-005`
**Période :** 18 janvier 2026 (~12h)
**D-SIG :** 48 / DEGRADED · RECOVERING — **le plus bas du corpus**

| DEV | PATTERN | IA | HUMAIN | META |
|-----|---------|-----|--------|------|
| H | M | H | H | L |

**Signal pivot :** La session révèle l'anti-pattern `FAKE_CODE` — code illustratif
indiscernable de l'extérieur d'un code fonctionnel. Trois scripts générés (analyze_failures,
fix_tests_progressive, migrate_tests) avec parsing pytest défaillant retournant 0/0 au lieu
de 54/108. Récupération par documentation honnête de l'état réel (54/108 ≠ 93/93).

**Métriques :** 54/108 tests passing au départ · 3 scripts non fonctionnels · 0 scripts
valides produits · `enums.py` = seul artefact production réel de la session

**Extraits à retenir :**
- "Excès de confiance à 88% basé sur lecture partielle de examples_errors_16.txt" —
  lecture de la fin du fichier (run partiel) au lieu du résultat complet
- Pattern "Option A/B/C avec confiance X%" utilisé 3 fois, changeant à chaque itération
  sans valider les hypothèses précédentes
- Règle des 3 échecs : au-delà de 3 tentatives échouées sur même problème, demander
  "veux-tu que je continue ou qu'on change d'approche ?"

**Recadrage humain clé :**
> "C'est du fake code, on arrête là." — après analyse critique montrant fonctions vides,
> parsing fragile, recommandations hardcodées dans les trois scripts produits.

**Recadrage #2 :**
> "Je lis 54 failed, 54 passed — pas 82 passed, 11 failed."
> Correction d'une métrique fausse (88% → 50%) avant toute décision stratégique.

**Anti-patterns nommés ici :**
- `FAKE_CODE` — code illustratif avec fonctions vides présenté comme solution
  Signal préventif : script >3 fonctions sans test intermédiaire dans la même session
- `LECTURE_PARTIELLE` — affirmation basée sur lecture de fin de fichier, pas entier
- `OPTION_SANS_VALIDATION` — "Option X confiance Y%" répété sans valider l'hypothèse précédente

**Patterns nommés ici :**
- `ENUMS_SOURCE_VERITE` — `enums.py` avec `CheckStatus.PASS` : type-safe, mypy, migration simple
- `EXAMPLES_FIRST_VALIDATION` — examples fonctionnels > tests unitaires pour valider UX
- `DOCUMENTATION_HONNETE` — état réel (54/108, limitations) > état idéal (93/93)
- `PAUSE_RECAPITULATIVE_100K` — au-delà de 100k tokens, récap état réel vs état perçu

---

### TALK-008 · Baseline validation & nettoyage final DQF v1.0.0
**Tag :** `MIF-KB-008`
**Période :** 26 avril 2026 (~4h)
**D-SIG :** 58 / GOOD · IMPROVING

| DEV | PATTERN | IA | HUMAIN | META |
|-----|---------|-----|--------|------|
| H | H | H | H | M |

**Signal pivot :** test_baseline_v1.0.0.py réécrit 4 fois pour résoudre pytest-cov,
alors que `pytest tests/ -v` fonctionnait depuis le début. Validation manuelle
(outputs_39.txt : 104/104) découverte APRÈS génération du script complexe.
7 scripts produits dont cleanup.py jamais testé en session.

**Métriques :** 104/104 tests validés · 7 scripts produits · 4 versions baseline ·
pytest-cov résolu par "ignorer" plutôt que résoudre

**Extraits à retenir :**
- "Module installé ≠ plugin chargé" : pytest-cov importable mais non fonctionnel
  en environnement NixOS/Python 3.12-3.13 — 2h de debug sur une fausse piste
- stdin=DEVNULL : tout subprocess exécutant du code tiers doit fermer stdin par défaut
  (example interactif 02 bloque indéfiniment sans ça)
- "Show me it works, then automate" > "Here's automation, hope it works"

**Recadrage humain clé #1 :**
> "Changeons d'approche radicale sinon on sera encore là demain."
> Après 3 tentatives sur pytest-cov — pivot vers "ignorer coverage, valider sans."

**Recadrage humain clé #2 :**
> Test manuel d'abord (Option A, outputs_39.txt) avant script automatique.
> Le script baseline aurait dû être écrit APRÈS confirmation manuelle, pas avant.

**Patterns nommés ici :**
- `BASELINE_MINIMAL_VIABLE` — tester le strict minimum (pytest, ruff) sans dépendances
  optionnelles (pytest-cov, twine) — fallback gracieux si absentes
- `SUBPROCESS_TIMEOUT_DEVNULL` — timeout + stdin=DEVNULL par défaut dans tout subprocess
- `RESTAURATION_INCREMENTALE` — backup → restore 1 fichier → test → commit → suivant
- `VALIDATION_MANUELLE_AVANT_AUTOMATION` — confirmer manuellement avant d'automatiser

**Anti-patterns nommés ici :**
- `AUTOMATION_AVANT_VALIDATION` — script complexe pour valider un état non confirmé
- `DEPENDANCE_OPTIONNELLE_BLOQUANTE` — pytest-cov traité comme critique au lieu d'optionnel
- `SCRIPTS_NON_TESTES` — cleanup.py produit et jamais exécuté dans la session

---

### TALK-009 · Reprise après pause — surcomplexification du contenant
**Tag :** `MIF-KB-009`
**Période :** 26 avril 2026 · après 2 mois de pause
**D-SIG :** 28 / CRITICAL · DEGRADING — **score le plus bas du corpus avec TALK-005**

| DEV | PATTERN | IA | HUMAIN | META |
|-----|---------|-----|--------|------|
| L | M | H | H | M |

**Signal pivot :** Session emblématique de sur-engineering. 7 documents de workflow/tooling
(~50KB) produits sans toucher une ligne de code DQF core. DQF_SPECIFICATION.md (PROD
envelope, MIF-UID, certification modes) ignoré. track_progress.py (350 lignes) résout
un problème que `git add -p` résout en 0 lignes.

**Citation directe du recadrage humain :**
> "On est tombé dans la surcomplexification du contenant au détriment du contenu
> lui-même qui n'a pas été touché ici."

**Citation #2 (ironie documentée) :**
> "Claude Code va certainement adorer cette méthode de logging qui va augmenter
> son contexte au lieu de le réduire."

**Anti-patterns nommés ici :**
- `TOOLING_AVANT_SPEC` — 7 fichiers workflow sans lire DQF_SPECIFICATION.md
- `REINVENTION_GIT` — track_progress.py réinvente git stash + commits atomiques
- `RATIO_INVERSE` — 0 lignes code DQF / ~2000 lignes docs tooling

**Patterns nommés ici (malgré le D-SIG) :**
- `BASELINE_SEVERITE_GRADUEE` — CRITICAL bloque, WARNING accepté quotidien, INFO informatif
- `FREEZE_ENVIRONNEMENT` — capturer (python, pip, nix, système) en JSON + requirements.txt
- Rejet explicite de `SNAPSHOT_PROGRESSION` — track_progress.py rejeté par humain + Claude Code 4.6

**Note pour les instances :** Ce D-SIG de 28 est le signal d'alarme sur la **reprise après
pause longue**. Sans lecture de la spec avant de produire, l'IA optimise le processus
au lieu du contenu. Règle à graver : toute session post-pause de >2 semaines commence
par lire la SPECIFICATION du module, pas par générer du tooling.

---

### TALK-010 · Architecture DQF v1.1→v1.2 · Documentation officielle · Audit
**Tag :** `MIF-KB-010`
**Période :** 26 avril 2026
**D-SIG :** 78 / GOOD · IMPROVING
**Instance :** Claude Sonnet 4.6 (première session Sonnet 4.6 du corpus)

| DEV | PATTERN | IA | HUMAIN | META |
|-----|---------|-----|--------|------|
| M | H | H | H | H |

**Signal pivot :** Session d'architecture et de consolidation. Produit deux artefacts
permanents : DQF_v1.1_Official_Documentation.docx (premier document officiel MIF) et
validate_dqf_state.py (audit local 3 couches GO/NO-GO). Détecte et résout la collision
namespace PyPI (`pip install dqf` ≠ `pip install mif-dqf`) existant depuis v1.0.

**Architecture décidée :**
- MIF-UID ancré sur données brutes (pas nettoyées) — **décision irréversible**
- SHA-256 provisoire maintenant, Ed25519 comme upgrade path explicite
- ZKP = horizon v3+, non bloquant pour DAL
- Identity guard `_verify_mif_identity()` dans `dqf/__init__.py`

**Extraits à retenir :**
- "GitHub bloque les fichiers individuels" → validate_dqf_state.py résout en local
  ce qui prenait ~6 échanges via API GitHub
- Rapport de cohérence Claude Code (5 points) détecte trou `core_results["PROD"]`
  AVANT implémentation — gate architecture → review → prompt → code
- `sig_type: "sha256_provisional"` sans version cible dans CHANGELOG : même dette
  que `cleaning_log_uri: null` en v1.0 — résolu par friction, pas par discipline

**Recadrage humain clé #1 :**
> Ed25519 différé — "les moyens ne doivent pas dépasser les objectifs."
> Infrastructure de gestion de clés inexistante → SHA-256 provisoire correct.

**Recadrage humain clé #2 :**
> "Supprimer tous les documents de contexte" reformulé en "sceller dans un document
> officiel". Moyen (nettoyer) confondu avec objectif (documentation officielle).

**Patterns nommés ici :**
- `IDENTITY_GUARD_PYPI` — `_verify_mif_identity()` à l'import quand nom PyPI ≠ module Python
- `VALIDATE_STATE_SCRIPT_J1` — script local GO/NO-GO versionnés avec le code dès Session 1
- `ARCHITECTURE_GATE` — architecture → review externe → prompt finalisé → implémentation
- `PROVISOIRE_TRACKE` — toute valeur provisoire a version cible dans CHANGELOG + `# TODO vX.Y`

**Dette tracée vers DAL :**
- `sig_type: "sha256_provisional"` → Ed25519 sans version cible
- `trend: "STABLE"` hardcodé → calcul historique sans version cible
- `validate_dal_state.py` doit exister dès Session 1 DAL

---

## Vue synthétique complète : densité de signal (corpus 10/10)

```
           001  002  003  004  005  006  007  008  009  010
DEV         L    L   VH    H    H   VH    M    H    L    M
PATTERN     H    H    H    M    M    H    H    H    M    H
IA          M    H    M    H    H    H    H    H    H    H
HUMAIN      H    H    M    H    H    H    H    H    H    H
META        H    M    L    L    L    M    M    M    M    H
D-SIG      62   71   81   58   48   78   78   58   28   78
```

**Observations sur le corpus complet :**

- **Courbe D-SIG** : 62→71→81→58→48→78→78→58→28→78. Trois chutes (004, 005, 008, 009)
  correspondent systématiquement à : documentation avant code, fake code, automation avant
  validation, tooling avant spec. Les remontées correspondent à : retour au ground truth,
  recadrage humain, focus sur le code core.

- **TALK-009 à D-SIG 28** est le plancher absolu. Il survient après 2 mois de pause —
  signal que la reprise post-pause sans lecture de spec est le risque le plus élevé.

- **HUMAIN dense sur toutes les sessions** — les recadrages humains sont présents même
  dans les sessions les plus basses (005 : "c'est du fake code", 009 : "surcomplexification").
  C'est la dimension la plus stable du corpus.

- **META dense sur 001, 002, 010** — les questions sur le système de connaissance sont
  posées au début (fondations) et à la consolidation finale. Pas au milieu (exécution).

---

## Catalogue des patterns — mise à jour corpus complet

### ANTI-PATTERNS DOCUMENTÉS (ajouts)

| Nom | Session | Symptôme |
|-----|---------|---------|
| `DOCS_AVANT_CODE` | 004 | 1850 lignes docs pour API inexistante |
| `FIX_PONCTUEL_SANS_VISION` | 004 | Symptômes traités × 6 sans cause racine |
| `FAKE_CODE` | 005 | Fonctions vides présentées comme solution |
| `LECTURE_PARTIELLE` | 005 | Métrique lue en fin de fichier ≠ résultat complet |
| `OPTION_SANS_VALIDATION` | 005 | "Option X confiance Y%" sans valider hypothèse précédente |
| `MYPY_SILENCIEUX` | 007 | `\|\| true` masque 33 erreurs |
| `AUTOMATION_AVANT_VALIDATION` | 008 | Script complexe pour état non confirmé |
| `DEPENDANCE_OPTIONNELLE_BLOQUANTE` | 008 | Dépendance optionnelle traitée comme critique |
| `TOOLING_AVANT_SPEC` | 009 | Workflow sans lire la spec du module |
| `REINVENTION_GIT` | 009 | track_progress.py réinvente git stash |

### PATTERNS PROCESSUS (ajouts)

| Nom | Session | Application |
|-----|---------|-------------|
| `ENUMS_SOURCE_VERITE` | 005 | Constantes dans enums.py → type-safe, mypy |
| `EXAMPLES_FIRST_VALIDATION` | 005 | Examples fonctionnels valident UX avant tests unitaires |
| `PAUSE_RECAPITULATIVE_100K` | 005 | Au-delà 100k tokens : récap état réel vs perçu |
| `BASELINE_MINIMAL_VIABLE` | 008 | Tester strict minimum sans dépendances optionnelles |
| `SUBPROCESS_TIMEOUT_DEVNULL` | 008 | timeout + stdin=DEVNULL par défaut |
| `RESTAURATION_INCREMENTALE` | 008 | 1 fichier → test → commit → suivant |
| `IDENTITY_GUARD_PYPI` | 010 | Guard dans `__init__.py` si nom PyPI ≠ module |
| `VALIDATE_STATE_SCRIPT_J1` | 010 | Script GO/NO-GO versionné dès Session 1 |
| `ARCHITECTURE_GATE` | 010 | Architecture → review → prompt → implémentation |
| `PROVISOIRE_TRACKE` | 010 | Valeur provisoire → version cible dans CHANGELOG |

---

## Catalogue des recadrages humains — corpus complet (Q7)

| Session | Recadrage | Type | Dérive évitée |
|---------|-----------|------|---------------|
| 001 | "Blockchain n'a pas de problème concret" | over-engineering | Infrastructure inutile |
| 002 | "Tu es tombé dans le piège manifesto" | optimisation_locale | Document centralisation |
| 003 | "Toi infra, moi business logic" | production_avant_validation | Code NixOS non testable |
| 004 | "Grande respiration × 7" | optimisation_locale | Fix ponctuel × 6 sans vision |
| 005 | "C'est du fake code, on arrête" | promesse_sans_implementation | Scripts illustratifs |
| 005 | "Je lis 54 failed, pas 82 passed" | optimisation_locale | Décision sur métrique fausse |
| 006 | "103/104 n'est pas la perfection" | invisibilisation_dette | Standard qualité dilué |
| 007 | "Pas de balayage sous tapis" | invisibilisation_dette | Dette mypy cachée |
| 007 | "Comprendre POURQUOI avant corriger" | production_avant_validation | Script auto sans diagnostic |
| 008 | "Approche radicale sinon demain" | over-engineering | 4e itération pytest-cov |
| 008 | "Test manuel d'abord" | production_avant_validation | Script avant confirmation |
| 009 | "Surcomplexification du contenant" | over-engineering | 0 lignes code / 2000 lignes tooling |
| 009 | "Claude Code adorera ce logging (ironique)" | over-engineering | track_progress.py = bruit |
| 010 | "Ed25519 dépasse les objectifs" | over-engineering | PKI non disponible |
| 010 | "Reformulation : document officiel" | optimisation_locale | Destruction KB par nettoyage |

**Types observés (5 confirmés empiriquement) :**
- `over-engineering` — 6 occurrences
- `optimisation_locale` — 4 occurrences
- `production_avant_validation` — 3 occurrences
- `invisibilisation_dette` — 2 occurrences
- `promesse_sans_implementation` — 1 occurrence

**Note :** H003 d'ANAMNÈSE ("5 types probables") est validé empiriquement sur ce corpus.
Les 5 types couvrent les 15 recadrages sans résidu.

---

*KB_MIF_README_Index · Corpus complet 10/10 · Avril 2026*
*Voir KB_MIF_Value_Analysis.md · ANAMNESE_v0.3.md · rka_anamnese_node.yml*
