import re


def main():
    # Get user input for time and call the convert function to process it
    print(convert(input("Hours: ")))


def convert(s):
    # Check if the input matches the correct format using regular expression
    if correct_format := re.search(
            r"^(([0-2]*[0-9]):*([0-5][0-9])*) ([A|P]M) to (([0-2]*[0-9]):*([0-5][0-9])*) ([A|P]M)$", s):

        return None
    else:
        # If the input doesn't match the correct format, raise a ValueError
        raise ValueError


# Call the main function if the script is run directly
if __name__ == "__main__":
    main()
