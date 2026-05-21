from app import validate_transfer_limit

def test_transfer():
    assert validate_transfer_limit(5000) == "APPROVED"
