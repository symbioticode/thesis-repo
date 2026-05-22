## Formalisation — Protocole de Cohérence Cognitive Distribuée (PCCD)

### Préambule

Ce document formalise l'architecture conceptuelle émergée de la conversation. Il ne décrit pas un outil, ni un logiciel, ni une implémentation spécifique. Il décrit un **protocole** — un ensemble de règles invariantes qui gouvernent comment une unité de connaissance se représente, s'observe, et s'active, indépendamment de l'exécuteur (humain, agent, LLM) et de la couche technique sous-jacente.

Le protocole est distinct de tout système qui l'implémente. Les outils sont des vues sur les données. Le protocole est la grammaire qui rend ces vues cohérentes.

---

### Principe fondateur

> *Les outils sont des vues sur les données, jamais le conteneur des données. La séparation des responsabilités est la condition de survie d'un standard face aux innovations successives.*

Ce principe, emprunté à l'architecture des systèmes de trading algorithmique, s'applique intégralement aux systèmes de gestion de connaissance. Un standard qui survit n'est pas celui qui anticipe tous les outils futurs — c'est celui qui n'en dépend d'aucun.

---

### I. Le Pattern Tripartite Universel

L'observation centrale est la suivante : tout système de connaissance cohérent présente invariablement trois couches, trois états temporels, et trois modes de lecture. Ces dimensions sont orthogonales mais traversent le même espace.

**Dimension spatiale**

| Couche | Rôle | Analogie cognitive |
|--------|------|--------------------|
| Locale | Mémoire de travail active | Ce qui est manipulé maintenant |
| Distante | Archive long terme | Ce qui a été consolidé |
| Interférente | Mémoire associative | Ce qui relie les deux |

**Dimension temporelle**

| État | Portée | Fonction |
|------|--------|----------|
| Passé lointain | Archive froide | Référence stable, peu volatile |
| Passé proche | Contexte récent | Signal de continuité |
| Présent | État actif | Point d'action |

**Dimension d'exécution**

| Mode | Lecteur | Format privilégié |
|------|---------|-------------------|
| Narratif | Humain | Markdown, prose |
| Vectoriel | LLM / agent | Embeddings, clusters |
| Structuré | Les deux | YAML, TOML, JSON minimal |

Ces trois dimensions ne sont pas des choix d'implémentation. Elles sont des contraintes fondamentales que tout système de connaissance rencontre, qu'il les nomme ou non.

---

### II. Le Paradoxe de l'Auto-Référence et sa Résolution

#### Le problème

Un système documentaire qui veut être observable tombe inévitablement dans le paradoxe de Quine-Tarski : un système ne peut pas être son propre juge de vérité sans créer une boucle logique indécidable. Appliqué concrètement : un fichier ne peut pas déclarer lui-même qu'il est expiré, obsolète, ou pertinent. Ces états sont des relations entre le fichier et un observateur externe, jamais des propriétés intrinsèques.

Le problème de l'observateur en systèmes distribués ajoute une contrainte supplémentaire : un système qui s'observe lui-même perturbe ce qu'il observe. Les bonnes architectures d'observabilité (OpenTelemetry, D-SIG) ont résolu ce problème par une règle stricte.

#### La résolution — Asymétrie émetteur / interpréteur

**Le fichier émet. Il n'interprète jamais.**

Un fichier déclare uniquement des faits objectifs et datés : origine, date de création, dernière modification, contexte de production, relations déclarées. La conclusion — expiré, pertinent, redondant, prioritaire — appartient exclusivement à une entité tierce : un agent, un humain, une couche d'observabilité.

Cette asymétrie de rôles est non négociable dans un système honnête. Toute architecture qui la viole crée une dette cognitive invisible qui se manifeste plus tard sous forme d'incohérences inexplicables.

#### Le lien avec D-SIG

Le protocole D-SIG (Distilled Signal Standard) résout ce paradoxe pour les données externes (logs, traces, métriques) en distillant des signaux complexes en indicateurs de vitalité lisibles sans interprétation locale. Le présent protocole applique la même logique aux données documentaires internes : le document émet un signal de vitalité, un observateur externe produit le verdict.

---

### III. Architecture des Lectures Prioritaires

