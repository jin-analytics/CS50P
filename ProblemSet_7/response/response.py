import sys
from validator_collection import validators, checkers, errors
# Validator:    email
# Checkers:     is_email

def main():
    try:
        # The value of email_address will now be "test@domain.dev"
        #email_address = validators.email(input('What's your email adress '))#
        email_address = validators.email("testdomain.dev")

        if checkers.is_email(email_address) == True:
            print('Valid')


    except errors.EmptyValueError:
        sys.exit('Invalid')
        # Handling logic goes here
    except errors.InvalidEmailError:
        # More handlign logic goes here
        sys.exit('Invalid')

if __name__ == "__main__":
    main()
