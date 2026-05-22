from app.transfer_limit import validate_transfer_limit

def test_transfer_under_threshold_is_approved():
    assert validate_transfer_limit(5000) == "APPROVED"

def test_transfer_over_threshold_requires_approval():
    assert validate_transfer_limit(15000) == "REQUIRES_APPROVAL"
