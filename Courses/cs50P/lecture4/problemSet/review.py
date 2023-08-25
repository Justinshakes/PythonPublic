import emoji


def convert_to_emojis(text):
    return emoji.emojize(text)


def main():
    try:
        user_input = input("Input: ")
        converted_input = convert_to_emojis(user_input)
        print("Converted:", converted_input)
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
