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