"""
5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
"""

# Prompt the user to enter their first and last name, separated by a space
first_name, last_name = input("Enter your first and last name: ").split()

# The input() function retrieves the user's input as a string.
# The split() method splits the input string into separate words based on whitespace.

# Assign the first name to the variable first_name and the last name to the variable last_name.

# Print the last name followed by the first name
print(last_name, first_name)

