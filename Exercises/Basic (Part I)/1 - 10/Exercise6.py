"""
6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

# Prompt the user to enter a sequence of comma-separated numbers
user_input = input("Enter a sequence of comma-separated numbers: ")

# The input() function retrieves the user's input as a string.

# Use the split() method to split the input string into individual numbers.
# Splitting is done based on the comma (",") separator.
numbers_list = user_input.split(",")

# The split() method returns a list of strings, where each string represents a number.

# Convert the list of strings to a tuple
numbers_tuple = tuple(numbers_list)

# The tuple() function is used to convert the list to a tuple.

# Print the list and tuple of numbers
print("List:", numbers_list)
print("Tuple:", numbers_tuple)