Plutôt qu'un index exhaustif qui tente de tout capturer (et devient rapidement inutilisable), le protocole définit trois niveaux de lecture en cascade. Un agent ou un humain n'accède au niveau N+1 que si le niveau N ne suffit pas à répondre à la question posée.

**Niveau 0 — Signal vital**

Trois champs maximum. Lisible sans ouvrir le fichier. Répond à : ce fichier existe-t-il, est-il intact, est-il récent ?

```
exists: true
hash: [md5]
last_modified: [timestamp]
```

**Niveau 1 — Contexte minimal**

Frontmatter du fichier. Lisible sans parser le contenu. Répond à : qui a produit ça, dans quel projet, pour quelle question ?

```yaml
origin: [projet source]
author: [humain ou agent]
created: [date]
domain: [domaine disciplinaire]
keywords: [3 à 5 termes]
summary: [2 phrases maximum]
relations: [liste de slugs liés]
```

**Niveau 2 — Contenu sémantique**

Le contenu réel, les liens profonds, les clusters thématiques. Nécessite une lecture complète ou un appel API. Réservé aux opérations de synthèse et de gap-analysis.

Cette cascade résout simultanément le problème de la lourdeur des index JSON et le problème de l'auto-référence : chaque niveau est interprété par l'entité qui l'interroge, jamais par le fichier lui-même.

---

### IV. Structure Physique du Système de Référence

La structure physique est neutre et stable. Elle ne reflète jamais les projets du moment, mais les types invariants de connaissance.

```
/knowledge/
  /_inbox/       ← zone de quarantaine, durée de vie nulle
  /corpus/       ← fichiers bruts, organisés par année d'ingestion
  /notes/        ← fiches .md, une par unité de connaissance
  /maps/         ← synthèses, cartes thématiques, research-front
  /assets/       ← images, données, tableaux extraits
  /archive/      ← traité, stable, ne bouge plus
  /meta/         ← index.json, hashes, registre des relations
```

La taxonomie thématique vit dans les métadonnées et les liens déclarés — jamais dans l'arborescence physique. Un fichier mal classé dans une arborescence thématique est perdu. Un fichier mal taggué dans un index plat est retrouvable.

---

### V. Les Skills du Protocole

Un skill est une procédure nommée, documentée en langage naturel, exécutable par un humain ou un agent sans ambiguïté. Les skills sont indépendants des outils qui les exécutent.

**`ingest`** — déclenché à chaque entrée dans `_inbox`. Extrait les métadonnées niveau 1 via API vision si nécessaire, génère un slug normalisé, crée la fiche `.md`, met à jour `meta/index`, déplace vers `/corpus/YYYY/`.

**`link`** — déclenché à la demande. Compare une fiche avec ses 20 voisines les plus proches dans l'index, propose des relations déclarées, met à jour le frontmatter.

**`weekly`** — déclenché chaque dimanche. Liste les ingestions de la semaine, identifie les thèmes émergents, met à jour `/maps/research-front.md`.

**`deduplicate`** — déclenché périodiquement. Compare les hashes MD5 et les titres normalisés, signale les doublons sans les supprimer.

**`gap-analysis`** — déclenché à la demande sur un thème. Croise l'index local avec une source externe (Semantic Scholar ou équivalent), identifie les zones non couvertes.

---

### VI. Les Invariants du Protocole

Ces règles ne peuvent pas être violées sans sortir du protocole.

1. **Séparation émetteur / interpréteur** — un fichier n'interprète jamais son propre état.
2. **Neutralité physique** — l'arborescence ne reflète pas les projets, elle reflète les types.
3. **Cascade de lecture** — niveau 0 avant niveau 1 avant niveau 2, sans exception.
4. **Portabilité absolue** — tout fichier de connaissance doit être lisible par un éditeur de texte sans aucun outil tiers.
5. **Index minimal** — l'index ne contient que ce qu'un agent peut lire en une seconde par entrée.
6. **Skill documenté** — aucune procédure n'existe si elle n'est pas écrite en langage naturel avant d'être automatisée.

---

### VII. Position dans le Paysage Existant

