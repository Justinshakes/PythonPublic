def is_palindrome(original_string):
    original_string = original_string.lower()
    reversed_string = original_string[::-1]
    return original_string == reversed_string


def main():
    s = input("Input: ")
    print(is_palindrome(s))


main()
