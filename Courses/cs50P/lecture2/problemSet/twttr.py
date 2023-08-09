def twitter_string(tweet):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    result = ""

    for char in tweet:
        if char not in vowels:
            result += char

    return result


def main():
    tweet = input("Tweet: ")
    result = twitter_string(tweet)
    print(result)


if __name__ == "__main__":
    main()
