def square_or_square_root(arr):
    result = []
    for num in arr:
        square_root = num ** 0.5
        if square_root.is_integer():
            result.append(int(square_root))
        else:
            result.append(num ** 2)
    return result


def main():
    result1 = square_or_square_root([4, 3, 9, 7, 2, 1])  # [2, 9, 3, 49, 4, 1]
    print(result1)
    # print(result2)


if __name__ == "__main__":
    main()
