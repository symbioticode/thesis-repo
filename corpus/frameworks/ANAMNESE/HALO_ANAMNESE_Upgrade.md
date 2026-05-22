# HALO → ANAMNÈSE — Instructions de mise à jour
## Upgrade concret · Phase 1 · Avril 2026

**Statut :** Instructions opérationnelles — prêt à implémenter
**Durée estimée :** 1 session de 2h
**Dépendances :** Accès à /mnt/project/, Claude Code ou Claude.ai

---

## Ce qui change, ce qui reste

| Fichier | Action | Raison |
|---------|--------|--------|
| `protocols.yaml` | Modifier section `protocole_dashboard` | Remplacer Q1 par triplet C1/C2/C3 |
| `project_instructions_memoire_partagee.md` | Modifier section FIN DE SESSION | Ajouter mesure C1/C2/C3 |
| `sessions/YYYY-MM-DD.yaml` template | Modifier section `metriques` | FR → triplet |
| `anamnese_state.yaml` | **Créer** | ÉTAT ACTIF — nouveau fichier pivot |
| `profil_stable.yaml` | Aucun changement | Reste source de C2 |
| `dashboard_metriques.yaml` | Modifier Q1 | Remplacer par C1/C2/C3 |

---

## FICHIER 1 — Modifier `protocols.yaml`

### Section à remplacer (dans `protocole_dashboard`)

```yaml
# REMPLACER :
moment_fin_session:
  que_faire:
    - "Andrei note Q1 : sentiment de continuité"
      format: "Q1: X/5"

# PAR :
moment_fin_session:
  que_faire:
    - "Andrei note C1 : le protocole a été reconnu sans réexplication"
      format: "C1: oui | non"
    - "Andrei note C3 : la prochaine action était claire sans négociation"
      format: "C3: oui | non"
    - "Claude note C2 : au moins un pattern de profil_stable.yaml reconnu spontanément"
      format: "C2: oui | non [+ quel pattern]"
    - "Claude note M4 : violations protocoles"
      format: "M4: X violations"
```

### Section à ajouter (après `protocole_dashboard`)

```yaml
# AJOUTER :
protocole_anamnese:
  objectif: "Maintenir anamnese_state.yaml à jour à chaque session"

  fin_session_rituel:
    duree: "10 minutes"
    etapes:
      - "Lire anamnese_state.yaml"
      - "Mettre à jour section ETAT_ACTIF : ce qui a avancé, ce qui est bloqué"
      - "Déclarer les éléments candidats à l'archivage (non référencés depuis 3+ sessions)"
      - "Andrei valide ou conteste chaque candidat"
      - "Mettre à jour le tag disposition_prochaine_session"

  decroissance:
    regle: "Un élément non référencé dans 3 sessions consécutives est candidat à l'archivage"
    detecteur: "Claude détecte, Andrei décide"
    action_archivage: "Déplacer de ETAT_ACTIF vers section ARCHIVE dans anamnese_state.yaml"
    jamais_supprimer: true

  note: |
    Ce rituel remplace le 'protocole_dashboard moment_fin_session' partiel.
    Les deux coexistent : dashboard (30s métriques) + anamnèse (10min état actif).
```

---

## FICHIER 2 — Créer `anamnese_state.yaml`

Ce fichier est le cœur de l'upgrade. Il est lu EN PREMIER à chaque session, avant `protocols.yaml`.

