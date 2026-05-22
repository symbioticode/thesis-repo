"""
S-04 — Contraste FIPA-ACL vs CLAIM
Projet IDEeS AP6-defi-13 — Protocole d'echange epistemique
Version : 1.0 — 18 mai 2026

Objectif : demontrer, par absence de champ, que des messages FIPA-ACL-like
ne permettent pas a un orchestrateur de calculer m(vide) ni de declencher
une escalade fondee sur une metrique de conflit.

Ce script ne pretend pas implementer FIPA-ACL. Il simule le format minimal
qu'un agent conforme FIPA-ACL produirait pour le meme scenario que S-01,
et montre que l'information necessaire a la detection de conflit est absente.

Usage : python s04_fipa_contrast.py
Reproductibilite : stdlib uniquement, zero dependance externe, deterministe.
"""

import sys
import os

# --- Import tbm_utils pour la partie CLAIM (meme scenario que S-01) ---
sys.path.insert(0, os.path.dirname(__file__))
try:
    from tbm_utils import tbm_conjunctive, derive_belnap, THETA, EMPTY
    TBM_AVAILABLE = True
except ImportError:
    TBM_AVAILABLE = False


# ===========================================================================
# CONSTANTES
# ===========================================================================

THETA_CONFLIT = 0.30   # seuil NMT-2 (conservateur, DEC-S3-03)


# ===========================================================================
# PARTIE A — FORMAT FIPA-ACL-LIKE
# ===========================================================================

def simuler_messages_fipa():
    """
    Simule deux messages FIPA-ACL conformes pour le scenario S-01.

    Un message FIPA-ACL comprend : performative, sender, receiver, content.
    La semantique BDI de FIPA-ACL autorise un champ 'uncertain' optionnel,
    mais celui-ci ne porte pas de distribution de masse sur 2^Theta —
    c'est un flag booleen de l'agent sur sa propre croyance, pas une mesure
    de conflit inter-agents.

    Source : FIPA Consortium, "FIPA ACL Message Structure Specification"
             (FIPA SC00061G, 2002), sections 3.2.3 et 4.
    """
    msg_radar = {
        "performative" : "INFORM",
        "sender"       : "Radar",
        "receiver"     : "Orchestrateur",
        "content"      : "target_class=military",
        # Champ 'uncertain' BDI optionnel — non standard, booleen
        # "uncertain"  : True   # <-- si present, flag booleen, PAS une masse
    }

    msg_sigint = {
        "performative" : "INFORM",
        "sender"       : "SIGINT",
        "receiver"     : "Orchestrateur",
        "content"      : "target_class=civilian",
    }

    return msg_radar, msg_sigint


def orchestrateur_fipa(msg1, msg2):
    """
    Tente de detecter un conflit entre deux messages FIPA-ACL-like.
    Retourne un diagnostic structure.
    """
    # Champs disponibles
    champs_disponibles = set(msg1.keys()) | set(msg2.keys())

    # Tentative de calcul de m(vide)
    m_empty_calculable = (
        "belief_mass" in msg1 and
        "belief_mass" in msg2
    )

    # Tentative de derivation d'un etat epistemique
    etat_epistemique_derivable = m_empty_calculable  # requiert m(vide)

    # Tentative de declenchement d'escalade metrique
    escalade_metrique_possible = m_empty_calculable  # requiert m(vide) >= theta

    # Ce que l'orchestrateur peut faire : comparaison textuelle des content
    contenu_1 = msg1.get("content", "")
    contenu_2 = msg2.get("content", "")
    desaccord_textuel = contenu_1 != contenu_2

    return {
        "champs_disponibles"          : sorted(champs_disponibles),
        "belief_mass_present"         : "belief_mass" in champs_disponibles,
        "m_empty_calculable"          : m_empty_calculable,
        "etat_epistemique_derivable"  : etat_epistemique_derivable,
        "escalade_metrique_possible"  : escalade_metrique_possible,
        "desaccord_textuel_detecte"   : desaccord_textuel,
        "decision_orchestrateur"      : (
            "DESACCORD TEXTUEL DETECTE — heuristique ad hoc ou silence"
            if desaccord_textuel
            else "AUCUNE DIFFERENCE DETECTEE"
        ),
    }


