def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    dollars = dollars.removeprefix('$')
    dollars = dollars.removesuffix('$')
    return float(dollars)


def percent_to_float(percent):
    percent = percent.removeprefix('%')
    percent = percent.removesuffix('%')
    return float(percent) / 100


if __name__ == "__main__":
    main()
