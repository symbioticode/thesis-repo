# ANAMNÈSE — Qualification du tournant · Nœud RKA
## État au 2026-04-26

signal: present
status: PENDING
role: container
created: 2026-04-26
cross_validated_by: [HALO, PCCD, MIF-corpus]
activation_mode: operative

---

## Ce qui est confirmé (ne pas re-ouvrir)

| Élément | Source | Confiance |
|---------|--------|-----------|
| Nom : ANAMNÈSE | Philosophique + médical — convergence des deux sens | Haute |
| Métrique : triplet C1/C2/C3 | HALO — empirique, observé en session | Haute |
| C1 observateur : humain | Structurel — protocole lisible par l'humain | Haute |
| C2 observateur : IA | Structurel — pattern reconnu par l'instance | Haute |
| C3 observateur : humain | Structurel — clarté de la prochaine action | Haute |
| Trois acteurs permanents | Humain / IA / Documents | Haute |
| Acteur absent : orchestrateur | Bus factor = 1 — documenté MIF + HALO | Haute |
| Périmètre : inter-sessions | Pas la doc, pas le code, pas la vision | Haute |
| RIEP comme composant | Raffinement Itératif par Évidence et Preuve | Moyenne |
| Résidence : Git + YAML/Markdown | Invariant format, indépendant du LLM | Haute |
| Relation HALO : instance partielle | HALO précède, ANAMNÈSE abstrait | Haute |
| Relation PCCD : non clarifiée | Enfant ou pair — question ouverte | Basse |

---

## Ce qui reste ouvert (à valider empiriquement)

**H001 — N=3 pour la décroissance**
Un élément non référencé dans 3 sessions consécutives est candidat à l'archivage.
Valider : après 10 sessions instrumentées, les candidats détectés sont-ils effectivement obsolètes ?

**H002 — FR cible = 0.65**
Au-delà de 0.65, le coût de maintenance dépasse le bénéfice.
Valider : corrélation entre (C1+C2+C3 = 3) et productivité de session sur 5+ mesures.

**H003 — 5 types de recadrages**
Le corpus MIF révèle des recadrages récurrents. 4-5 types distincts probables.
Valider : catalogue extrait après 10+ sessions avec Q7 documentés.

**H004 — PROMPT_ORCHESTRATION**
Une instance IA sans historique peut mettre à jour `anamnese_state.yaml` correctement.
Valider : test en Phase 2 avec une instance froide.

**H005 — ANAMNÈSE × PCCD relation**
Est-ce une instance-enfant de PCCD ou un protocole pair qui partage ses invariants ?
Valider : soumettre à PCCD avec les 8 invariants candidats — combien ANAMNÈSE respecte-t-elle ?

---

## Questions spécifiques encore en suspens

1. **Disposition comme signal épistémique** — capturer la disposition mentale de l'humain
   est utile pour un tiers observateur. Mais comme HALO l'a montré, l'humain ne peut
   pas contrôler son humeur pour produire de meilleurs prompts. La disposition est donc
   un tag *descriptif* (post-session), jamais *prescriptif*. Reste à valider : est-ce
   que la disposition corrèle avec C2 (reconnaissance de pattern) ?

2. **Le D-SIG préventif** — signal préventif plutôt qu'en temps réel. La proposition
   reste : signaler à une instance externe (Grok, Opus) quand un volume élevé de production
   n'a pas été soumis à révision. Mais le mécanisme de déclenchement n'est pas formalisé.

3. **Interface ANAMNÈSE × MIF** — MIF certifie les métriques. ANAMNÈSE gère la continuité
   du projet qui produit MIF. La question : est-ce que les KB articles de MIF (TALK-001
   à TALK-010) sont des nœuds ANAMNÈSE ou des nœuds RKA séparés ? Distinction à clarifier
   avant la Phase 2 analytique de HALO.

---

## Conditions de passage de PENDING à CERTIFIED

ANAMNÈSE sera certifiable quand :

- [ ] 5 sessions avec mesure C1/C2/C3 documentée
- [ ] H001 (N=3) validé ou amendé par l'observation
- [ ] H002 (FR cible) calibré empiriquement
- [ ] Au moins 3 recadrages catalogués avec leur type
- [ ] PCCD a répondu à H005 (relation enfant/pair)
- [ ] `anamnese_state.yaml` a été mis à jour par une instance froide avec succès (test H004)

**Estimation : 5-8 sessions instrumentées, soit 4-6 semaines à rythme normal.**

---

## Interfaces transversales (synthèse)

### PCCD × ANAMNÈSE
| Élément PCCD | Usage dans ANAMNÈSE |
|---|---|
| INV-01 (émetteur/interpréteur) | `anamnese_state.yaml` émet, l'instance interprète — jamais l'inverse |
| Statuts épistémiques | KB articles reçoivent PENDING/CERTIFIED/DEPRECATED |
| `cross_validated_by` | RIEP documente la convergence inter-instances |
| `epistemic_weight` | Chaque KB article a un niveau de confiance |

### RKA × ANAMNÈSE
| Élément RKA | Usage dans ANAMNÈSE |
|---|---|
| Niveau 0 (signal vital) | `anamnese_state.yaml` a signal/hash/last_modified |
| Niveau 1 (frontmatter) | KB articles ont type_valeur, disposition, scope |
| `activation_mode` | Éléments actifs = operative, archivés = contextual |
| Skill `heartbeat` | Détecte N=3 inactifs → propose archivage |
| `slug` | Chaque élément ÉTAT_ACTIF a un ID traçable |

### HALO × ANAMNÈSE
| Élément HALO | Rôle dans ANAMNÈSE |
|---|---|
| `protocols.yaml` | Hôte des règles ANAMNÈSE |
| `profil_stable.yaml` | Source de C2 (patterns pour reconnaissance) |
| Session YAML | Point de mesure C1/C2/C3 |
| `a_faire_prochaine_session` | Source de C3 |
| `memory/` | Couche d'archive ANAMNÈSE |
| `dashboard_metriques.yaml` | Historique FR (C1/C2/C3 par session) |

---

*ANAMNÈSE qualification · status: PENDING · 2026-04-26*
*Voir HALO_ANAMNESE_Upgrade.md pour les instructions d'implémentation*
