def string_clean(s):
    result = ""
    for char in s:
        if not char.isnumeric():
            result += char
    return result


def main():
    result1 = string_clean("")  # ""
    result2 = string_clean("! !")  # ! !
    result3 = string_clean("123456789")  # , "")
    result4 = string_clean("(E3at m2e2!!)")  # , "(Eat me!!)")

    print(result1)
    print(result2)
    print(result3)
    print(result4)


main()
