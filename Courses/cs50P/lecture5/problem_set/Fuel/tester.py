def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    gauge(percentage)


def convert(fraction):
    while True:
        try:
            result = round(eval(fraction), 2)
            if 0 <= result <= 1:
                return int(round(result * 100))
            else:
                fraction = input("Fraction: ")
                continue
        except (NameError, ZeroDivisionError, SyntaxError, ValueError):
            raise


def gauge(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%", end="")


if __name__ == "__main__":
    main()
