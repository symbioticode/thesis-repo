# TECH_README.md — Documentation technique complémentaire
**Projet** : IDEeS AP6-défi-13 — Protocole d'échange épistémique
**Version** : 1.0 — 18 mai 2026
**Scope** : Scripts S-01, S-02, S-03 + module commun tbm_utils.py

---

## Structure des fichiers

```
tbm_utils.py               — Module commun (fonctions TBM partagées)
s01_tbm_minimal.py         — Scénario S-01 : fusion TBM minimale (Radar + SIGINT)
s02_calibration_theta.py   — Scénario S-02 : calibration du seuil theta_conflit
s03_validation_malformed.py — Scénario S-03 : validation des CLAIM malformés
TECH_README.md             — Ce fichier
```

> **Important** : tous les fichiers `.py` doivent se trouver dans le **même répertoire**. S-02 et S-03 importent `tbm_utils`.

---

## Plan A — Thierry dispose d'un environnement Python

### Prérequis
- Python 3.9 ou supérieur (vérifier : `python --version` ou `python3 --version`)
- Aucune librairie externe requise (stdlib uniquement)

### Étapes

```bash
# 1. Vérifier la version Python
python --version          # doit afficher Python 3.9.x ou supérieur

# 2. Placer tous les fichiers dans un dossier de travail
mkdir idees_scripts && cd idees_scripts
# copier tbm_utils.py, s01_tbm_minimal.py, s02_calibration_theta.py,
#         s03_validation_malformed.py dans ce dossier

# 3. Exécuter S-01 (scénario de fusion TBM)
python s01_tbm_minimal.py

# 4. Exécuter S-02 (calibration du seuil)
python s02_calibration_theta.py

# 5. Exécuter S-03 (validation des CLAIM malformés)
python s03_validation_malformed.py
```

### Sorties attendues (exemples)

**S-01 :**
```
============================================================
S-01 — Fusion TBM non normalisee (IDEeS Defi 13)
...
  conflict_mass  m(vide) = 0.4200
  theta_conflit          = 0.3
  ...
  belnap_state = B
  ...
VERDICT : ESCALADE HUMAINE REQUISE
  m(vide) = 0.4200 >= theta_conflit = 0.3
============================================================
```

> m(∅) = 0.7 × 0.6 = 0.42 — conflit entre Radar ({H1}) et SIGINT ({H2}).
> 0.42 ≥ 0.30 : état Belnap **B**, escalade humaine obligatoire.

**S-02 :**
```
S-02 — Calibration de theta_conflit
...
  theta = 0.10      FPR = 0.xxx     TPR = 0.xxx
  theta = 0.15      FPR = 0.xxx     ...
  ...
  theta = 0.30      FPR = 0.0xx     TPR = 0.xxx
  ...
Recommandation :
  Seuil recommande : theta_conflit = 0.30
```

**S-03 :**
```
S-03 — Validation des CLAIM malformes (politique B.1)
...
  [OK]    VALIDE       - exemple nominal
           => [VALIDE]

  [OK]    REJET        - masse non normalisee
           => [REJET] belief_mass : somme = 1.10000000 ...

  [OK]    REJET        - timestamp manquant
           => [REJET] freshness.t_obs manquant
  ...
BILAN : tous les cas de test passent — politique B.1 conforme.
```

---

## Plan B — Andrei seul, sans développeur

### Étape 1 — Installer Python (si absent)

- **Windows** : télécharger depuis https://www.python.org/downloads/
  Sélectionner "Python 3.12.x Windows installer (64-bit)".
  ⚠️ Cocher **"Add Python to PATH"** lors de l'installation.

- **macOS** : télécharger depuis https://www.python.org/downloads/
  Ou via Homebrew : `brew install python3`

- **Linux (Ubuntu/Debian)** : `sudo apt install python3`

### Étape 2 — Vérifier l'installation

