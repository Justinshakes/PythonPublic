import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1]) as file:
        with open(sys.agrv[2], 'w', newline='') as new_file:
            fieldnames = ['first', 'last', 'house']

            writer = csv.DictWriter(new_file, fieldnames=fieldnames)

            reader = csv.DictReader(file)

            writer.writeheader()

            for row in reader:
                last, first = row['name'].split(",")
                writer.writerow({'first': first.strip(),
                                 'last': last.strip(),
                                 'house': row['house']})



except FileNotFoundError:
    sys.exit("Could not read " + sys.argv[1])
