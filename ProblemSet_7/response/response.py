from validator_collection import validators, checkers, errors

email_address = validators.email('test@domain.dev')
# The value of email_address will now be "test@domain.dev"

# Validator:    email
# Checkers:     is_email
