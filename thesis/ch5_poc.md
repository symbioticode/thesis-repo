# Chapitre 5 — Preuve de Concept : Le protocole CLAIM

## 5.1 Objectif du PoC

Le but de cette preuve de concept (PoC) est de démontrer par l'absurde et par la solution l'utilité du protocole CLAIM dans un système multi-agents. Nous simulons un scénario de fusion d'assertions contradictoires pour observer comment les deux approches (naïve vs CLAIM) gèrent l'incertitude et le conflit.

Le PoC se concentre sur le chaînon manquant identifié au Chapitre 1 : l'interface entre la connaissance produite en temps réel par des agents et la prise de décision automatisée.

## 5.2 Scénario A : Démonstration du problème (Fusion naïve)

Dans ce scénario, trois agents émettent des assertions sur une même hypothèse $H_2$ avec des masses de croyance contradictoires.
*   **Méthode** : Application de la règle de combinaison de Dempster standard avec normalisation.
*   **Résultat observé** : La masse de conflit $m(\emptyset)$ est artificiellement réduite à zéro par la normalisation. Le système produit une décision en faveur de $H_2$ avec une confiance apparente élevée (~0.87).
*   **Conclusion** : Le conflit est "balayé sous le tapis". L'orchestrateur est aveugle à la contradiction interne des agents, ce qui conduit à une décision automatique potentiellement fausse mais affichée avec certitude.

## 5.3 Scénario B : Démonstration de la solution (Protocole CLAIM)

Le même scénario est rejoué en appliquant le pipeline complet du protocole CLAIM.
*   **Validation** : Chaque assertion est d'abord passée au travers du `validator.py` pour vérifier sa structure et sa provenance.
*   **Combinaison TBM** : Utilisation de la règle conjonctive non normalisée de Smets. La masse de conflit $m(\emptyset)$ est conservée comme une donnée explicite.
*   **Analyse Belnap** : L'état épistémique est dérivé. Dans ce cas, $m(\emptyset) = 0.41$.
*   **Escalade** : Le seuil de conflit $\theta_{conflit}$ étant fixé à 0.30, le dépassement ($0.41 > 0.30$) déclenche immédiatement la suspension de la décision automatique.

### Sortie du système CLAIM :
```
[AVEC CLAIM] m(∅) combiné : 0.41  ← > θ_conflit (0.30)
[AVEC CLAIM] Belnap : B (Both — contradiction diagnostique)
[AVEC CLAIM] Conflit localisé : Agent_1 vs Agent_3 sur H2
[AVEC CLAIM] Décision automatique : SUSPENDUE
[AVEC CLAIM] Escalade C-07 : OUI
```

## 5.4 Conclusion du PoC

Le PoC valide opérationnellement les principes de la thèse :
1.  **La détection du conflit** est possible grâce à la conservation de la masse $m(\emptyset)$ (Smets).
2.  **L'explicabilité** est assurée par la localisation du conflit (PCR5 minimal) entre les agents spécifiques.
3.  **La sécurité du système** est garantie par le mécanisme d'escalade humaine, empêchant une décision automatique basée sur des croyances irréconciliables.

Ce PoC, bien que minimal, constitue l'implémentation de référence du contrat d'interface épistémique pour les systèmes de fusion en temps réel.
