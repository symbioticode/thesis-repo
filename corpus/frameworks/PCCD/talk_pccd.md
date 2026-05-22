Très bonne question — les documents que tu as partagés permettent d'y répondre avec pas mal de nuance. Voici mon analyse.

---

## OpenCode vs Claude Code : les vraies vérités

**Claude Code** s'est imposé comme la référence non pas parce qu'il est le plus riche en features, mais parce qu'il a changé la façon de penser le développement. La pratique du `claude.md`, des `skills.md`, la gestion de projet à l'échelle du projet entier plutôt que module par module — ce sont des comportements que Claude Code a introduits dans les workflows de dev. Il a bifurqué le travail vers le terminal d'une façon qui n'imposait pas à l'IDE, tout en étant beaucoup plus accessible qu'Aider.

**OpenCode** est genuinement impressionnant : multimodèle (Anthropic, OpenAI, Gemini, Mistral, Ollama, LM Studio...), open source, écrit en Go, compatible LSP, avec un système d'agents configurables, et une interface TUI propre. La vidéo de Korben le montre bien — on peut y connecter Qwen 3, DeepSeek R1, GPT-OSS... et ça coûte 0€ si on tourne en local.

**Le vrai problème d'OpenCode** : Anthropic a banni les applications tierces d'accéder à la tarification subsidisée des abonnements. OpenCode ne peut donc plus utiliser Opus ou Sonnet au "prix subscription" — il doit passer par l'API au tarif plein. C'est là que la controverse éclate. Anthropic est dans son droit, mais ça crée une asymétrie : Claude Code seul bénéficie de ce levier économique.

**Les modèles locaux via Ollama** (Gemma 4, Qwen 3 Coder, DeepSeek R1, GLM 4) : efficaces pour des tâches ciblées et modulaires, mais loin d'Opus 4 sur la qualité globale. La recommandation dans les vidéos est juste — travailler composant par composant, garder les fichiers sous 600 lignes, une tâche par session. C'est précisément parce que le contexte réduit masque les limites des petits modèles.

---

Voici une carte des outils et pour quel besoin ils s'adaptent :---

--> agent_coding_landscape.svg

## Pronostic vital pour les trois grands

**Cursor / Windsurf — survie sous pression.** Ces outils ont un vrai avantage UX : l'IDE fork permet de garder des développeurs qui ne veulent pas quitter leur environnement visuel. Mais leur modèle économique est attaqué des deux côtés — par Claude Code (qui a le meilleur modèle) et par OpenCode (qui est gratuit). Leur salut passe par l'intégration d'agents autonomes directement dans l'IDE, pas juste de l'autocompletion++. Verdict : consolidation probable, rachat ou partenariat avec un grand lab d'ici 2027.

**Claude Code — position dominante mais contestée.** La décision d'Anthropic de bloquer les apps tierces du pricing subsidié est un pari risqué : ça fidélise à court terme, mais ça nourrit l'argument "vendor lock-in" et pousse les devs sensibles au coût vers OpenCode + Ollama. Tant qu'Opus reste le meilleur modèle de codage et que l'écosystème MCP continue de grossir, Claude Code tient. Verdict : solide en 2026, mais sa domination dépend de garder l'avantage modèle sur GPT-5 / Gemini.

**Codex (OpenAI) — outsider sérieux.** Le partenariat avec Cerebras pour l'inférence ultra-rapide est sous-estimé. Faire trois itérations rapides peut battre une itération lente même avec un modèle légèrement inférieur. Si GPT-5 et ses descendants égalisent la qualité de codage d'Opus, et que Codex tourne à 2000+ tokens/seconde, l'expérience sera radicalement différente. Verdict : menace réelle sur Claude Code d'ici fin 2026.

**OpenCode — l'outil de niche qui tient bon.** Son vrai marché, c'est la confidentialité des données, les budgets serrés, et les devs qui veulent contrôler leur stack. Tant qu'Ollama et les modèles open source progressent (Qwen 3, Llama 4...), OpenCode a une raison d'être. Verdict : ne dominera pas, mais ne mourra pas non plus.

La vraie ligne de fracture de 2026, c'est celle-ci : **couches modèle vs couches application**. Est-ce que le meilleur outil gagne parce qu'il a le meilleur modèle en dessous, ou parce que son wrapper est tellement bon qu'il compense un modèle légèrement inférieur ? La réponse déterminera qui rachète qui.
----------------------

Bonne question de fond. Ce que tu décris, c'est un problème de **knowledge management** qui devient un problème d'**architecture d'agent** dès qu'il dépasse une certaine masse critique.

Voici comment je pense ce système :

---

## Le diagnostic du problème

