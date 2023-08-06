def meaning_of_life(user_input):
    if user_input == "42" or user_input == "forty-two" or user_input == "forty two":
        return "Yes"
    return "No"


def main():
    user_input = input("What is the meaning of life? ")
    answer = meaning_of_life(user_input.strip().casefold())
    print(answer)


if __name__ == "__main__":
    main()
