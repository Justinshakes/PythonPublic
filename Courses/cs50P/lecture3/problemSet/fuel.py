#  Will go over one more time
def get_fraction():
    print("Ex: 3/4")
    while True:
        fraction = input("Fraction: ")
        try:
            result = round(eval(fraction), 2)
            if 0 <= result <= 1:
                return result
        except (NameError, ZeroDivisionError, SyntaxError, ValueError):
            print("Invalid input")
            pass


def get_percentage(fraction):
    return round(float(fraction) * 100)


def fuel_gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    fraction = get_fraction()
    percentage = get_percentage(fraction)
    fuel_percentage = fuel_gauge(percentage)
    print(fuel_percentage)


if __name__ == "__main__":
    main()
