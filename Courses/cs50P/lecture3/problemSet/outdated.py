# Month names
months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]

while True:
    try:
        # Prompt the user to enter a date in MM/DD/YYYY or Month Day, Year format
        date_input = input("Enter a date (MM/DD/YYYY or Month Day, Year): ")

        # Check if the input matches MM/DD/YYYY format
        if "/" in date_input:
            # Split the input by "/" and convert the parts to integers
            month, day, year = map(int, date_input.split("/"))
        else:
            # Split the input by spaces into month name, day, and year
            month_name, day, year = date_input.split()

            # Remove the comma from the day
            day = day[:-1]

            # Find the corresponding month index in the month names list
            month = months.index(month_name) + 1

            # Convert day, month, and year to integers
            day = int(day)
            month = int(month)
            year = int(year)

        # Validate the date by checking if the month is between 1 and 12 and the day is between 1 and 31
        if 1 <= month <= 12 and 1 <= day <= 31:
            # Format the date in YYYY-MM-DD format using leading zeros
            date_output = f"{year:04d}-{month:02d}-{day:02d}"
            # Print the formatted date
            print(date_output)
            # Exit the loop
            break
        else:
            # Display an error message for an invalid date
            print("Invalid date. Please enter a valid date.")

    except ValueError:
        # Display an error message for invalid input
        print("Invalid input. Please enter the date in the specified format.")