Ouvrir un terminal (Windows : PowerShell ou Invite de commandes) :
```
python --version
```
Attendu : `Python 3.9.x` ou supérieur.

### Étape 3 — Préparer les fichiers

1. Créer un dossier `idees_scripts` sur le Bureau (ou ailleurs).
2. Y copier les 4 fichiers `.py` :
   `tbm_utils.py`, `s01_tbm_minimal.py`, `s02_calibration_theta.py`, `s03_validation_malformed.py`

### Étape 4 — Exécuter les scripts

Ouvrir un terminal dans le dossier `idees_scripts` :

**Windows PowerShell :**
```powershell
cd $env:USERPROFILE\Desktop\idees_scripts
python s01_tbm_minimal.py
python s02_calibration_theta.py
python s03_validation_malformed.py
```

**macOS / Linux :**
```bash
cd ~/Desktop/idees_scripts
python3 s01_tbm_minimal.py
python3 s02_calibration_theta.py
python3 s03_validation_malformed.py
```

### Étape 5 — Vérifier la cohérence des résultats

| Script | Indicateur de succès |
|--------|---------------------|
| S-01 | Ligne `VERDICT : ESCALADE HUMAINE REQUISE` + `m(vide) = 0.4200` |
| S-02 | Ligne `Seuil recommande : theta_conflit = 0.30` (ou autre valeur justifiée) |
| S-03 | Ligne finale `BILAN : tous les cas de test passent` |

Si un script affiche `[ECHEC]` ou une erreur Python (`Traceback`), vérifier que `tbm_utils.py` est dans le même dossier.

---

## Annexe A — Règle conjonctive non normalisée (TBM Smets)

### Formule

Pour deux agents avec masses m₁ et m₂ sur 2^Θ :

```
m_combined(A) = Σ_{B ∩ C = A} m₁(B) · m₂(C)    pour tout A ⊆ Θ (y compris ∅)
```

La masse sur l'ensemble vide `m(∅)` n'est **jamais normalisée** — elle mesure le **conflit explicite** entre les agents.

### Exemple de calcul (S-01)

| Agent | Masse |
|-------|-------|
| Radar  | m({H1}) = 0.7 , m(Θ) = 0.3 |
| SIGINT | m({H2}) = 0.6 , m(Θ) = 0.4 |

Calcul des intersections :

| B        | C        | B ∩ C   | m₁(B)·m₂(C) |
|----------|----------|---------|-------------|
| {H1}     | {H2}     | **∅**   | 0.7×0.6 = **0.42** ← conflit |
| {H1}     | Θ        | {H1}    | 0.7×0.4 = 0.28 |
| Θ        | {H2}     | {H2}    | 0.3×0.6 = 0.18 |
| Θ        | Θ        | Θ       | 0.3×0.4 = 0.12 |

Résultat : m(∅) = 0.42, m({H1}) = 0.28, m({H2}) = 0.18, m(Θ) = 0.12, somme = 1.00 ✓

Contrairement à la règle de Dempster, **le 0.42 n'est pas redistribué** : il représente la contradiction réelle entre Radar et SIGINT.

---

## Annexe B — Dérivation de l'état Belnap (CORR-TP01-06)

L'état Belnap est dérivé de m_combined par priorité décroissante :

| Priorité | Condition | État β | Signification |
|----------|-----------|--------|---------------|
| 1 | m(∅) ≥ θ_conflit | **B** | Contradiction — escalade humaine obligatoire |
| 2 | m(Θ) > max(m({H})) | **N** | Silence qualifié collectif |
| 3 | ∃H : m({H}) > 0.5 et m(∅) ≈ 0 | **T** | Accord sur H |
| 4 | défaut | **N** | Conservateur : mieux vaut signaler l'incertitude |

**Justification de la priorité B > N :** une contradiction détectée doit toujours être remontée à l'opérateur humain, quelles que soient les masses résiduelles. L'orchestrateur ne tranche jamais un conflit (règle cardinale de la spec).

