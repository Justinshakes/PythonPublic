def convert(user_input):
    if ":)" in user_input:
        return user_input.replace(":)", "🙂")
    if ":(" in user_input:
        return user_input.replace(":(", "🙁")
    return user_input


def main():
    user_input = input("Enter String: ")
    result = convert("Enter String: ")
    print(result)


if __name__ == "__main__":
    main()
