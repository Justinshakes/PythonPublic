def remove_every_other(my_list):
    return my_list[::2]


def main():
    result1 = remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # [1, 3, 5, 7, 9])
    result2 = remove_every_other(["Hello", "Goodbye", "Hello Again"])
    #  ['Hello', 'Hello Again'])
    print(result1)
    print(result2)


if __name__ == "__main__":
    main()
