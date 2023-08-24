def multi_table(number):
    result = ""
    counter = 1
    while counter <= 10:
        result += f"{counter} * {number} = {number * counter}\n"
        counter += 1
    return result.strip()  # Remove leading and trailing whitespace


def main():
    result = multi_table(5)
    print(result)


main()
