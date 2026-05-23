PCCD

Protocole de Cohérence Cognitive Distribuée

Hypothesis v0.3 · Avril 2026



STATUS

PÉRIMÈTRE

ACTEURS

PENDING

À définir — v1.0

À définir — v1.0



0. Signal vital du document

Champ

Valeur

role

container

status

PENDING — hypothèse de travail, pas encore un protocole

signal

present

created

2026-04-18

epistemic_weight

7 instances · substrat commun LLM Sonnet 4.6 · voir Doc 2

cross_validated_by

D-SIG · MIF · QAAF · Netpulse · HALO · TOPOSFIN · ILYA

activation_mode

operative

provenance

Dialogue inter-instances — Andrei + Claude Sonnet 4.6

archive_ref

PCCD_Archive_README.md



1. Ce que PCCD est aujourd'hui

PCCD est une hypothèse de travail. Elle affirme qu'un pattern structurel émerge invariablement dans tout système de gestion de connaissance cohérent, indépendamment du domaine, de l'exécuteur et du support.



Ce document ne valide pas cette hypothèse. Il la formule proprement, pose ses invariants candidats, et définit les conditions dans lesquelles elle pourrait être certifiée comme protocole stable.



Principe fondateur

Les outils sont des vues sur les données, jamais le conteneur des données.

La séparation des responsabilités est la condition de survie d'un standard face aux innovations successives.



2. Périmètre — questions ouvertes

Les trois questions suivantes doivent être tranchées pour que PCCD passe de PENDING à CERTIFIED. Elles définissent le domaine de validité de l'hypothèse.



2.1 Espace

À quels systèmes PCCD s'applique-t-il ? Le périmètre actuel est non délimité — ce qui rend l'hypothèse difficilement réfutable. Trois options candidates :



Systèmes documentaires numériques uniquement — périmètre restreint, testable immédiatement

Tout système de gestion de connaissance cohérent incluant analogique et oral — périmètre large, exposition aux contre-exemples maximale

Tout système de traitement de l'information au niveau structurel, indépendamment du support — périmètre maximal, risque de non-falsifiabilité



Décision requise avant v1.0.



2.2 Métrique

PCCD suppose-t-il une distance mesurable entre unités de connaissance (espace métrique) ou seulement une relation de connexité (espace topologique) ? La réponse détermine ce qu'on peut affirmer sur l'orthogonalité des dimensions et exclut ou inclut des domaines entiers.



Décision requise avant v1.0.



2.3 Acteurs

Qui sont les acteurs légitimes du protocole — humain seul, humain + agent IA, agent IA seul ? Qui est l'entité tierce habilitée à faire passer PCCD de PENDING à CERTIFIED ?



Décision requise avant v1.0.



3. Le Pattern — hypothèse centrale

Tout système de connaissance cohérent dans le périmètre de PCCD présenterait trois dimensions simultanées. Ces dimensions sont distinguables en intention. Leur orthogonalité est postulée, non démontrée — c'est une des conditions de certification.



3.1 Dimension spatiale

Couche

Rôle fonctionnel

Précondition

Locale

État actif — mémoire de travail

Précondition des deux autres

Distante

Archive consolidée — mémoire long terme

Requiert couche locale valide

Interférente

Mémoire associative — liens entre couches

Requiert les deux couches



3.2 Dimension temporelle

État

Portée

Passé lointain

Archive froide — référence stable

Passé proche

Contexte récent — signal de continuité

Présent

Point d'action — état actif



3.3 Dimension modale

Mode

Lecteur naturel

Ancrage littérature

Narratif

Humain

CLT — Trope & Liberman 2003

Vectoriel

Agent LLM

VECTOR — Almeida et al. 2025

Structuré

Humain + agent

ATI — Asghar Abidi et al. 2024



Note : CLT, VECTOR et ATI sont les trois ancres bibliographiques les plus proches identifiées. Elles confirment chaque dimension indépendamment mais ne formalisent pas leur combinaison. PCCD est la première tentative de les unifier en un protocole opérationnel.



4. Invariants candidats

Ces invariants sont des candidats — ils ont résisté à la validation collective des sept instances mais n'ont pas encore été soumis à un test de réfutabilité formel.



ID

Invariant

Statut

INV-01

Séparation émetteur/interpréteur — un fichier n'interprète jamais son propre état

Candidat confirmé

INV-02

