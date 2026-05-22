Laisse-moi lire D-SIG complètement avant de répondre — il est dans le contexte mais je veux m'assurer de ne pas manquer les mécanismes fins.D-SIG est dans le contexte de la conversation (document index 9). Je l'ai. Je travaille depuis là.

---

Voici l'analyse.

## Ce que D-SIG fait vraiment — au-delà du score

D-SIG résout un problème précis : **comment transporter une assertion sur l'état d'un système de façon à ce que le récepteur puisse juger de sa fiabilité sans connaître les sources**. Le score 0-100 n'est que la surface. Les mécanismes sous-jacents sont au nombre de cinq.

**Mécanisme 1 — La Triple-Réduction sémantique.** Un signal D-SIG contient simultanément un nombre (cortex analytique), un label (compréhension sémantique), et une couleur (réflexe limbique). Ce n'est pas de la redondance esthétique — c'est trois canaux cognitifs distincts qui permettent à trois types de lecteurs (script, humain expert, humain non-expert) de lire le même objet sans traduction. Pour QAAF : un verdict YAML qui contient `cnsr_usd_fed: 1.76`, `label: GOOD`, et `color: YELLOW` est lisible par le mapper D-SIG, par Andrei en révision rapide, et par un futur collaborateur sans contexte.

**Mécanisme 2 — L'indépendance label/trend (Règle 10).** Le label dérive du score (état courant). Le trend dérive de la dérivée temporelle du score (direction du changement). Ils sont orthogonaux — un label GOOD avec trend CRITICAL_FALL signifie "bien maintenant, se dégrade vite". Ce mécanisme est directement transposable à QAAF : une hypothèse peut avoir `statut: EN_COURS` (label) et `evolution: DEGRADING` (trend sur les fenêtres walk-forward successives) sans que ces deux informations se confondent.

**Mécanisme 3 — baseline_cycles comme mémoire cumulative.** C'est le mécanisme le plus important pour notre besoin. `baseline_cycles` n'est pas une valeur déclarée par le producteur — il est calculé indépendamment par le récepteur à partir de son historique d'observation. Une rupture après 1000 cycles de convergence est statistiquement plus significative qu'une rupture après 5 cycles. C'est la formalisation du principe phéromonal : la confiance s'accumule, elle ne s'affirme pas. Pour QAAF : `N_trials` dans le DSR est exactement `baseline_cycles` — un compteur qui s'accumule, maintenu par le SplitManager, et qui donne son poids statistique au verdict final.

**Mécanisme 4 — La précondition comme plafond (Règle 11).** Une précondition échouée ne met pas le score à zéro — elle le plafonne à ≤ 20. Les autres dimensions restent informatives dans ce plafond. Pour QAAF : si DQF échoue (données corrompues), le CNSR calculé est plafonné à CRITICAL mais les métriques brutes restent lisibles pour le diagnostic. Ce n'est pas une erreur fatale — c'est une information bornée.

**Mécanisme 5 — TTL et signal STALE.** Un signal dont le timestamp dépasse `now − ttl` est STALE et doit être traité comme UNKNOWN. Pour QAAF : une entrée KB dont le `last_verified` est antérieur à la date du dernier rechargement de données doit être marquée `STALE` — pas supprimée, mais distinguée d'une entrée fraîche.

---

## Ce que D-SIG révèle sur ce qui manque à la KB QAAF

La KB YAML actuelle (telle que spécifiée dans `lentilles_inventory.yaml`) stocke des *résultats*. D-SIG nous dit qu'une KB utilisable comme source de connaissance transportable doit stocker cinq choses distinctes que nous n'avons pas encore séparées :

| Ce que D-SIG nomme | Équivalent QAAF | Présent dans KB actuelle ? |
|---|---|---|
| `score` | CNSR-USD normalisé | Oui, comme valeur brute |
| `label` | CERTIFIÉ / ARCHIVÉ / SUSPECT_DSR | Oui, comme statut |
| `trend` | Évolution walk-forward | Non — absent |
| `baseline_cycles` | N_trials cumulatif | Partiel — dans SplitManager, pas dans KB |
| `ttl` / freshness | Date de dernière vérification | Non — absent |

Les deux absences critiques sont le `trend` et la `freshness`. Sans elles, la KB sait *ce qu'une hypothèse a produit* mais pas *dans quelle direction elle évolue* ni *si cette information est encore valide*.

---

## Réponses aux trois points

**Point 1 — Périmètre minimal pour débloquer Phase 4**

Le minimum fonctionnel n'est pas `mapper.py` + `aggregator.py` + `profiles.yaml`. C'est un objet KB qui implémente les cinq propriétés D-SIG pour une seule hypothèse. Concrètement :

