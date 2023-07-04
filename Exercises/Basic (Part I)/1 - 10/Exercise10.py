"""
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

# Prompt the user to enter an integer
n = int(input("Enter an integer: "))

# Calculate the value of n+nn+nnn
result = n + n*11 + n*111

# Print the result
print(result)
