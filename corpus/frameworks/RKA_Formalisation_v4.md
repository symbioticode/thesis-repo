# RKA — Reflective Knowledge Architecture
## Formalisation v4.0 · Avril 2026

---

## Signal vital

| Champ | Valeur |
|---|---|
| role | container |
| status | CERTIFIED |
| signal | present |
| created | 2026-04-19 |
| supersedes | RKA v3.0 (Anthill Edition) |
| provenance | Dialogue Andrei + Claude Sonnet 4.6 · Synthèse PCCD + AP + EREK |
| activation_mode | operative |
| cross_validated_by | PCCD · AP · EREK · MIF |

---

## 1. Définition

RKA est le protocole de navigation et de réutilisation de la connaissance dans un écosystème distribué humain/IA.

Ce n'est pas un outil de documentation. C'est l'interface entre ce qui a été produit et ce qui peut être retrouvé, relu, réutilisé — par un humain ou par une IA — sans redécouverte.

**Ce que RKA fait :**
- Chaque nœud de connaissance déclare son signal vital, son contexte minimal, et ses relations
- Le graphe émerge de l'agrégation de ces déclarations — pas d'un registre central
- Une IA peut naviguer ce graphe sans deviner les relations
- Un humain peut lire n'importe quel nœud en trois niveaux de profondeur croissante

**Ce que RKA ne fait pas :**
- Il ne certifie pas la vérité du contenu — c'est le rôle de MIF
- Il ne prouve pas les invariants universels — c'est le rôle de PCCD
- Il ne génère pas les protocoles — c'est le résultat d'AP
- Il ne prescrit pas la vision — c'est le rôle d'EREK/CORAIL

---

## 2. Principe fondateur

> Les outils sont des vues sur les données, jamais le conteneur des données.
> Un nœud n'interprète jamais son propre état.
> Le graphe n'est pas conçu — il est découvert.

*(INV-01 et INV-08 PCCD · Principe EREK)*

---

## 3. Architecture des lectures — les trois niveaux

Hérité de PCCD. Invariant de structure non négociable.

### Niveau 0 — Signal vital
Lisible sans ouvrir le fichier. Trois champs suffisent pour décider si on continue.

```
exists: true | false
hash: [md5 du contenu]
signal: present | absent | void
```

- `present` : le nœud existe et son contenu est cohérent avec son hash
- `absent` : le nœud est référencé mais le fichier n'existe pas
- `void` : le nœud existe mais son contenu est vide ou non interprétable

### Niveau 1 — Contexte minimal
Frontmatter YAML. Lisible sans parser le contenu. Décision de lecture complète basée sur ce niveau.

Champs obligatoires : `role`, `status`, `signal`, `created`, `slug`, `domain`, `summary`

Champs recommandés : tous les champs de relations, d'épistémologie, et de statut définis dans le template YAML.

### Niveau 2 — Contenu sémantique
Contenu complet. Relations profondes. Clusters. Requiert lecture complète ou appel API. Ne pas accéder si le niveau 1 suffit.

---

## 4. Invariants RKA

Hérités de PCCD (INV-01 à INV-08), adaptés à RKA.

| ID | Invariant | Source |
|---|---|---|
| RKA-INV-01 | Séparation émetteur/interpréteur — un nœud ne lit jamais son propre état | PCCD INV-01 |
| RKA-INV-02 | Neutralité physique — la structure de fichiers reflète les types, jamais les projets | PCCD INV-02 |
| RKA-INV-03 | Cascade de lecture — niveau 0 avant niveau 1 avant niveau 2 | PCCD INV-03 |
| RKA-INV-04 | Portabilité absolue — lisible sans outil tiers, YAML brut suffit | PCCD INV-04 |
| RKA-INV-05 | Index minimal — un nœud identifiable en une seconde au niveau 0 | PCCD INV-05 |
| RKA-INV-06 | Skill documenté — toute procédure en langage naturel avant automatisation | PCCD INV-06 |
| RKA-INV-07 | Précondition de couche — niveau 0 invalide rend les niveaux supérieurs non évaluables | PCCD INV-07 |
| RKA-INV-08 | Non-réécriture — le nœud cite sa source, ne réécrit jamais sa sémantique | PCCD INV-08 |
| RKA-INV-09 | Déclaration décentralisée — chaque nœud déclare ses propres relations, pas de registre central | EREK |
| RKA-INV-10 | Trace d'émergence — tout protocole documente sa genèse par contrainte, pas par design | AP |

---

## 5. Statuts épistémiques