```yaml
# ==============================================================================
# ANAMNÈSE — État actif
# Lu EN PREMIER. Mis à jour EN DERNIER.
# Ne jamais écraser — toujours amender.
# ==============================================================================

meta:
  version: "0.1.0"
  created: "2026-04-XX"
  last_updated: "2026-04-XX"
  updated_by: "Andrei + Claude"
  schema: "anamnese_v0.2"

# ------------------------------------------------------------------------------
# SIGNAL VITAL (Niveau 0 — lisible sans ouvrir)
# ------------------------------------------------------------------------------
signal: present
hash: ""  # md5 du contenu — à remplir après chaque mise à jour

# ------------------------------------------------------------------------------
# ÉTAT ACTIF (ce qui est vivant maintenant)
# Mis à jour à chaque fin de session. Décroît par inactivité (règle N=3).
# ------------------------------------------------------------------------------
etat_actif:

  decisions_en_cours:
    - id: "D001"
      decision: "Upgrade HALO vers ANAMNÈSE Phase 1"
      scope: extended
      sessions_depuis_reference: 0
      statut: en_cours

    - id: "D002"
      decision: "MIF Couche 2 — implémentation DAL"
      scope: extended
      sessions_depuis_reference: 0
      statut: en_cours

  hypotheses_ouvertes:
    - id: "H001"
      hypothese: "N=3 sessions pour décroissance du contexte actif"
      sessions_depuis_reference: 0
      a_valider_par: "observation empirique sur 5+ sessions"

    - id: "H002"
      hypothese: "FR cible raisonnable = 0.65"
      sessions_depuis_reference: 0
      a_valider_par: "mesure C1/C2/C3 sur 5+ sessions"

  questions_en_suspens:
    - "ANAMNÈSE est-elle enfant de PCCD ou protocole pair ?"
    - "PROMPT_ORCHESTRATION — quel format minimal ?"
    - "Catalogue de recadrages — 5 types à identifier empiriquement"

  patterns_actifs:
    - ref: "profil_stable.yaml#patterns_confirmes"
      note: "Les 4 patterns confirmés restent la source de C2"

  prochaine_session:
    disposition: "exécution"  # exploration | exécution | validation | urgence
    action_principale: "Implémenter DAL v4.9 — MIF Couche 2"
    contexte: "ANAMNÈSE Phase 1 upgradé, HALO instrumenté C1/C2/C3"

# ------------------------------------------------------------------------------
# ARCHIVE (éléments désactivés — ne jamais supprimer)
# Décroissance: 3 sessions sans référence → candidat → décision Andrei → ici
# ------------------------------------------------------------------------------
archive:
  - id: "A001"
    contenu: "Roadmap 12 semaines initiale MIF"
    archivé_le: "2026-01-02"
    raison: "Obsolète dès PROGRESSION.md v1"
    valeur_résiduelle: "leçon : ne pas écraser les roadmaps abandonnées"

# ------------------------------------------------------------------------------
# MÉTRIQUES ANAMNÈSE (historique C1/C2/C3)
# Rempli automatiquement à chaque fin de session
# ------------------------------------------------------------------------------
historique_fr:
  - session: "2026-04-XX"  # première session avec ANAMNÈSE
    C1: null
    C2: null
    C3: null
    note: "Baseline — avant upgrade"

# ------------------------------------------------------------------------------
# CATALOGUE RECADRAGES (à alimenter empiriquement)
# Format : type | signal_avant | recadrage | effet
# ------------------------------------------------------------------------------
recadrages_observes:
  # Alimenté au fil des sessions — ne pas inventer a priori
  []
```

---

## FICHIER 3 — Modifier le template session `YYYY-MM-DD.yaml`

### Section `metriques` — remplacer

```yaml
# REMPLACER :
metriques:
  M1: "X minutes"
  Q1: "X/5"
  Q2: "X occurrences"
  M4: "X violations"

# PAR :
metriques:
  M1: "X minutes"  # temps reconstruction contexte
  C1: "oui|non"   # protocole reconnu sans réexplication [humain]
  C2: "oui|non"   # pattern reconnu spontanément [IA] — préciser lequel
  C3: "oui|non"   # prochaine action claire sans négociation [humain]
  M4: "X violations"

  # Dérivé : continuation ou redémarrage ?
  type_session: "continuation | continuation_degradee | redemarrage_fonctionnel"
  # continuation = C1+C2+C3 tous oui
  # continuation_degradee = 2 sur 3
  # redemarrage_fonctionnel = 1 ou moins
```

### Section `anamnese_update` — ajouter en fin de template

```yaml
# AJOUTER :
anamnese_update:
  decisions_referencees: []      # IDs de D00X actifs dans cette session
  hypotheses_referencees: []     # IDs de H00X testés ou évoqués
  nouveaux_recadrages: []        # recadrages survenus [format: type + contexte]
  candidats_archivage: []        # éléments non référencés depuis 3 sessions
  disposition_prochaine: ""      # exploration | exécution | validation | urgence
```

