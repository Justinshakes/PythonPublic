# https://www.youtube.com/watch?v=Smf68icE_as

# Reads a CSV file using csv.reader

import csv
import sys
from tabulate import tabulate

if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
    sys.exit("Invalid argument, must be a single .csv file")

with open(sys.argv[1]) as file:
    lines = file.readlines()
    reader = csv.reader(lines)

print(tabulate(reader, headers="firstrow",
               tablefmt="grid"))

"""
Pizza 2.0 ?
import csv
import sys
from tabulate import tabulate

# Check if the correct command-line argument is provided
if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
    sys.exit("Invalid argument. Please provide a single .csv file.")

# Open the CSV file and read its contents
with open(sys.argv[1], newline="") as file:
    reader = csv.reader(file)
    data = list(reader)

# Check if the CSV file is empty
if not data:
    sys.exit("The CSV file is empty.")

# Print the CSV data in a tabular format
headers = data[0]
table_data = data[1:]
print(tabulate(table_data, headers=headers, tablefmt="grid"))

"""