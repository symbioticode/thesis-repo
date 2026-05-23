from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Tuple, Optional

class Illocution(Enum):
    OBSERVE = "OBSERVE"
    INFER = "INFER"
    DEDUCE = "DEDUCE"
    ASSUME = "ASSUME"

@dataclass(frozen=True)
class Freshness:
    t_obs: datetime
    delta_t_valid: float

@dataclass(frozen=True)
class Provenance:
    chain_id: str
    entity_id: Optional[str] = None
    agent_id: Optional[str] = None
    activity_id: Optional[str] = None

@dataclass(frozen=True)
class Claim:
    proposition: str
    belief_mass: Dict[str, float]  # Clés: "H1", "H1|H2", "Theta", "empty"
    illocution: Illocution
    freshness: Freshness
    provenance: Provenance

class BelnapState(Enum):
    T = "T"  # True (Accord sur H)
    F = "F"  # False (Accord sur ¬H)
    B = "B"  # Both (Contradiction)
    N = "N"  # None (Silence qualifié ou ignorance)

@dataclass(frozen=True)
class EpistemicState:
    belnap_state: BelnapState
    conflict_mass: float
    pcr5_source: List[Tuple[str, str, str]]  # (agent_i, agent_j, hyp_conflit)
    freshness: datetime