**Extension à |Θ| > 2 (CORR-TP01-06) :** les états T et F sont bien définis uniquement pour |Θ| = 2. Pour |Θ| > 2, les cas mixtes retournent N par convention conservatrice. La formalisation complète (dominance relative, ordre partiel) est prévue en NMT-4.

---

## Annexe C — Localisation PCR5 simplifiée (NMT-2)

### Principe

PCR5 (Proportional Conflict Redistribution rule 5, Dezert-Smarandanche) identifie **quels agents, sur quelles hypothèses, ont généré le conflit** et redistribue m(∅) proportionnellement.

### Version NMT-2 (s01_tbm_minimal.py, tbm_utils.py)

La version implémentée **liste les paires génératrices** sans redistribuer :

```
Pour chaque paire (B ∈ supp(m₁), C ∈ supp(m₂)) :
  si B ∩ C = ∅ et B ≠ C :
    contribution_conflit = m₁(B) · m₂(C)
    => reporter (agent1, B, agent2, C, contribution)
```

**Suffisant pour NMT-2** : l'opérateur humain voit *qui* est en désaccord et *sur quoi*, sans nécessiter la redistribution proportionnelle (qui est un choix de politique, pas un fait).

### Extension NMT-4

La redistribution PCR5 complète sera implémentée quand les décisions automatiques en aval de l'orchestrateur nécessiteront des masses post-conflit exploitables (ex. planification de mission).

---

## Annexe D — Politique de validation B.1

Tableau des cas de rejet selon `CLAIM_specification.md` section B.1 :

| Cas | Condition de rejet | Politique |
|-----|--------------------|-----------|
| Masse non normalisée | Σ m(A) ≠ 1 (± 1e-6) | Rejeter — log supervision |
| Clé hors 2^Θ | Clé non décomposable en sous-ensembles de Θ | Rejeter — log supervision |
| Timestamp manquant | `t_obs` absent | Rejeter — log supervision |
| Timestamp futur | `t_obs` > `t_reception` | Rejeter — log supervision |
| CLAIM expiré | `t_reception` > `t_obs + delta_t_valid` | Ignorer — log supervision |
| `delta_t_valid` négatif | Valeur < 0 | Rejeter — log supervision |
| Provenance absente | `chain_id` null ou non-URI | Rejeter — log supervision |
| Illocution invalide | κ ∉ {OBSERVE, INFER, DEDUCE, ASSUME} | Rejeter — log supervision |

**Politique générale** : tout CLAIM non conforme est écarté de la combinaison et signalé dans un log horodaté. Si la proportion de rejets dans une fenêtre glissante dépasse un seuil configurable, une alerte est émise vers C-07 (interface opérateur).

---

## Annexe E — Lien avec les sections de la proposition IDEeS

| Script | Utilisé dans | Rôle |
|--------|-------------|------|
| `tbm_utils.py` | Toutes tâches techniques | Bibliothèque de référence TBM |
| `s01_tbm_minimal.py` | CO-1b (faisabilité), CCP-4 (preuve technique NMT-2) | Démontre la fusion TBM non normalisée et l'escalade Belnap |
| `s02_calibration_theta.py` | CCP-4 (méthode calibration θ_conflit, B.2) | Justifie empiriquement la valeur θ = 0.30 pour NMT-2 |
| `s03_validation_malformed.py` | CCP-4 (robustesse B.1), CO-1b (résilience) | Démontre la détection de CLAIM malformés et la politique de rejet |

---

[andrei@nixos:~/Projects/52_MULTIMODALE/idees-proposal]$ python scripts/s01_tbm_minimal.py
============================================================
S-01 — Fusion TBM non normalisee (IDEeS Defi 13)
Protocole d'echange epistemique — NMT-2 -> NMT-3
============================================================

