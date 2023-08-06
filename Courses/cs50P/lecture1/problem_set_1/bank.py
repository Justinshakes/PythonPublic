def greetings(user_input):
    if "hello" in user_input:
        return "$0"
    elif user_input.startswith("h"):
        return "$20"
    else:
        return "$100"


def main():
    user_input = input("Greeting: ")
    pay_out = greetings(user_input.lower())
    print(pay_out)


if __name__ == "__main__":
    main()
