def validate_transfer_limit(amount):
    if amount > 10000:
        return "REQUIRES_APPROVAL"
    return "APPROVED"

print(validate_transfer_limit(5000))
