def get_average(marks):
    total = sum(marks) / len(marks)
    return int(total)


def main():
    result1 = get_average([2, 5, 13, 20, 16, 16, 10])  # 11
    print(result1)


if __name__ == "__main__":
    main()
