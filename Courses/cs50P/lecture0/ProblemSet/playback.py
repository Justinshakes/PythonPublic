def lower_case(s):
    return s.casefold()


def main():
    user_input = lower_case(input("Input String: "))
    print(user_input)


if __name__ == "__main__":
    main()