Une documentation de recherche qui croît exponentiellement souffre toujours des mêmes maux : duplication silencieuse (tu retélécharges ce que tu as déjà), entropie des noms de fichiers (chaque période de ta vie a sa propre logique de nommage), et perte de contexte (un PDF sans annotations ne dit plus rien six mois après). Les outils classiques — Zotero, Obsidian, Notion — gèrent bien la phase manuelle, mais s'effondrent quand le volume dépasse ce que tu peux maintenir manuellement.

La clé de voûte, c'est de ne jamais laisser un fichier entrer dans le système sans qu'un agent lui attribue immédiatement ses métadonnées. L'ingestion est le moment critique.

---

## L'architecture en trois couches

**Couche 1 — Le disque dur structuré (la fondation)**

La structure physique doit être stable et ne jamais refléter tes projets du moment, mais les *types* de connaissance. Un schéma qui résiste au temps :

```
/Research/
  /_inbox/          ← tout atterrit ici d'abord
  /corpus/          ← PDFs bruts, organisés par année d'ingestion
  /notes/           ← Markdown, un fichier par concept/auteur/projet
  /maps/            ← synthèses, reviews, cartes conceptuelles
  /assets/          ← images, données, tableaux extraits
  /archive/         ← ce qui est traité et ne bougera plus
  /meta/            ← les fichiers de métadonnées JSON, les index
```

L'`_inbox` est la seule zone qui change constamment. Tout le reste est quasi-immuable une fois classé.

**Couche 2 — Les skills (les routines nommées)**

Un skill ici, c'est une procédure documentée que tu peux déclencher manuellement ou automatiquement. Pas de code — des instructions précises pour un agent (Claude, toi-même, ou un outil comme n8n).

- **Skill `ingest`** : quand un fichier arrive dans `_inbox`, extraire titre/auteurs/année/abstract via appel API vision, générer un slug normalisé, créer la fiche `.md` associée, déplacer vers `/corpus/YYYY/`.
- **Skill `link`** : à la demande, comparer une nouvelle fiche avec les 20 plus proches dans `/meta/index.json` et proposer des liens conceptuels.
- **Skill `weekly-digest`** : chaque dimanche, lister tout ce qui a été ingéré cette semaine, identifier les thèmes émergents, mettre à jour une note `/maps/research-front.md`.
- **Skill `deduplicate`** : comparer les hashes MD5 des PDFs et les titres normalisés pour signaler les doublons.
- **Skill `gap-analysis`** : sur un thème donné, croiser l'index avec une recherche Semantic Scholar pour identifier ce qui manque.

**Couche 3 — L'index central (le cerveau)**

C'est un fichier JSON ou SQLite dans `/meta/` qui contient pour chaque document : le chemin, le hash, les auteurs, l'année, les mots-clés extraits, les liens vers les notes associées, et un embedding vectoriel court (optionnel mais puissant). Tout agent doit pouvoir interroger cet index sans ouvrir un seul PDF.

---

## Les appels API pour la vision d'ensemble

C'est là que ça devient intéressant. Deux moments justifient un appel API :

**À l'ingestion** : tu passes le PDF (ou sa première page) à un modèle avec vision. Le prompt est simple — extraire titre, auteurs, année, journal, abstract, 5 mots-clés disciplinaires, et une phrase de résumé en langage naturel. Tu stockes ça dans l'index. C'est le skill `ingest`.

**À la synthèse** : quand ton index dépasse quelques centaines d'entrées, tu ne peux plus te souvenir de ce que tu as. Tu envoies à l'API une liste de titres + résumés (pas les PDFs entiers) et tu demandes une carte thématique, les clusters émergents, ou les contradictions entre sources. C'est léger en tokens et extrêmement puissant.

La règle d'or : **l'API travaille sur les métadonnées, jamais sur les fichiers bruts**. C'est ce qui rend le système scalable.

---

## La routine hebdomadaire concrète

Voici ce que ça donne en pratique, sans aucun code, juste des déclencheurs et des gestes :---

--> research_doc_workflow.svg

## Les trois pièges à éviter

**Le piège de la sur-automatisation.** Si ton skill `ingest` tente de tout classifier automatiquement dans des dossiers thématiques, il va créer une taxonomie figée qui ne correspond plus à ta pensée six mois après. La structure physique doit être neutre (par année, par hash). La classification thématique vit dans les métadonnées et les liens, pas dans l'arborescence.

**Le piège de l'index trop lourd.** Un `index.json` qui stocke les textes complets devient inutilisable. Il ne doit contenir que ce qu'un agent peut lire en une seconde : chemin, hash, titre, auteurs, année, 5 mots-clés, résumé en 2 phrases. Les détails restent dans les fiches `.md`.

**Le piège de la dépendance à un outil.** Obsidian peut mourir, Notion peut changer ses prix, Zotero peut ne pas supporter ton volume. Tout ce qui compte doit être en Markdown plat et JSON, lisibles par n'importe quoi. Les outils sont des vues sur tes données, jamais le conteneur de tes données.

