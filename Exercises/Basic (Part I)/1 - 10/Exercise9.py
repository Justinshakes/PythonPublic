"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""

# Define the exam start date as a tuple (day, month, year)
exam_st_date = (11, 12, 2014)

# Display the examination schedule using f-string formatting
print(f"The examination will start from: {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}")
