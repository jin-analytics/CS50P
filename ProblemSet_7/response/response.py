from validator_collection import validators, checkers, errors

email_address = validators.email('testdomain.dev')
# The value of email_address will now be "test@domain.dev"
print(checkers.is_email(email_address))

# Validator:    email
# Checkers:     is_email
