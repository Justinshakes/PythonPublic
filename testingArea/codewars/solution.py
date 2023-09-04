def invert(lst):
    result = []
    for num in lst:
        if num <= 0:
            result.append(abs(num))
        else:
            result.append(num * -1)
    return result


def main():
    result1 = invert([1, -2, 3, -4, 5])  # [-1,2,-3,4,-5
    print(result1)


if __name__ == "__main__":
    main()
