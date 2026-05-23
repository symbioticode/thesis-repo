# ANAMNÈSE v0.3
## Protocole de continuité cognitive inter-sessions

**Status :** PENDING
**Créé :** Avril 2026 · v0.1
**Cette version :** v0.3 · 2026-04-26
**Provenance :** Dialogue Andrei + Claude Sonnet 4.6 · Corpus MIF 7/10 sessions · Instances HALO + PCCD
**Supersedes :** ANAMNÈSE v0.2

---

## Changelog v0.1 → v0.3

| Version | Apport |
|---------|--------|
| v0.1 | Nom, FR 0-5, trois acteurs, périmètre, quatre composants, RIEP |
| v0.2 | Réponses HALO/PCCD, C1/C2/C3 remplace FR, RIEP formalisé, relation HALO clarifiée |
| v0.3 | Dual observer inscrit comme invariant, relation HALO/ANAMNÈSE fixée causalement, Phase 2 HALO comme précondition, interfaces transversales synthétisées, upgrade ground disponible |

---

## 1. Définition

ANAMNÈSE est un protocole de continuité cognitive pour les collaborations humain-IA
sur plusieurs sessions. Il répond à une question unique :

> **Comment faire en sorte qu'une nouvelle instance IA puisse continuer un travail
> plutôt que le recommencer ?**

Ce n'est pas de la documentation. Ce n'est pas une mémoire. C'est du **contexte activable** —
la différence entre un chirurgien qui lit le dossier du patient avant d'opérer
et un chirurgien qui découvre le patient sur la table.

---

## 2. Nom

Du grec ἀνάμνησις — "non-oubli".

Deux sens convergents :
- **Médical** : recueil des antécédents qui conditionne le diagnostic. L'anamnèse présuppose
  un praticien partiellement informé — elle n'est pas lisible par un étranger complet.
- **Platonicien** : apprendre est se souvenir de ce qu'on savait déjà. La connaissance
  n'est pas retrouvée — elle est réactivée.

Les deux s'appliquent. ANAMNÈSE présuppose un contexte minimal chez le lecteur.
C'est sa force (concision) et sa limite (non-portabilité totale).

---

## 3. Métrique : le triplet C1/C2/C3

*(Contribution HALO — empirique, observé en sessions réelles)*

FR n'est pas un score 0-5. C'est un triplet binaire avec deux observateurs distincts.

| Condition | Énoncé | Observateur |
|-----------|--------|-------------|
| **C1** | Le protocole a été reconnu sans réexplication | Humain |
| **C2** | Au moins un pattern de `profil_stable` reconnu spontanément dans les 10 premiers échanges | IA |
| **C3** | La prochaine action était claire sans négociation | Humain |

**Règle d'interprétation :**
- C1 + C2 + C3 = continuation
- 2/3 = continuation dégradée
- 1/3 ou moins = redémarrage fonctionnel

**Invariant de séparation :** C2 et (C1, C3) ne sont jamais agrégés en un score unique.
C2 est vérifiable uniquement par l'IA. C1 et C3 sont vérifiables uniquement par l'humain.
Les agréger masquerait exactement le diagnostic qu'on cherche.

Cette séparation est structurelle, pas une convention. HALO l'avait implicitement
résolu (Q1 humain, Q2 IA, jamais agrégés) avant qu'ANAMNÈSE le nomme.

---

## 4. Les acteurs

### Trois permanents

**L'humain** porte ce que le protocole ne peut pas capturer : le sens (pourquoi ça compte),
la disposition temporelle (ce qui est urgent maintenant), le jugement contextuel
("c'est correct pour ce moment"), la tolérance au risque. Il est aussi le seul
capable de recadrage architecturalement fondé. Ce rôle n'est pas délégable.

**L'IA** apporte la production à haute vitesse, la cohérence locale, la détection de patterns,
l'implémentation des contraintes. Elle est fondamentalement amnésique entre les sessions.
Ce n'est pas un bug — c'est une propriété à intégrer dans l'architecture.

**Les documents** sont les acteurs les moins intelligents et les plus durables. Quand
l'humain oublie et que l'IA ne se souvient pas, les documents restent. Un document
bien formé (signal vital, contexte minimal, relations) réduit la charge de réactivation.
Un document mal formé augmente le bruit.

### Un absent : l'orchestrateur

Le rôle de maintenir l'anamnèse elle-même n'est assigné à personne formellement.
Actuellement assuré de façon informelle par l'humain. Bus factor = 1.

**Phase 1 (maintenant)** : rituel humain formalisé, 10 min/session.
Mettre à jour `anamnese_state.yaml` — ce qui avance, ce qui est bloqué,
ce qui est candidat à l'archivage.

**Phase 2 (après validation Phase 1)** : PROMPT_ORCHESTRATION — un prompt donnable
à n'importe quelle instance IA froide qui lui permet de jouer le rôle d'orchestrateur
pour une session. Le rôle est délégué à l'instance, pas à un système persistant.
Construire le PROMPT_ORCHESTRATION avant d'avoir compris le rituel humain serait
l'anti-pattern `DOCS_AVANT_CODE` appliqué à la méta-couche.

---

## 5. Périmètre

**Dans le périmètre :**
- Décisions architecturales et leurs raisons (le POURQUOI)
- Patterns nommés et validés (réutilisables)
- Anti-patterns documentés (les pièges rencontrés)
- Recadrages humains et leur type de déviation
- État épistémique actif (hypothèses en cours, questions ouvertes)
- Disposition de la session (tag descriptif, post-session, jamais prescriptif)