Hérités de PCCD. Cycle de vie complet d'un nœud de connaissance.

| Statut | Signification |
|---|---|
| `PENDING` | Hypothèse de travail — structure posée, non validée |
| `UNCERTIFIED` | Contenu présent mais provenance incomplète ou reconstruite |
| `CERTIFIED` | Validé — contenu, provenance et relations vérifiés |
| `VALID_INACTIVE` | Valide dans son contexte d'origine, non applicable actuellement |
| `TRANSITIONING` | En révision active — ni l'ancien ni le nouveau état n'est stable |
| `DEPRECATED` | Supplanté mais valide dans son contexte historique |
| `SUPERSEDED` | Remplacé par un nœud identifié dans `superseded_by` |
| `VOID` | Référencé mais vide ou non interprétable |

---

## 6. Skills candidats

| Skill | Déclencheur | Action |
|---|---|---|
| `ingest` | Entrée dans `_inbox` | Extrait niveau 1, génère slug, crée nœud, met à jour index |
| `link` | À la demande | Compare nœud avec 20 voisins, propose relations |
| `weekly` | Chaque dimanche | Thèmes émergents, met à jour `research-front.md` |
| `deduplicate` | Périodique | Compare hashes et titres, signale doublons sans supprimer |
| `gap-analysis` | À la demande / thème | Croise index local vs source externe |
| `heartbeat` | Mensuel | Détecte nœuds absents des digests + drift sémantique (hash vs frontmatter) |
| `certify` | À la demande | Valide syntaxe + sémantique + signature cryptographique |
| `rka-introspect` | Nouveau projet | Génère le YAML niveau 1 par introspection guidée IA + validation humaine |

---

## 7. Principes SYNERGIA — ancres sémantiques optionnelles

Pour les nœuds de l'écosystème Anthill. Optionnels pour les nœuds extérieurs.

| Principe | Aspects documentables |
|---|---|
| `FRUGALITY` | `MEMORY_EFFICIENCY` · `DATA_QUALITY_FIRST` · `MINIMAL_TOKENS` |
| `DECENTRALIZATION` | `NO_CENTRAL_COORDINATOR` · `AUTONOMOUS_AGENTS` |
| `EMERGENCE` | `STANDARDS_FROM_PRACTICE` · `BOTTOM_UP_DESIGN` |
| `ANTIFRAGILITY` | `FAULT_TOLERANCE` · `GRACEFUL_DEGRADATION` |
| `TRANSCENDENCE` | `CROSS_DOMAIN_APPLICABILITY` |

---

## 8. Relation humain/IA dans RKA

RKA formalise explicitement les rôles dans la boucle humain/IA.

**L'IA fait :** introspection guidée (génération du YAML niveau 1), détection de relations candidates, heartbeat (drift sémantique), navigation du graphe, réponse aux queries cross-nœuds.

**L'humain fait :** validation du niveau 1 généré, certification (signature), décision de statut, résolution des tensions (`tension_with`), arbitrage des duplicats.

**Ni l'un ni l'autre ne fait :** interpréter l'état d'un nœud depuis le nœud lui-même (RKA-INV-01).

---

## 9. Limites déclarées

| Limite | Description |
|---|---|
| Vocabulaire contrôlé | Les principes SYNERGIA fonctionnent dans l'écosystème Anthill. Vocabulaire libre en fallback pour les nœuds extérieurs. |
| Dérive sémantique | Deux nœuds peuvent nommer le même concept différemment. Skill `deduplicate` détecte, ne résout pas. |
| Maintenance | Le heartbeat détecte le drift hash/frontmatter. C'est une alerte, pas une résolution automatique. |
| Hallucination de relations | L'IA peut proposer des relations inexistantes. Validation humaine obligatoire sur `connections`. |
| PCCD reste PENDING | RKA adopte les invariants PCCD mais ne les certifie pas. La branche de réfutabilité reste ouverte. |

---

## 10. Ce que RKA n'est pas

RKA n'est pas un Knowledge Graph au sens W3C. Il ne requiert pas RDF/OWL.
RKA n'est pas un système de documentation — il ne remplace pas les READMEs.
RKA n'est pas un registre central — il n'y a pas de serveur maître.
RKA n'est pas un outil de certification de vérité — c'est le rôle de MIF.
RKA n'est pas la théorie universelle de la connaissance — c'est le rôle de PCCD.

---

*RKA Formalisation v4.0 · status: CERTIFIED · 2026-04-19*
*Voir RKA_Synthese_Discussion.md pour le contexte · Voir rka_node_template.yml pour l'implémentation*
