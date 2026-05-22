
Je vais lire les documents sources avant d'analyser.Le contenu des 4 documents est déjà dans le contexte. Je procède directement à l'analyse.

---

# Rapport BR-2026-FORMULATION
**Branche : YOUTUBE / XR Agents / Molmo / PixMo**
**Question inversée : CLAIM comble-t-il des lacunes réelles pour ces domaines ?**
**Instance : Claude Sonnet 4.6 — traitement en isolation**

---

## 1. Cadrage de la démarche

La branche BR-2026-FORMULATION avait établi que les 3 sources *situent* le gap sans le résoudre. La démarche inverse consiste à partir de la spécification CLAIM v1.1 et à tester si ses composants formels répondent à des lacunes concrètes identifiables dans ces corpus — et si ces lacunes constituent des arguments percutants pour une soumission de 3 000 caractères.

Les composants CLAIM évalués : **DS (Dempster-Shafer)**, **Belnap 4-valué**, **AGM (révision de croyance)**, **SAT (Speech Act Theory / actes illocutoires)**, **EPISTEMIC_STATE (orchestrateur)**, **audit_hash (provenance)**.

---

## 2. Tableau source / convergence / delta par composant

### DS — Masse de croyance sur l'espace des puissances de Θ

| Axe | Molmo/PixMo | Castrounis | Jayasri |
|-----|------------|------------|---------|
| **Convergence** | Le mécanisme de *pointing* produit des scores de confiance implicites (coordonnées + comptage). Le pipeline pré-entraînement/fine-tuning implique deux régimes d'incertitude distincts. | Les embeddings coordonnés dans un joint space capturent une similarité sémantique — mais sans quantification d'incertitude sur la mesure. | L'agent *listener* produit des chunks de transcription sans aucune métrique de confiance sur la reconnaissance vocale. |
| **Delta (lacune)** | Molmo n'expose aucune distribution de masse sur ses hypothèses alternatives. Un pointing à (63.5, 44.5) ne dit pas "je crois à 0.7 que c'est Mt. Rainier, et à 0.3 que c'est Mt. Adams." | La projection dans un joint embedding space efface l'incertitude modale — on obtient un vecteur, pas une croyance. | La latence de la voix crée une incertitude temporelle non modélisée : le chunk T est-il la suite du chunk T-1 ou une nouvelle assertion ? |
| **Score pertinence NMT-2** | ★★★★★ | ★★★☆☆ | ★★★★☆ |

**Verdict DS** : Lacune confirmée et exploitable. L'argument pour la soumission : *"Molmo produit un résultat ponctuel là où un système ISR exige une distribution."*

---

### Belnap — 4 états épistémiques (T / F / N / B)

| Axe | Molmo/PixMo | Castrounis | Jayasri |
|-----|------------|------------|---------|
| **Convergence** | Le cas *"not present"* dans PixMo-Points (absence du cible) est une réponse N (None — non-information). Le modèle répond correctement mais sans signaler que cet état est qualitativement différent d'un False. | Le silence d'un modèle sur une requête hors-distribution est traité comme une erreur, pas comme un état N reconnu. | L'agent guide répond "what's going on?" même quand la transcription est partielle — il n'a pas de mécanisme pour émettre un état N ("je n'ai pas assez de contexte pour répondre"). |
| **Delta (lacune)** | Molmo confond N et F dans son interface de sortie : "This isn't in the image" n'est pas distingué formellement d'une réponse négative sur un objet présent mais mal détecté. | Aucun des modèles cités ne distingue entre "information contradictoire reçue" (B) et "information absente" (N). | En contexte ISR, la confusion N/B est critique : un capteur silencieux (N) vs. deux capteurs contradictoires (B) ont des implications de décision radicalement différentes. |
| **Score pertinence NMT-2** | ★★★★★ | ★★☆☆☆ | ★★★★★ |

**Verdict Belnap** : Argument le plus percutant pour la soumission. La distinction N/B est absente de tous les systèmes cités et directement critique en ISR.

---

### AGM — Révision de croyance