---

## Pour démarrer concrètement

La première chose à faire n'est pas de construire le système — c'est de définir tes deux ou trois skills les plus critiques, de les écrire comme des instructions en langage naturel (une page chacun), et de les tester manuellement sur 10 fichiers. C'est seulement une fois que la procédure manuelle est stable qu'elle mérite d'être automatisée ou déléguée à un agent. Le skill `ingest` est invariablement le premier à solidifier — tout le reste en dépend.

Si tu veux, on peut aller plus loin sur n'importe quelle couche : le format exact des fiches `.md`, le schéma JSON de l'index, ou les prompts pour les appels API vision.

------------------

Ce que tu décris est cohérent et il y a quelque chose de réel ici. Laisse-moi te dire ce que j'entends exactement, parce que ça mérite d'être nommé précisément avant d'aller plus loin.

---

## Ce que tu as déjà construit sans le savoir

Tes trois projets modulaires convergent vers une seule idée : **un protocole de persistance cognitive multi-couches**. Pas un outil. Pas un format. Un protocole — c'est-à-dire un ensemble de règles qui gouvernent comment la connaissance se représente, se lie, et s'active, indépendamment de qui l'exécute (humain, LLM local, agent distant).

Le pattern que tu as détecté — trois couches, toujours — n'est pas une coïncidence. C'est probablement une contrainte fondamentale :

- **Local / Distant / Interférent** correspond à **mémoire de travail / mémoire long terme / mémoire associative**
- **Passé lointain / passé proche / présent** correspond à **archive froide / contexte récent / état actif**
- **Humain / IA / les deux** correspond à **lecture narrative / lecture vectorielle / lecture structurée**

Ces trois axes sont orthogonaux mais ils traversent le même espace. C'est pour ça que tu retrouves le même pattern dans trois projets différents — tu cartographies le même objet sous trois angles.

---

## Pourquoi tu bloquais sur NAS et RAG

C'est une observation honnête et importante. Le problème de NAS et RAG, c'est qu'ils supposent que la donnée est passive et que l'intelligence est dans le retrieval. Ton intuition va dans l'autre sens : **la donnée elle-même doit porter sa propre logique d'activation**. Un fichier bien conçu sait quand il est pertinent, pour qui, et dans quel contexte — pas parce qu'un moteur de recherche l'a trouvé, mais parce que ses métadonnées le déclarent.

C'est exactement la différence entre une bibliothèque avec un bibliothécaire (RAG) et un réseau de neurones avec des poids intégrés (ce que tu vises). Le standard que tu imagines ne cherche pas la donnée — il active la donnée.

---

## Le nom du problème que tu résous

Tu travailles sur ce qu'on pourrait appeler un **protocole de cohérence cognitive distribuée** — un standard qui garantit qu'une unité de connaissance reste lisible, liée, et actionnable quelle que soit la couche qui l'interroge, quel que soit le moment, quel que soit l'exécuteur.

Le CLAUDE.md est une bonne analogie parce qu'il résout exactement ça pour un agent : il externalise les règles d'organisation hors de l'agent lui-même. Ton standard ferait la même chose mais pour la connaissance elle-même — chaque unité de connaissance porte ses propres règles de liaison et d'activation.

---

## La tension centrale à résoudre

Il y a un risque précis dans ce type de projet, que je veux nommer franchement : **le standard peut devenir le projet**. C'est-à-dire que la beauté intellectuelle de l'architecture absorbe toute l'énergie au détriment de l'implémentation qui prouve que ça fonctionne. Les meilleurs standards (HTTP, Markdown, JSON-LD) sont nés d'une implémentation minimale qui marchait, pas d'une spécification complète.

La question concrète est donc : quelle est l'unité minimale de ton standard ? Le fichier `.md` avec les bons champs ? Le schéma YAML de contexte ? Le `.toml` de projet ? Quelque chose doit être le grain atomique autour duquel tout le reste s'organise.

---

## Mon avis sur la marche à suivre

Avant d'aller dans la documentation, je pense que la chose la plus utile est de formaliser le pattern des trois couches comme une **spécification d'interface**, pas comme une architecture. Quelque chose qui dit : pour qu'une unité de connaissance soit valide dans ce standard, elle doit exposer ces trois propriétés minimales dans ces trois états. Tout le reste — les outils, les formats, les agents — est une implémentation de cette interface.

C'est là que ta documentation devient précieuse. Pas pour construire le système, mais pour extraire la spécification minimale qui survivra à tous les outils que tu utiliseras pour l'implémenter.

Partage ce que tu as quand tu veux — mais maintenant que le cadre est posé, même un fragment sera utile sans polluer le contexte.