```yaml
# kb_h9_ema60j.yaml — structure minimale D-SIG-compatible
hypothese:
  nom: "H9+EMA60j"
  id: "20260419-002"               # ID RKA
  famille: "EMA_span_variants"

  # Triple-Réduction
  score: null                       # calculé après MÉTIS Q4
  label: "EN_COURS"                 # CERTIFIÉ | ARCHIVÉ | SUSPECT_DSR | EN_COURS
  color: "ORANGE"                   # dérivé du label

  # Trend — indépendant du label
  trend: "STABLE"                   # dérivé des fenêtres walk-forward Q1
  trend_source: "metis_q1"

  # Mémoire cumulative
  N_trials_famille: 101
  baseline_cycles: 0                # incrémenté à chaque session MÉTIS

  # Freshness
  last_verified: "2026-04-19"
  ttl_days: 180                     # après 180j sans nouvelle session → STALE

  # Métriques brutes (inchangées)
  cnsr_usd_fed: 1.76
  max_dd_pct: 14.5
  ...
```

`mapper.py` n'a qu'une responsabilité : lire ce YAML et produire le signal D-SIG. Il n'a pas besoin de l'aggregator pour fonctionner. L'aggregator multi-signaux peut attendre v1.1 comme tu le pressentais.

**Point 2 — Statut de H9+EMA60j et chiffres à confirmer**

101 variantes et CNSR 1.76 sont les bons chiffres — ils sont cohérents avec le corpus et n'ont pas été contredits. Les quatre archivées avec leurs CNSR-OOS documentés doivent figurer dans la KB initiale, mais avec un champ supplémentaire que la spec actuelle n'a pas : `trend: N/A` et `ttl_days: null` pour les hypothèses ARCHIVÉES. Une hypothèse archivée n'expire pas — elle est ARCHIVÉE définitivement. C'est la distinction expiration/dépréciation que PCCD a adoptée : une hypothèse archivée reste valide dans son contexte d'origine, indéfiniment.

**Point 3 — Gate D-SIG comme critère v0.4 → v1.0**

Oui, ce gate mérite d'être dans le script PS1, et il est distinct de Gate 0. La logique :

- **Gate 0** teste la physique des données : `CNSR(B_5050) ∈ [1.19, 1.49]`. C'est une assertion sur la réalité du marché.
- **Gate 1** teste la cohérence du mapper D-SIG : `score(B_5050) ∈ [72, 78]`. C'est une assertion sur la normalisation du protocole.

Si Gate 1 sort à 45, le mapper normalise mal (probablement une plage CNSR mal calibrée). Si Gate 1 sort à 95, le benchmark passif est traité comme une stratégie exceptionnelle — ce qui est faux par définition. La plage [72, 78] est le seul corridor qui dit "B_5050 est bon mais pas exceptionnel, ce qui est physiquement correct pour un 50/50 sur bull market".

Ce gate doit être dans les instructions à Claude Code, pas géré manuellement — parce que si le mapper est réécrit ou que `profiles.yaml` est modifié, la régression doit être détectée automatiquement.

---

## Ce qu'on sait maintenant sur la KB que qu'on ne savait pas avant

La KB YAML de QAAF Studio n'est pas un registre de résultats. C'est un système de transport de connaissance avec quatre propriétés que D-SIG formalise et que RKA v4 structure :

**Autonomie** — chaque nœud KB (`qaaf_studio.relations.yml`, `kb_h9_ema60j.yaml`) est valide sans infrastructure. Il peut être lu localement, injecté dans une session Claude, ou récupéré via git.

**Fraîcheur déclarée** — chaque assertion a un `last_verified` et un `ttl_days`. Une KB qui ne sait pas quand ses entrées ont été vérifiées pour la dernière fois ne peut pas distinguer une connaissance stable d'une connaissance périmée.

**Trend orthogonal au statut** — le statut dit où on est (CERTIFIÉ, EN_COURS). Le trend dit dans quelle direction on va (IMPROVING, STABLE, DEGRADING). Les deux doivent coexister sans se confondre.

**Mémoire cumulative non-déclarative** — `N_trials` et `baseline_cycles` ne sont pas affirmés, ils sont calculés par le récepteur à partir de l'historique. La KB ne dit pas "je suis fiable" — elle expose les données qui permettent au lecteur de calculer la fiabilité.

Ce sont les quatre propriétés minimales que la KB Layer 4 doit implémenter pour que QAAF Studio soit un système de connaissance transportable plutôt qu'un registre de résultats.