**Hors périmètre :**
- Le code (git)
- La documentation technique API (docs formelles)
- Les données et résultats de tests (système de fichiers)
- La vision long terme et stratégie (document de vision séparé)

**Frontière critique :** ANAMNÈSE n'est pas un résumé. C'est une interface entre sessions —
ce qui permet à une session N+1 d'être productive sans relire les sessions 1 à N-1.

---

## 6. Décroissance du contexte actif

Ce qui était critique en session N peut être archivé en session N+7.
Un système d'anamnèse statique accumule du bruit et fait baisser C1/C2/C3.

**Règle H001 (hypothèse, non validée) :** un élément non référencé dans 3 sessions
consécutives est candidat à l'archivage.

"Référencé" = cité, construit dessus, ou contredit dans une session.

**Protocole :** l'IA détecte les candidats, l'humain décide. L'humain peut maintenir
un élément sans justification — l'intuition qu'il redeviendra pertinent est légitime.
Jamais supprimer, toujours archiver.

---

## 7. RIEP — Raffinement Itératif par Évidence et Preuve

Composant abstrait observé dans le corpus MIF. Décrit le processus par lequel
un artefact partagé s'améliore à travers des instances multiples.

**Structure d'un cycle :**
```
[ARTEFACT v.N]
  → déployé à N instances
  → produit des résultats empiriques
  → une instance détecte un gap entre artefact et résultats
  → gap documenté + correction minimale proposée
  → [ARTEFACT v.N+1]
```

**Ce qui distingue RIEP d'une révision classique :**
- Le déclencheur est toujours empirique (résultats réels), jamais théorique
- La correction est toujours minimale (delta-only)
- L'instance qui corrige n'est pas forcément celle qui a généré

ANAMNÈSE v0.1 → v0.2 → v0.3 est lui-même un cycle RIEP.

---

## 8. Résidence et format invariant

**Où :** Git (GitHub/Gitea/GitLab) comme source de vérité.
**Format :** YAML pour le structuré, Markdown pour le narratif.
**Invariant :** lisible par un humain avec un éditeur de texte sans outil tiers (INV-04 PCCD).
**Indépendance :** aucune dépendance au LLM ou à l'agent. L'IA lit et produit, elle ne stocke pas.

**Fichier pivot :** `anamnese_state.yaml` — l'ÉTAT ACTIF mis à jour à chaque fin de session.
C'est le seul fichier qui fait la différence entre ANAMNÈSE et une collection de notes.

---

## 9. Interfaces transversales

### PCCD × ANAMNÈSE
- INV-01 : `anamnese_state.yaml` émet, l'instance interprète — jamais l'inverse
- Statuts épistémiques : KB articles reçoivent PENDING/CERTIFIED/DEPRECATED
- `cross_validated_by` : RIEP documente la convergence inter-instances
- Question ouverte (H005) : ANAMNÈSE est-elle instance-enfant de PCCD ou protocole pair ?

### RKA × ANAMNÈSE
- Niveau 0 : `anamnese_state.yaml` a signal/hash/last_modified
- Niveau 1 : KB articles ont type_valeur, disposition, scope
- `activation_mode` : éléments actifs = operative, archivés = contextual
- Skill `heartbeat` : détecte N=3 inactifs → propose archivage

### HALO × ANAMNÈSE
- HALO est une instance partielle d'ANAMNÈSE (60%), preuve de concept, pas implémentation
- La causalité est inversée : HALO (fév. 2026) a engendré ANAMNÈSE (avril 2026), pas l'inverse
- `protocols.yaml` : hôte des règles ANAMNÈSE
- `profil_stable.yaml` : source de C2
- Session YAML : point de mesure C1/C2/C3
- `memory/` : couche d'archive ANAMNÈSE
- Phase 2 analytique de HALO (memory.db) : ANAMNÈSE en est la précondition, pas le contenu

---

## 10. Hypothèses ouvertes (à valider empiriquement)

| ID | Hypothèse | Validation |
|----|-----------|------------|
| H001 | N=3 sessions pour décroissance | 10 sessions instrumentées : les candidats sont-ils effectivement obsolètes ? |
| H002 | FR cible = 0.65 — au-delà le coût > bénéfice | Corrélation (C1+C2+C3=3) × productivité sur 5+ mesures |
| H003 | 5 types de recadrages distincts | Catalogue après 10+ sessions avec Q7 documentés |
| H004 | PROMPT_ORCHESTRATION faisable | Test instance froide sur `anamnese_state.yaml` |
| H005 | ANAMNÈSE × PCCD : enfant ou pair | Soumettre aux 8 invariants PCCD — combien respectés ? |

---

## 11. Conditions de certification

ANAMNÈSE passe de PENDING à CERTIFIED quand :

- [ ] 5 sessions avec C1/C2/C3 documenté
- [ ] H001 (N=3) validé ou amendé par observation
- [ ] H002 (FR cible) calibré empiriquement
- [ ] 3+ recadrages catalogués avec leur type
- [ ] PCCD a répondu à H005
- [ ] Une instance froide a mis à jour `anamnese_state.yaml` avec succès

**Estimation : 5-8 sessions instrumentées.**

---

*ANAMNÈSE v0.3 · status: PENDING · 2026-04-26*
*Voir HALO_ANAMNESE_Upgrade.md pour l'implémentation concrète*
*Voir ANAMNESE_Instance_Perspective.md pour la perspective de cette instance*
