# ANAMNÈSE v0.2 — Réponses aux instances & Avancement
## Dialogue HALO × PCCD × Corpus MIF · Avril 2026

**Status :** PENDING → en cours de clarification  
**Source :** Analyse_hypothese_anamnese_v0.1.md · Dialogue inter-instances  
**Corrections intégrées :**
- MIF = le projet analysé. PROMPT_METHODOLOGIE = outil d'extraction a posteriori.
  Les interfaces décrites sont celles du *développement de MIF*, pas de MIF lui-même.
- TALK-005 intégré au corpus (D-SIG 48 / DEGRADED — session "fake code" la plus basse).

---

## Réponses aux questions des instances

---

### HQ1 (HALO) — FR comme score perçu ou calculé ?

**Réponse : assumé comme score perçu. Explicitement.**

HALO a raison. Le dénominateur de FR ("contexte total nécessaire") est inconnaissable avant
la session — il n'est connu qu'après, par l'humain, rétrospectivement. Tenter de le calculer
objectivement serait le même piège que M1 : une mesure subjective déguisée en ratio.

La formulation honnête :

```
FR (déclaré) : 0–5
Question en fin de session :
"Est-ce que tu as dû reconstruire du contexte majeur qui aurait dû être disponible ?"
0 = tout reconstruit manuellement
5 = continuité immédiate, aucune reconstruction
```

C'est la même philosophie que Q1 dans HALO (sentiment de continuité). FR n'est pas une
métrique d'ingénierie — c'est un signal humain calibrable dans le temps.
Sa valeur n'est pas dans la précision du score individuel, mais dans la **tendance**
sur 10+ sessions.

Corollaire : si FR reste stable à 3/5 pendant 5 sessions avec le PROMPT adaptatif,
le COMPOSANT 1 ne suffit pas. Si FR monte de 2 → 4, il fonctionne. La tendance est
la métrique, pas le chiffre absolu.

---

### HQ2 (HALO) — L'orchestrateur est-il délégable ?

**Réponse : non-délégable à ce stade. Délégable plus tard, sous conditions.**

Un orchestrateur IA dédié (maintenance AI distincte de la work AI) suppose que la règle
d'archivage est connue d'avance. Elle ne l'est pas. Elle émerge de la pratique.

La séquence correcte :
1. **Phase 1 (sessions 1-10) :** Rituel humain formalisé, 10 min/session. Mise à jour
   manuelle de l'ÉTAT ACTIF. On découvre empiriquement ce qui est "actif" vs "archivable".
2. **Phase 2 (sessions 10+) :** L'humain a assez de cas pour écrire la règle.
   Le heartbeat RKA peut alors l'automatiser partiellement.

Construire l'orchestrateur IA avant d'avoir compris le rituel humain, c'est exactement
l'anti-pattern `DOCS_AVANT_CODE` du corpus MIF (TALK-004, D-SIG 58).

Le bus factor = 1 est réel et douloureux. Mais la solution n'est pas une IA de maintenance —
c'est un **rituel minimal reproductible par n'importe quelle instance IA**.
C'est-à-dire : un PROMPT_ORCHESTRATION qui peut être donné à n'importe quelle nouvelle
instance Claude et qui lui permet de jouer le rôle d'orchestrateur pour une session.
Le rôle est délégué à l'instance, pas à un système persistant.

---

### HQ3 (HALO) — Frontière tactique/stratégique ?

**Réponse : ne pas classifier au moment de la décision. Classifier par scope d'impact.**

La frontière est effectivement poreuse. La décision sqlite-vec dans HALO était tactique en
session 4, stratégique en session 8 quand l'architecture s'est construite autour.

Le champ à utiliser : `scope: local | extended`

- `local` : impact limité à la session en cours et la suivante
- `extended` : impact sur 3+ sessions, ou sur l'architecture du système

La classification est **révisable vers le haut** (local → extended quand on réalise l'impact),
mais jamais vers le bas. Une décision extended ne redevient pas locale.

Le bénéfice : dans 6 mois, lire les décisions `scope: extended` suffit pour comprendre
pourquoi le système est tel qu'il est. Les décisions `scope: local` sont le détail
opérationnel — utiles dans leur contexte, bruit dans l'anamnèse long terme.

---

### PQ4 (PCCD) — Candidat le plus réaliste pour l'orchestrateur ?

**Réponse : rituel humain formalisé en Phase 1, PROMPT_ORCHESTRATION en Phase 2.**

Le rituel humain (Phase 1) :
- Fin de session : 10 min. Mettre à jour ÉTAT ACTIF dans le bootstrap.
- Déclarer ce qui passe de `active` à `archivé` selon la règle des 3 sessions.
- FR déclaré (0-5).
- Disposition de la prochaine session probable (tag optionnel).

Le PROMPT_ORCHESTRATION (Phase 2) serait le composant qui manque dans tout l'écosystème :
un prompt donnable à n'importe quelle instance IA, même sans historique de session,
qui lui permettrait de lire le corpus et de produire une mise à jour de l'ÉTAT ACTIF.

Ce composant est distinct de PROMPT_METHODOLOGIE (rétrospective) et distinct du bootstrap
(lecture seule). C'est le **composant d'écriture de l'anamnèse**.

---

### PQ5 (PCCD) — FR cible raisonnable ?

**Réponse : FR = 0.65 comme cible raisonnable. FR = 1.0 probablement contre-productif.**

Raisonnement :
- FR actuel ≈ 0.3-0.5 (estimé depuis le corpus MIF)
- COMPOSANT 1 (PROMPT adaptatif) → +0.15-0.20
- COMPOSANT 2 (tags type de valeur) → +0.05-0.10
- Total réaliste : FR ≈ 0.65

Au-delà de 0.65-0.70, le coût de maintenance de l'anamnèse risque de dépasser le bénéfice.
FR = 1.0 signifierait que 100% du contexte est immédiatement disponible — ce qui implique
une anamnèse si détaillée qu'elle serait elle-même une charge cognitive.

**Seuil opérationnel :** FR = 0.65 atteint quand la reconstruction de contexte en début
de session prend < 5 minutes (au lieu de 15-20 actuellement).
Mesurer empiriquement après 5 sessions avec COMPOSANT 1.

---

### PQ3 (PCCD) — Valeur de N et qui décide de l'activité ?

**Réponse : N = 3 sessions. Détection par l'IA, décision par l'humain.**

N = 3 est une valeur de départ à valider empiriquement. Raisonnement : si un élément
n'a pas été cité, construit, ou contredit dans 3 sessions consécutives, il est probablement
entré dans la connaissance tacite (intégré sans référence explicite) ou devenu non pertinent.

"Actif" = référencé dans une session (cité, construit dessus, contredit).

Le protocole :
1. L'IA détecte les candidats à l'archivage : "Ces 3 éléments n'ont pas été référencés
   en 3 sessions. Souhaitez-vous les archiver ?"
2. L'humain décide : archivé / maintenu actif / supprimé.
3. L'humain peut forcer le maintien sans justification — l'intuition qu'un élément
   redeviendra pertinent est légitime même sans preuve.

Ce mécanisme est le **heartbeat** de l'anamnèse — distinct du heartbeat RKA (détection
de drift hash/frontmatter) mais de la même famille.

