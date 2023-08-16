# Review Time Baby Yup Clock
def get_date_input():
    return input("Enter a date (MM/DD/YYYY or Month Day, Year): ")


def parse_date_input(date_input):
    months = (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    )
    if "/" in date_input:
        return map(int, date_input.split("/"))
    else:
        month_name, day, year = date_input.split()
        day = day.replace(",", "")
        month = months.index(month_name) + 1
        return int(day), int(month), int(year)


def validate_date(month, day):
    return 1 <= month <= 12 and 1 <= day <= 31


def format_date(year, month, day):
    return f"{year:04d}-{month:02d}-{day:02d}"


def main():
    while True:
        try:
            date_input = get_date_input()
            day, month, year = parse_date_input(date_input)

            if validate_date(month, day):
                date_output = format_date(year, month, day)
                print(date_output)
                break
            else:
                print("Invalid date. Please enter a valid date.")
        except ValueError:
            print("Invalid input. Please enter the date in the specified format. ")


if __name__ == "__main__":
    main()