# ===========================================================================
# PARTIE B — FORMAT CLAIM (meme scenario S-01)
# ===========================================================================

def simuler_claims_s01():
    """
    Reproduit les deux CLAIM du scenario S-01 (s01_tbm_minimal.py).
    Les masses sont identiques a S-01 pour permettre la comparaison directe.
    """
    if not TBM_AVAILABLE:
        return None, None

    # Masses S-01 (identiques)
    H1    = frozenset({"H1"})
    H2    = frozenset({"H2"})
    THETA_SET = frozenset({"H1", "H2", "H3"})

    claim_radar = {
        "sender"       : "Radar",
        "illocution"   : "OBSERVE",
        "belief_mass"  : {H1: 0.70, THETA_SET: 0.30},
        "hypothesis"   : "H1",
        "provenance"   : "urn:sensor:radar:FR-001",
        "freshness"    : {"t_obs": 1000.0, "delta_t_valid": 300},
    }

    claim_sigint = {
        "sender"       : "SIGINT",
        "illocution"   : "INFER",
        "belief_mass"  : {H2: 0.60, THETA_SET: 0.40},
        "hypothesis"   : "H2",
        "provenance"   : "urn:sensor:sigint:FR-002",
        "freshness"    : {"t_obs": 1005.0, "delta_t_valid": 300},
    }

    return claim_radar, claim_sigint


def orchestrateur_claim(claim1, claim2):
    """
    Detecte le conflit entre deux CLAIM en utilisant TBM conjunctif.
    """
    if not TBM_AVAILABLE or claim1 is None:
        return None

    m1 = claim1["belief_mass"]
    m2 = claim2["belief_mass"]

    combined  = tbm_conjunctive(m1, m2)
    m_empty   = combined.get(EMPTY, 0.0)
    state     = derive_belnap(combined, theta=THETA_CONFLIT)

    escalade  = state == "B"

    return {
        "m_empty"              : round(m_empty, 4),
        "belnap_state"         : state,
        "theta_conflit"        : THETA_CONFLIT,
        "escalade_declenchee"  : escalade,
        "source_conflit"       : (
            f"{claim1['sender']} ({claim1['hypothesis']}) "
            f"vs {claim2['sender']} ({claim2['hypothesis']})"
            if escalade else "N/A"
        ),
        "decision_orchestrateur" : (
            "ESCALADE HUMAINE REQUISE — conflit inter-agents confirme"
            if escalade
            else "PAS D'ESCALADE — conflit sous le seuil"
        ),
    }


# ===========================================================================
# AFFICHAGE
# ===========================================================================

def afficher_separation(titre=""):
    largeur = 70
    if titre:
        print(f"\n{'=' * ((largeur - len(titre) - 2) // 2)} {titre} "
              f"{'=' * ((largeur - len(titre) - 2) // 2)}")
    else:
        print("=" * largeur)


