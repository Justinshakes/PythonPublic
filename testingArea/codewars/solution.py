def is_uppercase(inp):
    for char in inp:
        if char.isalpha() and not char.isupper():
            return False
    return True



def main():
    result1 = is_uppercase("hello I AM DONALD") # False
    print(result1)
    # print(result2)


if __name__ == "__main__":
    main()
