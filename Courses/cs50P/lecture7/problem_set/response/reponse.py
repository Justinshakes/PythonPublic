from validator_collection import validators

try:
    email_address = validators.email(None)
    # Will raise an EmptyValueError
except errors.EmptyValueError:
    # Handling logic goes here
except errors.InvalidEmailError:
    # More handlign logic goes here