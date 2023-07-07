def main():
    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(word):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result_string = ''
    for char in word:
        if char not in vowels:
            result_string += char
    return result_string


if __name__ == "__main__":
    main()
