from validator_collection import validators, checkers, errors
# Validator:    email
# Checkers:     is_email

def main():
    email_validation(input("What's your email adress? "))

def email_validation(email_adress):
    try:
        email_address = validators.email(email_adress)
        if checkers.is_email(email_address) == True:
            print('Valid')

    except errors.EmptyValueError:
        print('Invalid')

    except errors.InvalidEmailError:
        print('Invalid')

if __name__ == "__main__":
    main()
