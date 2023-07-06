"""
14. Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

# Import the datetime module
import datetime


# Define a function that takes two dates as arguments and returns the number of days between them

def main():
    days = days_between_dates(datetime.date(2014, 7, 2), datetime.date(2014, 8, 11))
    print(days)


def days_between_dates(date1, date2):
    # Calculate the number of days between the two dates
    return (date2 - date1).days


# Call the main function
if __name__ == "__main__":
    main()