def main():
    afficher_separation()
    print("S-04 — Contraste FIPA-ACL vs CLAIM (IDEeS Defi 13)")
    print("Scenario : Radar croit {H1=militaire}, SIGINT croit {H2=civil}")
    afficher_separation()

    # ------------------------------------------------------------------
    # PARTIE A — FIPA-ACL
    # ------------------------------------------------------------------
    afficher_separation("PARTIE A : FORMAT FIPA-ACL-LIKE")

    msg_radar, msg_sigint = simuler_messages_fipa()
    diag_fipa = orchestrateur_fipa(msg_radar, msg_sigint)

    print("\nMessage Radar  :", msg_radar)
    print("Message SIGINT :", msg_sigint)
    print()
    print("Diagnostic orchestrateur (FIPA-ACL) :")
    print(f"  Champs disponibles         : {diag_fipa['champs_disponibles']}")
    print(f"  belief_mass present        : {diag_fipa['belief_mass_present']}  "
          f"<-- ABSENT")
    print(f"  m(vide) calculable         : {diag_fipa['m_empty_calculable']}  "
          f"<-- IMPOSSIBLE")
    print(f"  Etat epistemique derivable : {diag_fipa['etat_epistemique_derivable']}  "
          f"<-- IMPOSSIBLE")
    print(f"  Escalade metrique possible : {diag_fipa['escalade_metrique_possible']}  "
          f"<-- IMPOSSIBLE")
    print(f"  Desaccord textuel detecte  : {diag_fipa['desaccord_textuel_detecte']}  "
          f"<-- comparaison de chaines uniquement")
    print()
    print(f"  DECISION : {diag_fipa['decision_orchestrateur']}")
    print()
    print("  => L'orchestrateur sait que les deux agents disent des choses")
    print("     differentes. Il ne sait PAS a quel point. Il ne peut PAS")
    print("     calculer m(vide)=0.42, ni declencher une escalade fondee")
    print("     sur ce chiffre, ni localiser la paire conflictuelle.")

    # ------------------------------------------------------------------
    # PARTIE B — CLAIM
    # ------------------------------------------------------------------
    afficher_separation("PARTIE B : FORMAT CLAIM (meme scenario)")

    if not TBM_AVAILABLE:
        print("\n  [ATTENTION] tbm_utils non disponible — partie B ignoree.")
        print("  Placer tbm_utils.py dans le meme repertoire que ce script.")
    else:
        claim_radar, claim_sigint = simuler_claims_s01()
        diag_claim = orchestrateur_claim(claim_radar, claim_sigint)

        print("\nCLAIM Radar  : belief_mass =",
              {str(k): v for k, v in claim_radar["belief_mass"].items()})
        print("CLAIM SIGINT : belief_mass =",
              {str(k): v for k, v in claim_sigint["belief_mass"].items()})
        print()
        print("Diagnostic orchestrateur (CLAIM) :")
        print(f"  m(vide) calcule            : {diag_claim['m_empty']}  "
              f"<-- CONFLIT QUANTIFIE")
        print(f"  Etat Belnap                : {diag_claim['belnap_state']}  "
              f"<-- B = contradiction confirmee")
        print(f"  Seuil theta_conflit        : {diag_claim['theta_conflit']}")
        print(f"  Escalade declenchee        : {diag_claim['escalade_declenchee']}  "
              f"<-- DECISION FONDEE SUR METRIQUE")
        print(f"  Source du conflit          : {diag_claim['source_conflit']}")
        print()
        print(f"  DECISION : {diag_claim['decision_orchestrateur']}")

    # ------------------------------------------------------------------
    # COMPARAISON
    # ------------------------------------------------------------------
    afficher_separation("COMPARAISON")
    print()
    print(f"  {'Capacite orchestrateur':<40}  {'FIPA-ACL':<12}  {'CLAIM'}")
    print(f"  {'-'*40}  {'-'*12}  {'-'*12}")
    print(f"  {'Detecter un desaccord':<40}  {'Oui (texte)':<12}  {'Oui (masse)'}")
    print(f"  {'Quantifier le conflit (m(vide))':<40}  {'Non':<12}  {'0.4200'}")
    print(f"  {'Deriver etat epistemique (Belnap)':<40}  {'Non':<12}  {'B'}")
    print(f"  {'Declencher escalade sur metrique':<40}  {'Non':<12}  {'Oui (>= 0.30)'}")
    print(f"  {'Localiser la paire conflictuelle':<40}  {'Non':<12}  {'Radar/SIGINT'}")
    print(f"  {'Tracer la provenance':<40}  {'Non':<12}  {'Oui (URN)'}")
    print()
    print("  Conclusion : FIPA-ACL detecte le symptome (deux messages differents).")
    print("  CLAIM detecte, quantifie, localise et escalade le conflit")
    print("  de facon auditable et reproductible.")
    afficher_separation()


if __name__ == "__main__":
    main()
