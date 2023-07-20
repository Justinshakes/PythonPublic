import re


def main():
    # Get user input for time and call the convert function to process it
    print(convert(input("Enter time in the format 'HH:MM AM/PM to HH:MM AM/PM': ")))


def convert(s):
    # Check if the input matches the correct format using regular expression
    if correct_format := re.search(
            r"^(([0-2]*[0-9]):*([0-5][0-9])*) ([A|P]M) to (([0-2]*[0-9]):*([0-5][0-9])*) ([A|P]M)$", s
            ):

        # Extract groups from the regex match
        groups = correct_format.groups()

        # Check if the hour parts are greater than 12, which would be an invalid input
        if int(groups[1]) > 12 or int(groups[5]) > 12:
            raise ValueError("Invalid time format. Hours should be in 12-hour format.")

        # Convert both times to 24-hour format
        updated_1st_time = twentyfour_hour_format(groups[1], groups[2], groups[3])
        updated_2nd_time = twentyfour_hour_format(groups[5], groups[6], groups[7])

        return f"{updated_1st_time} to {updated_2nd_time}"
    else:
        # If the input doesn't match the correct format, raise a ValueError
        raise ValueError("Invalid time format. Please enter time in the format 'HH:MM AM/PM to HH:MM AM/PM'")


def twentyfour_hour_format(hour, minute, am_or_pm):
    # Convert 12-hour format time to 24-hour format
    if am_or_pm == "PM":
        if int(hour) == 12:
            updated_hour = 12
        else:
            updated_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            updated_hour = 0
        else:
            updated_hour = int(hour)

    # If minute is None, set it to '00', otherwise, include the given minute
    if minute is None:
        updated_minute = "00"
    else:
        updated_minute = minute

    # Create the updated time format in the format 'HH:MM'
    updated_format = f"{updated_hour:02}:{updated_minute}"
    return updated_format


# Call the main function if the script is run directly
if __name__ == "__main__":
    main()
