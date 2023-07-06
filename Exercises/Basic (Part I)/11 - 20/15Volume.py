"""
15. Write a Python program to get the volume of a sphere with radius six.
"""

# Import the math module
import math


# Define a function that takes the radius of a sphere as an argument and returns the volume of the sphere
def main():
    volume = sphere_volume(6)
    print(volume)


def sphere_volume(radius):
    # Calculate the volume of the sphere
    return (4 / 3) * math.pi * radius ** 3


# Call the main function
if __name__ == "__main__":
    main()