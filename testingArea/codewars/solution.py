def divisible_by(numbers, divisor):
    result = []
    for num in numbers:
        if num % divisor == 0:
            result.append(num)
    return result


def main():
    result1 = divisible_by([0,1,2,3,4,5,6], 4) # [0,4]
    print(result1)
    # print(result2)


if __name__ == "__main__":
    main()
