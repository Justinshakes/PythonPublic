def convert_to_snake_case(string):
    result = ""

    for char in string:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char

    return result


def main():
    user_input = input("camelCase: ")

    snake_case = convert_to_snake_case(user_input)
    print(snake_case)


if __name__ == "__main__":
    main()
