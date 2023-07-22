from validator_collection import validators


def main():
    email = input("What's Your Email Address: ")
    print(validate_email(email))


def validate_email(email):
    try:
        validators.email(email)
        return "Valid"
    except:
        return "Invalid"


if __name__ == "__main__":
    main()