---

## FICHIER 4 — Modifier `project_instructions_memoire_partagee.md`

### Section DÉBUT DE SESSION — remplacer

```markdown
## DÉBUT DE SESSION — Ordre de lecture

Lire dans cet ordre strict :

1. `anamnese_state.yaml` EN PREMIER
   - ÉTAT ACTIF : décisions en cours, hypothèses ouvertes, prochaine action
   - Disposition déclarée pour cette session
   - Candidats à l'archivage signalés

2. `protocols.yaml`
   - Gardes-fous et règles communication

3. `profil_stable.yaml`
   - Patterns confirmés (source de C2)

4. `sessions/recent/[DERNIERE_DATE].yaml`
   - Contexte session précédente
   - Métriques C1/C2/C3 de la dernière session
```

### Section FIN DE SESSION — ajouter bloc ANAMNÈSE

```markdown
## FIN DE SESSION — Protocole complet

### Étape 1 — Dashboard (30 secondes)
Andrei : C1, C3 (oui/non)
Claude : C2 (oui/non + quel pattern), M4

### Étape 2 — Mise à jour ANAMNÈSE (10 minutes)
Claude lit anamnese_state.yaml, propose :
- Ce qui a avancé dans ETAT_ACTIF (décisions, hypothèses)
- Candidats à l'archivage (non référencés depuis 3 sessions)
- Nouveau recadrage à documenter (s'il y en a eu)
- Disposition pour la prochaine session

Andrei valide ou corrige. Claude génère le YAML mis à jour.

### Étape 3 — Fichier session
Générer sessions/YYYY-MM-DD.yaml avec section anamnese_update remplie.
```

---

## ROADMAP GROUND — HALO ANAMNÈSE Phase 1

### Semaine 1 — Instrumentation

- [ ] Créer `anamnese_state.yaml` (template ci-dessus, rempli avec l'état actuel)
- [ ] Modifier `protocols.yaml` (section dashboard + protocole_anamnese)
- [ ] Modifier `project_instructions_memoire_partagee.md` (ordre de lecture + fin session)
- [ ] Faire une session test : mesurer C1/C2/C3 pour la première fois
- [ ] Documenter le résultat dans `historique_fr` de `anamnese_state.yaml`

### Sessions 2-5 — Validation empirique

- [ ] Mesurer C1/C2/C3 à chaque session
- [ ] Observer : est-ce que `type_session` est prédictible depuis le contenu du bootstrap ?
- [ ] Identifier le premier recadrage → le documenter dans `recadrages_observes`
- [ ] Tester la règle N=3 : y a-t-il des éléments candidats à l'archivage après 3 sessions ?

### Décision à la session 5

- Si C1+C2+C3 stables sur 3+ sessions → ANAMNÈSE Phase 1 validée → passer Phase 2
- Si C2 systématiquement à 0 → `profil_stable.yaml` ou bootstrap à réviser
- Si C3 systématiquement à 0 → `a_faire_prochaine_session` pas assez précis

### Phase 2 (déclenché par validation Phase 1)

- [ ] Écrire `PROMPT_ORCHESTRATION` — une instance IA peut mettre à jour `anamnese_state.yaml` sans historique
- [ ] Extraire les 5 types de recadrages depuis le catalogue accumulé
- [ ] Connecter `memory.db` (sqlite-vec) avec `anamnese_state.yaml` comme index sémantique

---

## Ce que cet upgrade prouve ou modifie pour ANAMNÈSE

Chaque session instrumentée alimente les hypothèses ouvertes :

| Hypothèse | Signal à observer |
|-----------|------------------|
| N=3 pour décroissance | Est-ce que les éléments sans référence depuis 3 sessions sont effectivement obsolètes ? |
| FR cible = 0.65 | Est-ce que 2/3 C positifs corrèlent avec une session productive ? |
| 5 types de recadrages | Combien de types distincts émergent après 10 sessions ? |
| PROMPT_ORCHESTRATION faisable | Une instance sans historique peut-elle mettre à jour `anamnese_state.yaml` correctement ? |

*HALO_ANAMNESE_Upgrade · Phase 1 · Avril 2026*
