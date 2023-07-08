def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    fuel_left = gauge(percentage)
    print(fuel_left)


def convert(fraction):
    while True:
        try:
            x, y = map(int, fraction.split("/"))
            result = x / y
            if 0 <= result <= 1:
                return int(round(result * 100))
            elif x > y:
                raise ValueError
            else:
                fraction = input("Fraction: ")
                continue
        except (NameError, ZeroDivisionError, SyntaxError, ValueError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
