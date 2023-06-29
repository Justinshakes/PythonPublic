def main():
    fraction = get_fracdtion()
    percentage = get_percentage(fraction)
    remaining_fuel(percentage)


def get_fraction():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = map(int, fraction.split("/"))
            result = round(eval(fraction), 2)
            if 0 <= result <= 1:
                return result
        except (NameError, ZeroDivisionError, SyntaxError, ValueError):
            pass


def get_percentage(fraction):
    return round(float(fraction) * 100)


def remaining_fuel(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%", end="")


main()