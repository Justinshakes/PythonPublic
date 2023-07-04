"""
12. Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
"""
import calendar


# Define a function that takes a month and year as arguments and prints the calendar for that month and year
def print_calendar(month, year):
    print(calendar.month(year, month))


# Call the function
print_calendar(12, 2020)
print_calendar(1, 2021)
print_calendar(2, 2021)
