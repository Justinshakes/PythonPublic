def convert(user_input):
    emoji_dict = {
        ":)": "🙂",
        ":(": "🙁",
        # Add more conversions here
    }

    print(emoji_dict.items())

    for emoji_code, emoji in emoji_dict.items():
        user_input = user_input.replace(emoji_code, emoji)

    return user_input


def main():
    user_input = convert(input("Emoji Converter: "))
    print(user_input)


if __name__ == "__main__":
    main()
