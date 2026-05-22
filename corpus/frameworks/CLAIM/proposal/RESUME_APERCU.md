# 2 — Description du projet (Résumé · Mots-clés · Aperçu)
**Version** : 1.0 — 16 mai 2026
**Statut** : v1 — prêt pour saisie portail PID
**Référence** : proposal/RESUME_APERCU.md (à mettre à jour avec ces versions finales)

---

## A. Résumé de projet (≤ 2 000 caractères — portail avec NL)

**Corps formulaire : ~1 431 caractères**

Les opérations ISR des Forces armées canadiennes génèrent des flux hétérogènes — radar, SIGINT, EO/IR, texte, télémétrie — traités par des agents spécialisés dont les sorties sont incomparables. Un radar exprime une probabilité, un capteur EO/IR une classification, un système SIGINT une inférence sur une échelle distincte. Sans langage commun, l'orchestrateur ne peut combiner ces sorties de façon cohérente, traçable et certifiable. L'opérateur humain se retrouve seul face à des chiffres incompatibles sous contrainte temporelle.

Ce projet spécifie la couche manquante : le CLAIM, unité atomique d'échange épistémique entre agents spécialisés et orchestrateur coordinateur. Un CLAIM porte cinq invariants : ce que l'agent a observé ou inféré, sa masse de croyance formelle sur l'ensemble des hypothèses (y compris son ignorance explicite), son statut illocutionnaire auto-déclaré, son horodatage de validité, et sa chaîne de provenance traçable. L'orchestrateur combine les CLAIMs par règle formelle, détecte et localise les conflits, et produit un état épistémique lisible pour l'opérateur en moins de dix secondes. Règle cardinale : en cas de conflit non résolu, l'orchestrateur suspend toute décision automatique et expose le désaccord à l'humain.

Le livrable est une spécification adoptable par tout pipeline de fusion multimodale ISR, validée analytiquement sur données synthétiques. NMT-2 à l'entrée, NMT-3 en six mois.

---

## B. Mots-clés (3 à 5)

1. Fusion épistémique multimodale
2. Orchestration multi-agents ISR
3. Protocole d'échange épistémique
4. Traçabilité certifiable
5. Architecture neuro-symbolique hybride

---

## C. Aperçu du projet (≤ 3 000 caractères — portail avec NL)

**Corps formulaire : ~2 357 caractères**

Les opérations ISR modernes agrègent des flux de données hétérogènes — radar, SIGINT, EO/IR, texte, télémétrie — issus d'agents spécialisés dont les sorties sont structurellement incomparables. Chaque agent exprime sa confiance sur une échelle différente, le silence d'un capteur peut signifier absence d'observation ou absence de signal, et aucun protocole existant ne permet à un orchestrateur de combiner ces sorties de façon mathématiquement cohérente, traçable et certifiable. Ce gap d'interface, confirmé par revue de littérature indépendante (quatre sources, consensus unanime), est le problème que ce projet résout.

La contribution est le CLAIM — unité atomique d'échange épistémique entre un agent spécialisé et un orchestrateur coordinateur. Un CLAIM porte cinq invariants indissociables : contenu propositionnel sur une entité résolue, fonction de masse de croyance sur l'ensemble des sous-ensembles d'hypothèses (Transferable Belief Model de Smets, masse de conflit m(vide) conservée), statut illocutionnaire auto-déclaré (OBSERVE, INFER, DEDUCE, ASSUME), horodatage de validité, et identifiant de provenance traçable PROV-O. L'orchestrateur combine les CLAIMs par règle conjonctive non normalisée, localise les conflits par PCR5, et produit un EPISTEMIC_STATE (état Belnap : accord, désaccord, silence qualifié) transmis à l'interface humaine. Si la masse de conflit dépasse un seuil configurable, toute décision automatique est suspendue et le conflit est exposé à l'opérateur avec sa source identifiée.

L'architecture est neuro-symbolique hybride : une couche perceptive apprenante (agents experts par modalité, y compris tout modèle de langage multimodal compatible) alimente une couche de raisonnement déterministe et auditable. Le CLAIM est le contrat d'interface manquant entre ces deux couches — ce que ni le modèle JDL (référence doctrinale NATO pour la fusion ISR) ni les architectures neuro-symboliques existantes ne définissent formellement.

Le livrable est une spécification formelle adoptable par tout pipeline de fusion multimodale, validée analytiquement sur données synthétiques (autorisées par Q3/R4). Hypothèse de travail documentée : l'alignement spatio-temporel et la résolution d'entités sont supposés résolus en amont. NMT-2 à l'entrée du contrat, NMT-3 en six mois.

---

## Notes de calibrage

| Champ | Chars (avec NL) | Limite | Marge |
|-------|----------------|--------|-------|
| Résumé | ~1 431 | 2 000 | ~569 |
| Aperçu | ~2 357 | 3 000 | ~643 |

**Marge résumé (~569 chars)** : possibilité d'ajouter une phrase sur l'applicabilité canadienne
hors défense (santé, sécurité publique) ou sur la composition canadienne de l'équipe.

**Marge aperçu (~643 chars)** : possibilité d'ajouter un exemple concret (scénario sonar +
radar + SIGINT — 90 secondes pour décider) pour ancrer le lecteur non-technique.
Peut aussi accueillir la mention du collaborateur (Thierry) et du NRC si pertinent.

---

## Références

- Smets et Kennes (1994) — TBM, m(vide) conservé
- Belnap (1977) — états épistémiques quatre valeurs
- Dezert et Smarandanche — PCR5, localisation du conflit
- W3C PROV-O (2013) — traçabilité provenance
- Steinberg et al. (1999) — JDL, gap d'interface
- Q3/R4 AP6-défi-13 — données synthétiques autorisées
- QO-S2-01 résolu — gap confirmé consensus 4/4 IA
