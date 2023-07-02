# 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

# Import the datetime module to work with dates and times
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Print a message indicating the current date and time
print ("Current date and time : ")

# Format the date and time to a specific string format ("%Y-%m-%d %H:%M:%S")
# and print it
print(now.strftime("%Y-%m-%d %H:%M:%S"))
