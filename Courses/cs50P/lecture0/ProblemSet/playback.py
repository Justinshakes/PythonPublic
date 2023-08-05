def playback(user_input):
    return user_input.replace(" ", "...")


def main():
    user_input = input("Input String: ")
    user_input = playback(user_input)
    print(user_input)


if __name__ == "__main__":
    main()
