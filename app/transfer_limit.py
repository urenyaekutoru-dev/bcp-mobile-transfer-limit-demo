def validate_transfer_limit(amount: int) -> str:
    if amount > 10000:
        return "REQUIRES_APPROVAL"
    return "APPROVED"