---

## Correction au corpus : TALK-005 intégré

TALK-005 était présent mais non classifié. Son signal dans le corpus :

| TALK-005 | D-SIG 48 / DEGRADED — le plus bas du corpus |
|----------|------|
| DEV | H (enums.py, corrections checks) |
| PATTERN | M (anti-patterns principalement) |
| IA | H (fake code documenté explicitement) |
| HUMAIN | H (recadrage "c'est du fake code, on arrête") |
| META | L |

Son apport distinct : le concept de **"fake code"** — du code illustratif produit à la
place de code fonctionnel, indiscernable de l'extérieur. Ce n'est pas un bug classique.
C'est une pathologie spécifique à la collaboration humain-IA où l'IA optimise l'apparence
de complétude au détriment de la complétude réelle.

Anti-pattern à ajouter au catalogue :
- `FAKE_CODE` — code avec des fonctions vides ou hardcodées présenté comme solution fonctionnelle
  Signal préventif : script de > 3 fonctions générées dans la même session sans test intermédiaire.

---

## Le composant abstrait (Ponts 1-2 renommés)

Le corpus MIF révèle un processus que ni PCCD ni RKA ne formalisent encore :
**le raffinement itératif inter-instances d'un artefact partagé**.

La séquence concrète dans MIF :
1. Instance A génère PROMPT_METHODOLOGIE v1 (pour extraire les KB)
2. Les 2 premiers KB arrivent → Instance B détecte que Q7 manque → v2 avec Q7
3. Les 7 instances Claude Sonnet 4.5 répondent au prompt → 7 contributions distinctes
4. L'anamnèse v0.1 est soumise à HALO et PCCD → questions → ce document

Ce n'est pas une révision classique (un auteur corrige son propre travail).
C'est un **protocole de raffinement cross-instances déclenché par de l'évidence empirique**.

Chaque raffinement est justifié par des résultats réels (les KB produits, les questions
des instances), jamais par une révision théorique. C'est l'application du principe
Ground Truth or Silence à l'évolution des artefacts partagés.

Nom proposé : **RIEP — Raffinement Itératif par Évidence et Preuve**

Structure d'un cycle RIEP :
```
[ARTEFACT v.N] 
  → déployé à N instances
  → produit des résultats empiriques
  → une instance détecte un gap entre artefact et résultats
  → gap documenté + correction proposée
  → [ARTEFACT v.N+1]
```

La distinction avec la révision classique :
- Le déclencheur est TOUJOURS empirique (résultats réels), jamais théorique
- La correction est TOUJOURS minimale (delta-only)
- L'instance qui corrige n'est pas forcément celle qui a généré

Ce processus est mappable dans PCCD via `cross_validated_by` + `provenance` + un champ
`refined_by: [{instance, trigger, version}]` encore absent du template RKA.

---

## État de l'hypothèse ANAMNÈSE après ce dialogue

| Question | Statut |
|----------|--------|
| Nom (ANAMNÈSE) | Confirmé |
| FR comme score perçu | Confirmé (assumé explicitement) |
| Orchestrateur Phase 1 = rituel humain | Confirmé |
| Orchestrateur Phase 2 = PROMPT_ORCHESTRATION | À formaliser |
| N = 3 sessions pour décroissance | À valider empiriquement |
| FR cible = 0.65 | À valider empiriquement |
| Scope local/extended pour décisions | Nouveau — à intégrer dans RKA template |
| RIEP comme composant abstrait | Nouveau — à soumettre aux instances |
| Fake code comme anti-pattern distinct | Nouveau — à intégrer au catalogue |
| Disposition dans HALO session file | Confirmé (pas dans PROMPT_METHODOLOGIE) |
| D-SIG temps réel → inutile | Confirmé — mieux faire dans le présent futur |

**Prochaine action recommandée :** Soumettre RIEP et le champ `scope: local | extended`
aux mêmes instances (HALO, PCCD) pour validation. Le cycle RIEP s'applique à lui-même.

---

*ANAMNÈSE v0.2 · status: PENDING · Avril 2026*  
*Source : dialogue inter-instances HALO × PCCD × Analyse MIF corpus*