| Axe | Molmo/PixMo | Castrounis | Jayasri |
|-----|------------|------------|---------|
| **Convergence** | Le fine-tuning de Molmo est une forme implicite de révision — le modèle met à jour ses paramètres face à de nouvelles données. La *rolling memory* de Jayasri est une forme naïve de révision contextuelle. | La notion de diffusion (débruitage depuis des features latentes) ressemble à une révision bayésienne — mais non formalisée. | La mémoire roulante de l'agent listener accumule sans jamais retirer : aucun mécanisme d'oubli contrôlé ou de contraction. |
| **Delta (lacune)** | Le fine-tuning est batch, hors-ligne, coûteux. Pour un système ISR temps-réel, la révision doit être incrémentale, traçable, et réversible. AGM fournit exactement ces axiomes. | Aucun des systèmes ne distingue *expansion* (ajout d'info cohérente), *contraction* (retrait d'une croyance) et *révision* (intégration d'info contradictoire). | En contexte ISR : un agent reçoit "zone sûre" puis "contact ennemi" — la révision naïve (écrasement) est inacceptable. Il faut une trace de la contraction. |
| **Score pertinence NMT-2** | ★★★☆☆ | ★★☆☆☆ | ★★★★☆ |

**Verdict AGM** : Lacune réelle mais argument moins immédiat pour 3 000 caractères. Pertinent pour Partie B / NMT 4-5. À ne pas foregronder dans la soumission.

---

### SAT — Actes illocutoires (Speech Act Theory)

| Axe | Molmo/PixMo | Castrounis | Jayasri |
|-----|------------|------------|---------|
| **Convergence** | Les style tags de Molmo ("vqa2:", "long caption:") sont des marqueurs d'acte illocutoire primitifs — ils signalent l'intention communicationnelle de la requête. | La distinction *summarization / translation / creation* de Castrounis mappe sur les actes directifs, assertifs et déclaratifs de Searle. | L'agent guide de Jayasri ne distingue pas entre une assertion ("la zone est sûre") et une requête d'information ("qu'est-ce que la zone ?") dans son output. |
| **Delta (lacune)** | Les style tags de Molmo sont des conventions ad hoc non formalisées, non interopérables entre agents. CLAIM standardise cet acte comme champ `illocutionary_force` typé. | Les 3 catégories de Castrounis sont descriptives, pas normatives — elles ne dictent pas ce qu'un agent *doit* signaler à un orchestrateur. | Sans typage illocutoire, un orchestrateur ne peut pas distinguer un agent qui *informe* d'un agent qui *recommande* d'un agent qui *alerte* — trois niveaux de réponse décisionnelle très différents en ISR. |
| **Score pertinence NMT-2** | ★★★★☆ | ★★★☆☆ | ★★★★★ |

**Verdict SAT** : Argument fort, sous-exploité. La distinction *informer / recommander / alerter* est directement parlante pour un évaluateur MDN.

---

### EPISTEMIC_STATE (orchestrateur) + audit_hash

| Axe | Molmo/PixMo | Castrounis | Jayasri |
|-----|------------|------------|---------|
| **Convergence** | Molmo produit des outputs mais aucun état agrégé inter-modal. L'architecture 4-composants n'a pas de couche d'arbitrage. | La notion de joint embedding space est le plus proche d'un EPISTEMIC_STATE — mais c'est une représentation, pas un état de croyance arbitré. | L'architecture 2-agents de Jayasri n'a pas d'orchestrateur : listener et guide coexistent sans arbitrage formel de leurs outputs. |
| **Delta (lacune)** | Qui agrège les sorties de 3 VLMs sur le même théâtre ? Aujourd'hui : personne. CLAIM propose l'orchestrateur + EPISTEMIC_STATE comme réponse. | L'absence d'audit_hash signifie qu'une trace de décision est impossible : on ne peut pas savoir quel agent a produit quelle contribution à la fusion. | En ISR, la traçabilité de provenance est une exigence légale et opérationnelle. Jayasri ne l'adresse pas même en prototype. |
| **Score pertinence NMT-2** | ★★★★★ | ★★★☆☆ | ★★★★★ |

**Verdict EPISTEMIC_STATE + audit_hash** : Argument de clôture le plus fort. C'est le composant le plus différenciant de CLAIM par rapport à tout ce que les 3 sources décrivent.

---

## 3. Tableau de décision consolidé

| Composant CLAIM | Verdict | Destination | Argument pour soumission |
|----------------|---------|-------------|--------------------------|
| **DS (masses sur 2^Θ)** | ✅ Garde — intégration directe | Partie A (arg. principal) + Partie B (détail calibration) | "Molmo produit un score, CLAIM produit une distribution." |
| **Belnap 4 états** | ✅ Garde — argument clé | Partie A (différenciateur) | "La confusion N/B est absente de tous les systèmes existants et critique en ISR." |
| **AGM révision** | ⚠️ Garde — usage différé | Partie B uniquement | Trop technique pour 3 000 car. — réserve pour NMT 4-5. |
| **SAT illocutoire** | ✅ Garde — argument opérationnel | Partie A (reformulation accessible) | "Informer ≠ recommander ≠ alerter : CLAIM type l'acte, les VLMs ne le font pas." |
| **EPISTEMIC_STATE** | ✅ Garde — argument de clôture | Partie A (position finale) | "Aucun système existant n'a de couche d'arbitrage inter-agents formalisée." |
| **audit_hash** | ✅ Garde — argument réglementaire | Partie A (1 phrase) + Partie B | "Traçabilité de provenance : exigence MDN non adressée par les VLMs." |

**Rejet** : Aucun composant n'est rejeté. AGM est *différé*, pas écarté.

---

## 4. Arguments percutants extractibles pour Partie A (≤ 3 000 car.)

Trois formulations candidates, classées par impact décroissant pour un évaluateur NMT-2 :

**ARG-F1 (Belnap + opérationnel)** — *"Les meilleurs VLMs ouverts (famille Molmo, 86M paramètres) ne distinguent pas l'absence d'information du désaccord entre capteurs. CLAIM formalise cet état B (both) comme signal d'escalade, distinct de N (silence qualifié)."*

**ARG-F2 (DS + décision)** — *"Un agent Molmo produit un résultat ponctuel sur Mt. Rainier. Un système ISR exige : masse 0.7 sur {Rainier}, masse 0.2 sur {Adams}, masse 0.1 sur Θ. CLAIM standardise ce transfert."*

**ARG-F3 (SAT + arbitrage)** — *"Aucune architecture multi-agents publiée (Jayasri 2024, fluffy-guide ; Molmo 2024) ne type l'acte illocutoire de l'output agent. CLAIM introduit ce typage comme condition nécessaire à une orchestration décisionnelle responsable."*

---

## 5. Limites et risques d'intégration

**Risque 1 — Contamination de périmètre** : Les 3 sources traitent de VLMs civils (navigation, lecture, captioning). Leur citation directe dans la soumission MDN doit être calibrée — elles servent à situer le gap, pas à définir le contexte d'application.

**Risque 2 — Complexification de Partie A** : AGM introduit une complexité formelle disproportionnée pour 3 000 car. Maintenir en Partie B.

**Risque 3 — Surcharge argumentaire** : Les 3 ARG ci-dessus ne doivent pas tous apparaître en Partie A. Recommandation : ARG-F1 en position principale, ARG-F3 en support, ARG-F2 en Partie B.

---

## Note gouvernance

Ce rapport est produit en isolation BR-2026-FORMULATION. Il ne modifie pas CLAIM_specification.md v1.1. Toute intégration d'un ARG dans Partie A est soumise à validation Andrei avant merge. Le rapport est lui-même candidat à révision par une instance analyste per le protocole établi.

---

## Rapport BR-2026-CLAIM\_vs\_NeSy-Cyber

### Rapport d'analyse de convergence/divergence — Décision d'intégration

**Statut :** Branche isolée · Instance analyste secondaire requise
**Horizon d'évaluation :** NMT-2 soumission J-12 · Post-soumission extension possible

---

## I. Identification des composants proposés par la branche

La branche Gemini extrait 5 propositions distinctes du corpus NeSy-Cyber :

| ID | Composant proposé | Source primaire |
|----|-------------------|-----------------|
| P1 | CLAIM comme mécanisme d'*Instructibility* inter-agents manquant au cadre G-I-A | PDF cyber §II + §VI-A |
| P2 | Figure 11 (0% couverture sur 7 dimensions) comme preuve empirique du gap de standardisation | PDF cyber §IV-B Fig.11 |
| P3 | Contexte dual-use NeSy autonome comme justification formelle de la règle cardinale m(∅) ≥ θ_conflit | PDF cyber §III-D |
| P4 | ThreatKG/CTINexus comme précédent partiel à distinguer explicitement (faits structurés ≠ croyances formelles) | PDF cyber §III-C |
| P5 | Reformulation de l'Assertion A : "interface L1→L2" → "interface entre tout nœud de traitement et l'orchestrateur" | BR-analyse §2 |

---

## II. Tableau source / convergence / delta par composant

### P1 — CLAIM comme pièce manquante du G-I-A

| Axe | Contenu |
|-----|---------|
| **Source** | G-I-A Instructibility : `I(θ,K,H) = E[Adaptation(Δθ_h, ΔK_h)]` — mesure l'adaptation à un feedback *humain*, pas inter-agents |
| **Convergence** | Le CLAIM est précisément le canal par lequel un agent hétérogène transmet son état épistémique à l'orchestrateur, ce qui est la condition nécessaire à ce que la dimension I opère en contexte distribué. Convergence forte. |
| **Delta** | Le G-I-A opère *intra-agent* (Instructibility = analyste → système). Le CLAIM opère *inter-agents*. Ce n'est pas la même couche. Prétendre que le CLAIM "complète" le G-I-A serait une sur-extension — le positionner comme "analogue architectural à une couche supérieure" est plus juste. |

**Score pertinence NMT-2 :** 4/5 — argumentaire CO-1 direct, renforce la démonstration du gap
**Score solidité formelle :** 3/5 — analogie valide, mais le G-I-A n'est pas le cadre de référence IDEeS
**Score risque d'intégration :** 2/5 — aucune modification spec requise, usage rhétorique seulement

---

### P2 — Figure 11 comme preuve empirique (0% sur 7 dimensions)

| Axe | Contenu |
|-----|---------|
| **Source** | Hakim et al. 2025, Figure 11 : matrice de couverture benchmarks NeSy × exigences spécifiques. Zéros confirmés pour : causal reasoning, multi-agent testing, instructibility assessment, alignment verification |
| **Convergence** | Confirme directement l'Assertion B : aucun système existant ne couvre le domaine que CLAIM adresse. Citable comme référence peer-reviewed (arXiv, soumis 2025). |
| **Delta** | La Figure 11 concerne les *benchmarks d'évaluation*, pas les *architectures opérationnelles*. Elle prouve l'absence de métriques, pas l'absence de protocoles. Distinction utile à maintenir pour éviter l'overreach. |

**Score pertinence NMT-2 :** 5/5 — preuve empirique directe, utilisable dans Partie B §B.1 ou argumentation CCP
**Score solidité formelle :** 4/5 — source systématique (127 papers, κ=0.89), méthode SPAR-4-SLR
**Score risque d'intégration :** 1/5 — aucun risque, usage citation uniquement

---

### P3 — Dual-use NeSy comme justification de la règle cardinale

| Axe | Contenu |
|-----|---------|
| **Source** | HPTSA : 42% succès zero-day à 24$/exploit (pass@5). VulnBot : 30.3% vs 9.09% baseline. PDF cyber §III-D |
| **Convergence** | La règle cardinale du CLAIM (escalade humaine obligatoire si m(∅) ≥ θ_conflit) trouve une justification *empirique externe* : des systèmes NeSy autonomes, sans supervision humaine dans la boucle de décision, produisent des effets offensifs réels à coût marginal. En contexte ISR militaire, l'analogie est directe. |
| **Delta** | Ces systèmes (HPTSA, VulnBot) sont des agents offensifs cyber, pas des capteurs ISR. Le transfert analogique tient pour le principe (autonomie sans superviseur humain = risque), mais ne doit pas être présenté comme un cas ISR direct. |

**Score pertinence NMT-2 :** 4/5 — justifie la contrainte de gouvernance sans alourdir la spec
**Score solidité formelle :** 3/5 — analogie valide mais domaine adjacent (cyber offense ≠ ISR fusion)
**Score risque d'intégration :** 2/5 — aucune modification spec, usage justificatif uniquement

---

### P4 — ThreatKG/CTINexus comme précédent partiel à distinguer

| Axe | Contenu |
|-----|---------|
| **Source** | ThreatKG : pipeline de construction de graphes de connaissances à partir de rapports CTI non structurés. CTINexus : raffinement LLM-driven avec alignment STIX. PDF cyber §III-C |
| **Convergence** | Ces systèmes partagent des *représentations de connaissances* entre agents — le plus proche existant d'un mécanisme de partage inter-agents dans la littérature. La branche Gemini a raison de les identifier comme précédent partiel à nommer proactivement. |
| **Delta** | Différence fondamentale et nette : ThreatKG/CTINexus partagent des triplets (entité, relation, entité) — des *faits*. Le CLAIM transmet des *masses de croyance* sur un cadre de discernement Θ, avec m(∅) explicite et statut illocutoire. La distinction tient formellement. |

**Score pertinence NMT-2 :** 3/5 — utile pour l'argumentation défensive si un évaluateur soulève ces travaux
**Score solidité formelle :** 5/5 — distinction formelle béton, démontrable en 2 lignes mathématiques
**Score risque d'intégration :** 1/5 — aucun risque, note défensive dans Partie B si nécessaire

---

### P5 — Reformulation de l'Assertion A

| Axe | Contenu |
|-----|---------|
| **Source** | Analyse interne de la branche : "exactement à l'interface L1→L2" est une sur-spécification fragile. La littérature NeSy confirme le gap à toutes les interfaces inter-agents, pas seulement L1→L2. |
| **Convergence** | La reformulation est plus défendable, plus générale, et mieux étayée par les deux PDFs. Elle élargit la portée du gap sans changer la contribution CLAIM. |
| **Delta** | Le cadre JDL L1/L2 est familier aux évaluateurs MDN. Le remplacer par "interface entre tout nœud de traitement et l'orchestrateur" est plus précis mais moins ancré dans le vocabulaire de référence de l'appel IDEeS. Compromis possible : mentionner les deux formulations. |

**Score pertinence NMT-2 :** 4/5 — renforce la robustesse de l'Assertion A face à un évaluateur expert
**Score solidité formelle :** 5/5 — confirmé par les deux sources indépendantes
**Score risque d'intégration :** 2/5 — modifie une formulation dans CCP-4, pas la spec CLAIM elle-même

---

## III. Tableau de décision consolidé

| Composant | Verdict | Destination | Justification |
|-----------|---------|-------------|---------------|
| **P1** — CLAIM comme pièce manquante G-I-A | **GARDER — usage rhétorique** | CO-1 (formulation "épistémique"), Partie A | Argument fort, analogie valide, risque nul. Ne pas présenter G-I-A comme cadre principal — le mentionner comme confirmation externe. |
| **P2** — Figure 11 comme preuve empirique | **GARDER — citation directe** | Partie B §B.1 ou note dans CCP-4 | Meilleure preuve externe disponible. SPAR-4-SLR, 127 papers, zéros explicites. Citer comme "Hakim et al. 2025". |
| **P3** — Dual-use comme justification règle cardinale | **GARDER — usage justificatif** | Partie B §B.2 (calibration θ_conflit) | Renforce la contrainte de supervision humaine sans modifier la spec. Doit rester dans Partie B, pas Partie A. |
| **P4** — ThreatKG/CTINexus comme précédent à distinguer | **GARDER — note défensive** | Partie B, note de bas de page ou §B.1 | Anticipation proactive d'objection. 1-2 lignes suffisent. Ne pas sur-expliquer. |
| **P5** — Reformulation Assertion A | **GARDER — formulation hybride recommandée** | CCP-4, reformulation de l'Assertion A | Conserver "L1→L2 dans JDL" pour les évaluateurs MDN + ajouter la généralisation NeSy entre parenthèses ou en note. |

---

## IV. Position globale sur la branche

**Verdict de branche : INTÉGRATION PARTIELLE RECOMMANDÉE — usage argumentatif uniquement, aucune modification de la spec CLAIM v1.1.**

La branche BR-2026-CLAIM\_vs\_NeSy-Cyber ne contient aucun élément qui remet en cause la spec. Elle fournit cinq arguments exploitables pour renforcer la démonstration du gap et la justification des contraintes de gouvernance. Le risque d'intégration est minimal sur tous les composants — aucun ne touche à la structure CLAIM, aux champs Partie A, ni aux formules DS/Belnap.

**Chronologie recommandée :**
- **Avant J-0 (soumission) :** P1 → CO-1, P5 → CCP-4 (reformulations mineures de l'argumentation)
- **Dans Partie B (annex GitHub) :** P2, P3, P4 — à intégrer au prochain push de CLAIM\_specification.md v1.2
- **Post-soumission (si extension) :** P1 comme point de départ d'un positionnement CLAIM dans l'écosystème NeSy-Cyber plus large

---

*Ce rapport est produit en branche isolée. Ses conclusions sont soumises à validation par instance analyste avant intégration dans le corpus principal. Seul Andrei peut autoriser la fusion.*