| Concept existant | Relation avec le protocole |
|-----------------|---------------------------|
| RAG | Implémentation possible du niveau 2, non substituable aux niveaux 0 et 1 |
| NAS | Infrastructure de stockage, couche en dessous du protocole |
| Obsidian / Zotero | Vues sur les données, jamais conteneurs |
| CLAUDE.md | Analogie directe : règles externalisées portées par un fichier, pas par l'agent |
| D-SIG | Protocole frère pour les données externes, même philosophie d'asymétrie |
| OpenTelemetry | Inspiration architecturale pour la séparation émission / interprétation |

---

### VIII. Ce que ce Protocole n'est pas

Il n'est pas un logiciel. Il n'est pas un format de fichier. Il n'est pas une taxonomie thématique. Il n'est pas dépendant d'un LLM spécifique. Il n'est pas une solution complète — c'est une grammaire qui rend cohérentes les solutions qui l'implémentent.

Le livrable final est double : le protocole lui-même (ce document, affiné) et une implémentation de référence dans le domaine documentaire qui prouve que les invariants tiennent sous charge réelle.

---

---

## Questionnaire — À soumettre aux instances concernées

Ces questions ont émergé naturellement de la conversation. Elles sont formulées pour être soumises telles quelles à un agent, un collaborateur, ou une session de travail ultérieure.

---

**Sur la structure et le pattern tripartite**

1. Les trois couches (locale / distante / interférente) et les trois états temporels (passé lointain / passé proche / présent) sont-ils vraiment orthogonaux, ou y a-t-il des cas où ils se confondent ? Existe-t-il des domaines où le pattern tripartite ne tient pas ?

2. Le pattern à trois temps détecté dans les trois projets modulaires est-il une contrainte fondamentale du problème, ou une contrainte cognitive de l'observateur qui l'a construit ?

3. Quelle est l'unité atomique minimale du protocole — le fichier `.md` avec frontmatter, le schéma YAML de contexte, le `.toml` de projet, ou autre chose ?

**Sur l'auto-référence et l'observabilité**

4. Comment D-SIG résout-il concrètement la frontière entre signal émis et interprétation produite ? Y a-t-il des cas limites où cette frontière devient floue dans l'implémentation v0.5 ?

5. Quels sont les signaux vitaux minimaux (niveau 0) qu'un fichier documentaire doit émettre pour être observable sans jamais s'auto-interpréter ?

6. L'asymétrie émetteur / interpréteur tient-elle quand l'interpréteur est lui-même un fichier du système (une carte thématique qui agrège d'autres fiches) ? Ou faut-il introduire une couche supplémentaire ?

**Sur les formats et métadonnées**

7. Quel est le schéma exact du frontmatter niveau 1 qui couvre tous les cas d'usage sans devenir lourd ? Quels champs sont vraiment invariants, lesquels sont optionnels ?

8. Le format TOML pour les fichiers de projet et YAML pour les fiches de connaissance — cette distinction de format reflète-t-elle une distinction de rôle, ou est-ce une convention arbitraire qu'on peut unifier ?

9. Comment le format TOON s'articule-t-il avec les niveaux 0, 1 et 2 de lecture prioritaire ? Est-il un format de niveau 1, de niveau 2, ou traverse-t-il les trois ?

**Sur le protocole comme standard**

10. Quelle est la différence opérationnelle entre le protocole PCCD et D-SIG ? Sont-ils destinés à fusionner, à rester distincts, ou à former une famille de protocoles avec une spécification parente commune ?

11. Quelle implémentation minimale suffit à prouver que les six invariants tiennent sous charge réelle ? Quel est le seuil de volume documentaire à partir duquel le protocole montre sa valeur différentielle par rapport à une organisation manuelle ?

12. Comment garantir que le protocole reste lisible et actionnable par un humain sans aucun outil — y compris quand les agents qui l'utilisent deviennent plus capables que les conventions initiales ne l'anticipaient ?

**Sur la gouvernance du standard**

13. Qui est l'entité tierce légitime pour juger de l'expiration, de la pertinence, et de la redondance des unités de connaissance ? Un agent dédié, un humain en boucle, ou une règle déclarative dans le protocole lui-même ?

14. Comment versionner le protocole sans casser les implémentations existantes — et quelle est la politique de rétrocompatibilité minimale pour qu'il reste un standard plutôt qu'un outil ?

15. À quel moment une implémentation du protocole devient-elle suffisamment robuste pour être proposée comme référence à d'autres systèmes — et qui décide de ce seuil ?