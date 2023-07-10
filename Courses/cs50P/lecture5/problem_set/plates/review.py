def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return check_length(s) and check_first_two(s) and check_numbers_at_end(s)


def check_length(s):
    return 2 <= len(s) <= 6


def check_first_two(s):
    return s[:2].isalpha()


def check_numbers_at_end(s):
    found_number = False

    for i in range(2, len(s)):
        if s[i].isnumeric() and not found_number and s[i] == '0'
            return False