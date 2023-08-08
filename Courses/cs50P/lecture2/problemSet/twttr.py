def twitter_string(string):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    result = ""

    for char in string:
        if char not in vowels:
            result += char

    return result


def main():
    user_string = input("Twitter Input: ")
    result = twitter_string(user_string)
    print(result)


if __name__ == "__main__":
    main()
