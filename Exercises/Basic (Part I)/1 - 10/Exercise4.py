# 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
import math

# Import the math module to access mathematical functions and constants


# Prompt the user to enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle using the formula: area = pi * radius^2
area = math.pi * radius ** 2

# Print the calculated area of the circle
print("Area = ", area)