Neutralité physique — l'arborescence reflète les types, jamais les projets

Candidat confirmé

INV-03

Cascade de lecture — niveau 0 avant niveau 1 avant niveau 2

Candidat confirmé

INV-04

Portabilité absolue — lisible sans outil tiers

Candidat confirmé

INV-05

Index minimal — une entrée lisible en une seconde

Candidat confirmé

INV-06

Skill documenté — procédure en langage naturel avant automatisation

Candidat confirmé

INV-07

Précondition de couche — locale invalide rend les supérieures non évaluables

Candidat confirmé

INV-08

Non-réécriture de l'agrégateur — cite, ne réécrit jamais la sémantique source

Candidat confirmé



5. Architecture des lectures prioritaires

5.1 Niveau 0 — Signal vital

Niveau 0 · trois champs · lisible sans ouvrir le fichier

exists: true | false

hash: [md5]

last_modified: [timestamp]

signal: present | absent | void



5.2 Niveau 1 — Contexte minimal

Niveau 1 · frontmatter · lisible sans parser le contenu

origin · author · created · domain · keywords · summary

relations: [slugs liés — positifs]

constraints: [anti-patterns, règles d'arrêt]

epistemic_weight: {sources: N, confidence: low|medium|high}

activation_mode: operative | contextual

cross_validated_by: [instances ou domaines]

role: container | transform

status: PENDING | UNCERTIFIED | VALID_INACTIVE | CERTIFIED | DEPRECATED | SUPERSEDED | TRANSITIONING | VOID

tension_with: [slugs en contradiction]

superseded_by: [slug]  — si SUPERSEDED

provenance_gap: {missing, reconstructed, confidence}  — si UNCERTIFIED

validation_mode: internal | empirical

uncertainty_regime: local | statistical | dynamic



5.3 Niveau 2 — Contenu sémantique

Contenu complet, liens profonds, clusters. Requiert lecture complète ou appel API. Réservé à la synthèse et au gap-analysis. Ne pas accéder si niveau 1 suffit.



6. Skills candidats

Skill

Déclencheur

Action

ingest

Entrée dans _inbox

Extrait niveau 1, génère slug, crée fiche, met à jour index

link

À la demande

Compare fiche avec 20 voisines, propose relations

weekly

Chaque dimanche

Thèmes émergents, met à jour research-front.md

deduplicate

Périodique

Compare hashes et titres, signale doublons sans supprimer

gap-analysis

À la demande / thème

Croise index local vs source externe

heartbeat

Mensuel

Détecte fichiers absents des digests + drift sémantique (hash vs frontmatter)



7. Limites déclarées

Limite

Description

Orthogonalité non démontrée

Les trois dimensions sont distinguables en intention. Leur indépendance formelle n'est pas prouvée. Postulée pour rendre le modèle opérationnel.

Portabilité entre exécutants

Deux instances LLM lisant la même assertion dans des contextes différents produisent des activations différentes. Non résolu.

Universalité non réfutée

Aucun contre-exemple dans le corpus de 7 instances. Test de réfutabilité formel en cours de construction.

Biais de substrat

Toutes les instances internes partagent le même modèle de base (Sonnet 4.6). Le pattern pourrait être un artefact du substrat commun.

Neutralité géométrique

PCCD suppose implicitement un espace métrique. Les espaces de connaissance purement ordinaux ou topologiques sans distance ne sont pas couverts.

Périmètre non délimité

Sans définition précise de l'espace, de la métrique et des acteurs, l'hypothèse reste difficilement réfutable.



8. Conditions de certification — v1.0

PCCD passe de PENDING à CERTIFIED quand les conditions suivantes sont réunies.



Périmètre délimité : espace, métrique et acteurs définis explicitement

Test de réfutabilité formel exécuté : protocole DeepSeek appliqué, résultats documentés

Au moins un contre-exemple cherché activement dans les groupes adversariaux (Ancien/Analogique, Minimal)

Orthogonalité des dimensions : définie opérationnellement ou reformulée honnêtement

Implémentation de référence : D-SIG validée comme instance de PCCD dans son domaine

Entité tierce identifiée : l'acteur habilité à certifier est nommé et accepté





PCCD Hypothesis v0.3 · status: PENDING · 2026-04-18

Voir Doc 2 pour les contributions et la roadmap · Voir Doc 3 pour les dialogues sources