import csv
import sys
from tabulate import tabulate

if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
    sys.exit("Invalid argument, must be a single .csv file")

with open(sys.argv[1]) as file:
    lines = file.readlines()
    reader = csv.reader(lines)

print(tabulate(reader, headers="firstrow", tablefmt="grid"))