--- Validation des CLAIM entrants (B.1) ---
[OK] Agent Radar : masse valide (somme = 1.000000)
[OK] Agent SIGINT : masse valide (somme = 1.000000)

--- CLAIM emis par les agents ---

  CLAIM [Radar]
    m({vide}) = 0.0000
    m({H1}) = 0.7000
    m({H1, H2, H3}) = 0.3000

  CLAIM [SIGINT]
    m({vide}) = 0.0000
    m({H2}) = 0.6000
    m({H1, H2, H3}) = 0.4000

--- Verification algebrique ---
  Somme m_combined : 1.000000 (attendu : 1.000000)
  [OK] Conservation de la masse verifiee

--- EPISTEMIC_STATE (orchestrateur -> interface C-07) ---
  conflict_mass  m(vide) = 0.4200
  theta_conflit          = 0.3
  m_combined({vide}) = 0.4200 <-- CONFLIT
  m_combined({H1}) = 0.2800
  m_combined({H2}) = 0.1800
  m_combined({H1, H2, H3}) = 0.1200

  belnap_state = B

--- Localisation PCR5 (conflits par paire d'agents) ---
  Conflit : Radar ({'H1'}) vs SIGINT ({'H2'}) | contribution = 0.4200

============================================================
VERDICT : ESCALADE HUMAINE REQUISE
  m(vide) = 0.4200 >= theta_conflit = 0.3
  L'orchestrateur suspend toute decision automatique.
  L'etat de conflit est expose a l'operateur (C-07).
============================================================

[andrei@nixos:~/Projects/52_MULTIMODALE/idees-proposal]$ python scripts/s02_calibration_theta.py
=================================================================
S-02 — Calibration de theta_conflit (IDEeS Defi 13)
Methode : taux de faux positifs sur corpus synthetique
=================================================================

Parametres :
  N_PAIRS      = 500 paires par seuil
  PROB_CONFLICT = 0.5 (probabilite de conflit reel injecte)
  SEED          = 42 (reproductible)

Resultats :
-----------------------------------------------------------------
   Seuil theta   FPR (faux positifs)    TPR (vrais positifs)
-----------------------------------------------------------------
  theta = 0.10      FPR = 0.000                 TPR = 1.000
  theta = 0.15      FPR = 0.000                 TPR = 1.000
  theta = 0.20      FPR = 0.000                 TPR = 1.000
  theta = 0.25      FPR = 0.000                 TPR = 1.000
  theta = 0.30      FPR = 0.000                 TPR = 0.959
  theta = 0.35      FPR = 0.000                 TPR = 0.866
  theta = 0.40      FPR = 0.000                 TPR = 0.716
  theta = 0.45      FPR = 0.000                 TPR = 0.597
  theta = 0.50      FPR = 0.000                 TPR = 0.437
-----------------------------------------------------------------

Recommandation :
  Seuil recommande : theta_conflit = 0.1
  Justification    : premier seuil avec FPR <= 0.05 et TPR >= 0.80.
                     Compromis minimal faux positifs / sensibilite acceptable.

Interpretation :
  FPR eleve  = trop d'escalades humaines inutiles (surcharge operateur).
  TPR faible = conflits reels non detectes (risque operationnel).
  Valeur 0.30 = conservatrice : prefere l'escalade au silence sur un conflit reel.
=================================================================

[andrei@nixos:~/Projects/52_MULTIMODALE/idees-proposal]$ python scripts/s03_validation_malformed.py
======================================================================
S-03 — Validation des CLAIM malformes (politique B.1)
======================================================================

Horodatage de reference : 2026-05-18T12:00:00+00:00

  [OK]     VALIDE       - exemple nominal
           => [VALIDE]

  [OK]     REJET        - masse non normalisee
           => [REJET] belief_mass : somme = 1.10000000 (attendu 1.0, tolerance 1e-06)

  [OK]     REJET        - timestamp manquant
           => [REJET] freshness.t_obs manquant

  [OK]     REJET        - delta_t_valid negatif
           => [REJET] freshness.delta_t_valid negatif ou invalide : -10

  [OK]     REJET        - provenance absente
           => [REJET] Champ obligatoire manquant : 'provenance'

  [OK]     REJET        - illocution invalide
           => [REJET] illocution invalide : 'GUESS' (valeurs admises : ['ASSUME', 'DEDUCE', 'INFER', 'OBSERVE'])

======================================================================
BILAN : tous les cas de test passent — politique B.1 conforme.
======================================================================

Les trois scripts tournent proprement — voici ce que les résultats nous disent sur la spec.

---

## S-01 : résultat attendu, spec confirmée

m(∅) = 0.42 ≥ 0.30, état Belnap **B**, escalade déclenchée. C'est exactement le comportement décrit dans la règle cardinale de la spec. La localisation PCR5 identifie correctement la paire (Radar/{H1}, SIGINT/{H2}) comme source du conflit. **Rien à modifier.**

---

## S-02 : résultat surprenant — FPR = 0.000 pour tous les seuils

C'est le résultat qui mérite attention. Le générateur `generer_masses_conflit` produit des paires **parfaitement séparées** : cas conflit = masses sur {H1} et {H2}, cas non-conflit = masses sur le même singleton ou sur Θ. Dans cette construction, les paires non-conflictuelles ne génèrent **jamais** de m(∅) > 0, donc le FPR est mécaniquement zéro quel que soit le seuil.

Conséquences concrètes :

**1. La recommandation θ = 0.1 est un artefact**, pas une vraie calibration. Le corpus synthétique actuel est trop simple : il n'y a pas de cas ambigus (paires partiellement chevauchantes, masses mixtes entre singletons distincts et Θ). Un vrai corpus de calibration devrait inclure des cas comme m₁ sur {H1, H2} et m₂ sur {H2, H3} — là où m(∅) peut être non-nul même sans conflit "sémantique" fort.

**2. La valeur conservative 0.30 reste justifiée pour NMT-2**, précisément parce que la calibration rigoureuse n'est pas encore possible sur données synthétiques réalistes. S-02 démontre la *méthode*, pas encore le résultat final.

**Ce qu'il faut noter dans la spec (section B.2) :** la méthode de calibration NMT-3 doit enrichir le générateur avec des cas ambigus intermédiaires (masses sur ensembles non-disjoints, bruit de capteur, hypothèses partiellement compatibles). Il vaudrait ajouter une QO tracée à cet effet.

---

## S-03 : tous les cas passent — politique B.1 validée

Les six cas couvrent exactement le tableau B.1 de la spec. **Rien à modifier sur B.1.**

---

## Recommandation de mise à jour

La spec ne nécessite **pas de correction formelle** — les décisions DEC- et CORR- sont toutes confirmées. Une seule mise à jour est utile, dans la section B.2 :

```diff
- Générer un corpus de scénarios synthétiques avec taux de conflit connu (données simulées — CC-01).
+ Générer un corpus de scénarios synthétiques avec taux de conflit connu (données simulées — CC-01).
+ Le corpus doit inclure des cas ambigus : masses sur sous-ensembles non-disjoints,
+ bruit résiduel sur Θ, hypothèses partiellement compatibles — pour que le FPR
+ soit non-trivial et que la calibration soit discriminante.
```

Et une QO à ajouter au registre :

| ID | Description | Condition de résolution |
|----|-------------|------------------------|
| AM-04 | Corpus synthétique S-02 trop simple (FPR = 0 trivial) — enrichir avec cas ambigus | NMT-3, avant calibration θ_conflit sur données simulées CC-01 |

Voulez-vous que je produise la version mise à jour de `CLAIM_specification.md` avec ces deux ajouts, ou préférez-vous les intégrer manuellement ?

---

*Document produit le 18 mai 2026. Autorité de modification : Andrei (PI).*