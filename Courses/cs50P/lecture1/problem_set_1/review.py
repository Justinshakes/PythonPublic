def meaning_of_life(user_input):
    if user_input == "42" or user_input == "forty-two" or user_input == "fortytwo":
        return "Yes"
    return "No"


def main():
    user_input = input("what is the meaning of life? ")
    answer = meaning_of_life(user_input)
    print(answer)


if __name__ == "__main__":
    main()
