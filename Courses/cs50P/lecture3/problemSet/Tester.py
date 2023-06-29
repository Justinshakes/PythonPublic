# Month names
months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]

while True:
    try:
        date_input = input("Enter a date (MM/DD/YYYY or Month Day, Year): ")

        if "/" in date_input:
            month, day, year = map(int, date_input.split("/"))
        else:
            month_name, day, year = date_input.split()

            day = day[:-1]

            month = months.index(month_name) + 1

            day = int(day)
            month = int(month)
            year = int(year)

        if 1 <= month <= 12 and 1 <= day <= 31:
            date_output = f"{year:0d}-{month:02d}-{day:02d}"

            print(date_output)
            break
        else:
            print("Invalid date. Please enter a valid date.")


    except ValueError:
        print("Invalid input. Please enter the date in the specified format.")
