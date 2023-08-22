def playback(user_input):
    return user_input.replace(" ", "...")


def main():
    user_input = playback(input("Input: "))
    print(user_input)


if __name__ == "__main__":
    main()
