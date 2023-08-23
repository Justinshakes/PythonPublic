def sum_str(a, b):
    if not a:
        a = 0
    if not b:
        b = 0
    return str(int(a) + int(b))


def main():
    result = sum_str("4", "5")
    print(result)


main()
