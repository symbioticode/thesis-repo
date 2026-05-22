# CCP-2 — Solution nouvelle et innovante
**Version** : 2.0 — 16 mai 2026
**Statut** : FINAL — prêt pour saisie portail PID (tableau → liste textuelle)
**Caractères** : ~2 880 / ~3 000

---

## Corps formulaire (≤ 3 000 caractères)

La revue de littérature conduite en Sprint 1 (quatre sources indépendantes) établit qu'aucun
standard existant ne couvre simultanément les cinq dimensions d'un contrat d'interface épistémique
inter-agents : FIPA-ACL définit les actes illocutionnaires mais ignore la confiance quantifiée,
la fraîcheur et la provenance (1/5). Le TBM de Smets formalise la masse de croyance mais ne
définit pas d'acte de langage ni de traçabilité (1/5). JDL structure les niveaux de fusion sans
interface inter-niveaux formelle (0/5). PROV-O assure la traçabilité sans confiance ni états
épistémiques (2/5). Les protocoles modernes A2A et MCP assurent la provenance mais ignorent
confiance et états épistémiques (1/5). Le CLAIM proposé couvre les cinq dimensions simultanément.

Ce gap est structurel : chaque standard a été conçu pour une communauté distincte. La contribution
originale est leur unification dans un contrat d'interface unique, indépendant de l'implémentation
interne des agents.

Le paradoxe de Zadeh (1979) illustre pourquoi cette unification est nécessaire et non triviale :
la règle de Dempster normalisée efface le conflit entre agents contradictoires au lieu de le
signaler. Aucun protocole de communication inter-agents déployé en contexte ISR ne traite ce
paradoxe au niveau de l'interface. Le CLAIM le résout en imposant la conservation de m(∅) comme
invariant du protocole — pas comme choix d'implémentation, mais comme contrat.

Troisième différenciateur : la valeur Neither de Belnap, représentant « je n'ai pas observé »
distinctement de « j'ai observé l'absence », est absente de tous les protocoles existants. Pour
un système ISR, un sonar silencieux dans un secteur hostile n'émet pas la même information qu'un
sonar non consulté. Sans ce champ, l'orchestrateur produit une fausse confiance.

Notre proposition se distingue également des architectures neuro-symboliques intégrées comme
DeepProbLog ou NS-CL : au lieu de fusionner apprentissage et raisonnement dans un seul modèle,
nous définissons l'interface standardisée qui permet à tout agent ML — y compris ces systèmes —
d'opérer dans une architecture distribuée et auditable. Le gap adressé n'est pas dans
l'algorithme de fusion, mais dans le protocole de communication que ces algorithmes n'ont pas.

Hypothèse de travail (DEC-S2-08) : l'alignement spatio-temporel (C-02) et la résolution
d'entités (C-03) sont supposés résolus en amont — couches à NMT 4-5, hors périmètre documenté.
La proposition vise NMT-2 (spécification) avec trajectoire vers NMT-3 (validation analytique
sur données synthétiques, modalité autorisée par Q3/R4).

---

## Références citées dans cette section

- Zadeh (1979) — paradoxe, motivation centrale
- Smets & Kennes (1994) — TBM, m(∅) conservé
- Belnap (1977) — Neither, silence qualifié
- FIPA-ACL, JDL, PROV-O, A2A — standards différenciés
- Manhaeve et al. (2018) — DeepProbLog
- MIT NSCL (2019) — NS-CL
- Q&R AP6-défi-13 Q3/R4 — données synthétiques

---

## Note de calibrage

Marge ~120 caractères disponibles. QO-FORM-01 FERMÉ : liste textuelle intégrée.
Révision globale cohérence : J17.
