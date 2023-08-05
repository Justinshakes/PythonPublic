def deep_thought(user_input):
    if user_input == "42" or user_input == "forty-two" or user_input == "forty two":
        return "Yes"
    return "No"


def main():
    print(deep_thought(input("What is the Answer to the Great Question of Life, "
                             "the Universe, and Everything? ")))


if __name__ == "__main__":
    main()
