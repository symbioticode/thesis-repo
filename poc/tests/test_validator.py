import pytest
from datetime import datetime, timedelta, timezone
from poc.claim.validator import ClaimValidator
from poc.claim.structures import Illocution

@pytest.fixture
def validator():
    return ClaimValidator()

@pytest.fixture
def valid_data():
    now = datetime.now(timezone.utc)
    return {
        "proposition": "Test hypothesis",
        "belief_mass": {"H1": 0.7, "Theta": 0.3},
        "illocution": "OBSERVE",
        "freshness": {
            "t_obs": now.isoformat(),
            "delta_t_valid": 60
        },
        "provenance": {
            "chain_id": "urn:test:chain"
        }
    }

def test_validate_success(validator, valid_data):
    is_valid, reason = validator.validate(valid_data)
    assert is_valid
    assert reason == "Valid"

def test_validate_missing_field(validator, valid_data):
    del valid_data["proposition"]
    is_valid, reason = validator.validate(valid_data)
    assert not is_valid
    assert "Niveau 0" in reason
    assert "Champ manquant: proposition" in reason

def test_validate_invalid_mass(validator, valid_data):
    valid_data["belief_mass"] = {"H1": 0.5, "Theta": 0.2} # Sum = 0.7
    is_valid, reason = validator.validate(valid_data)
    assert not is_valid
    assert "Niveau 1" in reason
    assert "Somme des masses != 1.0" in reason

def test_validate_invalid_illocution(validator, valid_data):
    valid_data["illocution"] = "INVALID"
    is_valid, reason = validator.validate(valid_data)
    assert not is_valid
    assert "Niveau 1" in reason
    assert "Illocution invalide" in reason

def test_validate_future_timestamp(validator, valid_data):
    future = datetime.now(timezone.utc) + timedelta(minutes=10)
    valid_data["freshness"]["t_obs"] = future.isoformat()
    is_valid, reason = validator.validate(valid_data)
    assert not is_valid
    assert "Niveau 2" in reason
    assert "t_obs dans le futur" in reason

def test_validate_expired(validator, valid_data):
    past = datetime.now(timezone.utc) - timedelta(minutes=10)
    valid_data["freshness"]["t_obs"] = past.isoformat()
    valid_data["freshness"]["delta_t_valid"] = 60 # 1 minute
    is_valid, reason = validator.validate(valid_data)
    assert not is_valid
    assert "Niveau 2" in reason
    assert "CLAIM expiré" in reason

def test_to_claim(validator, valid_data):
    is_valid, reason = validator.validate(valid_data)
    assert is_valid
    claim = validator.to_claim(valid_data)
    assert claim.proposition == "Test hypothesis"
    assert claim.belief_mass["H1"] == 0.7
    assert claim.illocution == Illocution.OBSERVE
    assert isinstance(claim.freshness.t_obs, datetime)
    assert claim.provenance.chain_id == "urn:test:chain"

def test_validate_exception(validator):
    # Pass something that isn't a dict to trigger exception in validate
    is_valid, reason = validator.validate(None)
    assert not is_valid
    assert "Exception durant la validation" in reason

def test_validate_belief_mass_not_dict(validator, valid_data):
    valid_data["belief_mass"] = [0.7, 0.3]
    is_valid, reason = validator.validate(valid_data)
    assert not is_valid
    assert "belief_mass doit être un dictionnaire" in reason

def test_validate_freshness_malformed(validator, valid_data):
    valid_data["freshness"] = "not a dict"
    is_valid, reason = validator.validate(valid_data)
    assert not is_valid
    assert "freshness malformé" in reason

def test_validate_provenance_malformed(validator, valid_data):
    valid_data["provenance"] = {"no_chain_id": "none"}
    is_valid, reason = validator.validate(valid_data)
    assert not is_valid
    assert "provenance malformée" in reason

def test_validate_chain_id_empty(validator, valid_data):
    valid_data["provenance"]["chain_id"] = ""
    is_valid, reason = validator.validate(valid_data)
    assert not is_valid
    assert "chain_id absent dans provenance" in reason

def test_validate_t_obs_no_tz(validator, valid_data):
    # datetime without timezone (naive)
    # We use utcnow() to get a naive UTC datetime to test the validator's timezone addition logic
    valid_data["freshness"]["t_obs"] = datetime.now(timezone.utc).replace(tzinfo=None)
    is_valid, reason = validator.validate(valid_data)
    # It should still be valid as we add UTC in validator
    assert is_valid

def test_to_claim_t_obs_no_tz(validator, valid_data):
    # We use utcnow() to get a naive UTC datetime
    valid_data["freshness"]["t_obs"] = datetime.now(timezone.utc).replace(tzinfo=None)
    validator.validate(valid_data)
    claim = validator.to_claim(valid_data)
    assert claim.freshness.t_obs.tzinfo is not None
