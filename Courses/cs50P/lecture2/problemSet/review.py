def is_valid(plate):
    return (
        check_length(plate)
        and check_first_two(plate)
        and check_numbers_at_end(plate)
        and check_no_punctuation(plate)
    )


def check_length(plate):
    return 2 <= len(plate) <= 6


def check_first_two(plate):
    return plate[:2].isalpha()


def check_numbers_at_end(plate):
    found_number = False

    for i in range(2, len(plate)):
        if plate[i].isnumeric() and not found_number and plate[i] == "0":
            return False
        if plate[i].isalpha() and found_number:
            return False
        if plate[i].isnumeric() and not found_number:
            found_number = True

    return True


def check_no_punctuation(plate):
    return plate.isalnum()


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
