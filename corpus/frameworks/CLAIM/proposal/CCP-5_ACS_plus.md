# CCP-5 — Analyse comparative entre les sexes plus (ACS Plus)
**Version** : 1.1 — 17 mai 2026
**Statut** : FINAL — prêt pour saisie portail PID
**Corps formulaire** : ~2 291 caractères (avec retours de ligne — comptage portail PID)

---

## PARTIE A — Corps formulaire (≤ 2 950 caractères, comptage avec retours de ligne)

Ce projet produit une spécification formelle de protocole. L'ACS Plus s'applique à trois dimensions : la conception du protocole, le processus de validation, et les usages futurs du standard.

Dimension 1 — Conception du protocole. Le CLAIM est neutre par construction : il transporte une masse de croyance, un statut illocutionnaire, une provenance et un horodatage. Ces champs ne portent aucune variable identitaire — le protocole ne traite pas de données sur des individus ou des groupes. Cette neutralité est structurelle : elle découle de la propriété stateless du CLAIM, qui interdit tout état persistant portant une caractéristique d'agent humain.

Cependant, la neutralité du protocole ne garantit pas la neutralité de ses usages. Si les agents en amont sont entraînés sur des données biaisées, le CLAIM transmettra ces biais sans les signaler. Le champ de provenance PROV-O offre un levier d'audit : il permet d'identifier quels agents contribuent à une décision et d'examiner si leurs données d'entraînement présentent des déséquilibres. Cette traçabilité rend visible ce qui était opaque dans les architectures monolithiques.

Dimension 2 — Processus de validation et composition d'équipe. Les scénarios synthétiques couvrent des cas d'usage diversifiés (opérations dans l'Arctique, opérations maritimes, unités tactiques). L'équipe réunit un chercheur principal (NRC Ottawa), un collaborateur technique et un conseiller scientifique externe titulaire d'un doctorat en mathématiques. Cette composition multidisciplinaire réduit les angles morts d'une validation conduite par un profil unique. La spécification est rédigée en français et en anglais pour garantir son accessibilité aux partenaires alliés non francophones et aux équipes FAC bilingues.

Dimension 3 — Usages futurs. La règle cardinale du protocole — l'orchestrateur ne tranche jamais, il expose le conflit à l'opérateur humain — maintient l'humain dans la boucle décisionnelle et empêche toute automatisation de décisions à impact différentiel. La chaîne PROV-O permet une révision après coup des décisions prises avec l'appui du système.

Le livrable est une spécification documentaire à NMT-2. Les questions d'ACS Plus liées au déploiement opérationnel seront documentées comme contraintes pour les phases NMT 4-5.

---

## PARTIE B — Annexe GitHub (hors formulaire PID)

**Références**
- W3C PROV-O (2013) — traçabilité, audit de provenance
- CLAIM_specification.md v1.1 — propriété stateless, chaîne de provenance
- AP6-défi-13 — résultats souhaités, cas d'usage opérationnels
- DEC-S2-06 — règle cardinale de l'orchestrateur

**Note**
Ebenezer est mentionné comme conseiller scientifique (doctorat en mathématiques).
Son accord formel est en attente — si non disponible, un profil équivalent sera identifié.
Marge résiduelle ~659 chars disponible pour enrichissement si nécessaire.
