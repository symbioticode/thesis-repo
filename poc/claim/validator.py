import logging
from datetime import datetime, timezone
from typing import Dict, Any, Tuple
from .structures import Claim, Illocution, Freshness, Provenance

# Configuration du logger
logger = logging.getLogger(__name__)

class ClaimValidator:
    """
    Validateur de CLAIM implémentant la cascade de validation B.1 (3 niveaux).
    """

    def __init__(self, tolerance: float = 1e-6):
        self.tolerance = tolerance

    def validate(self, data: Dict[str, Any], t_reception: datetime = None) -> Tuple[bool, str]:
        """
        Valide un dictionnaire de données CLAIM et retourne (is_valid, reason).
        """
        if t_reception is None:
            t_reception = datetime.now(timezone.utc)

        try:
            # Niveau 0 : Structure et types obligatoires
            is_valid, reason = self._validate_structure(data)
            if not is_valid:
                return False, f"Niveau 0: {reason}"

            # Niveau 1 : Validité sémantique (Masse, Illocution, Provenance)
            is_valid, reason = self._validate_semantics(data)
            if not is_valid:
                return False, f"Niveau 1: {reason}"

            # Niveau 2 : Validité temporelle (Freshness)
            is_valid, reason = self._validate_temporal(data, t_reception)
            if not is_valid:
                return False, f"Niveau 2: {reason}"

            return True, "Valid"

        except Exception as e:
            return False, f"Exception durant la validation: {str(e)}"

    def _validate_structure(self, data: Dict[str, Any]) -> Tuple[bool, str]:
        required = ["proposition", "belief_mass", "illocution", "freshness", "provenance"]
        for field in required:
            if field not in data:
                return False, f"Champ manquant: {field}"

        if not isinstance(data["belief_mass"], dict):
            return False, "belief_mass doit être un dictionnaire"

        if not isinstance(data["freshness"], dict) or "t_obs" not in data["freshness"] or "delta_t_valid" not in data["freshness"]:
            return False, "freshness malformé"

        if not isinstance(data["provenance"], dict) or "chain_id" not in data["provenance"]:
            return False, "provenance malformée"

        return True, "Structure OK"

    def _validate_semantics(self, data: Dict[str, Any]) -> Tuple[bool, str]:
        # Masse : Somme = 1.0 (± tolerance)
        masses = data["belief_mass"]
        total_mass = sum(masses.values())
        if abs(total_mass - 1.0) > self.tolerance:
            return False, f"Somme des masses != 1.0 ({total_mass})"

        # Illocution : Dans l'énumération
        try:
            Illocution(data["illocution"])
        except ValueError:
            return False, f"Illocution invalide: {data['illocution']}"

        # Provenance : chain_id présent
        if not data["provenance"].get("chain_id"):
            return False, "chain_id absent dans provenance"

        return True, "Sémantique OK"

    def _validate_temporal(self, data: Dict[str, Any], t_reception: datetime) -> Tuple[bool, str]:
        freshness = data["freshness"]
        t_obs = freshness["t_obs"]
        if isinstance(t_obs, str):
            t_obs = datetime.fromisoformat(t_obs.replace("Z", "+00:00"))

        if not t_obs.tzinfo:
            t_obs = t_obs.replace(tzinfo=timezone.utc)

        # Timestamp futur
        if t_obs > t_reception:
            return False, "t_obs dans le futur"

        # Validité expirée
        delta_t_valid = freshness["delta_t_valid"]
        if (t_reception - t_obs).total_seconds() > delta_t_valid:
            return False, "CLAIM expiré"

        return True, "Temporel OK"

    def to_claim(self, data: Dict[str, Any]) -> Claim:
        """
        Convertit un dictionnaire validé en objet Claim.
        """
        fresh_data = data["freshness"]
        t_obs = fresh_data["t_obs"]
        if isinstance(t_obs, str):
            t_obs = datetime.fromisoformat(t_obs.replace("Z", "+00:00"))
        if not t_obs.tzinfo:
            t_obs = t_obs.replace(tzinfo=timezone.utc)

        prov_data = data["provenance"]

        return Claim(
            proposition=data["proposition"],
            belief_mass=data["belief_mass"],
            illocution=Illocution(data["illocution"]),
            freshness=Freshness(t_obs=t_obs, delta_t_valid=fresh_data["delta_t_valid"]),
            provenance=Provenance(
                chain_id=prov_data["chain_id"],
                entity_id=prov_data.get("entity_id"),
                agent_id=prov_data.get("agent_id"),
                activity_id=prov_data.get("activity_id")
            )
        )
