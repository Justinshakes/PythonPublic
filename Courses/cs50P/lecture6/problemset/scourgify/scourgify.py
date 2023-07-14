import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    # Open the input CSV file
    with open(sys.argv[1]) as file:
        # Open the output CSV file
        with open(sys.argv[2], 'w', newline='') as new_file:
            # Specify the fieldnames for the output file
            fieldnames = ["first", "last", "house"]

            # Create a DictWriter object to write to the output file
            writer = csv.DictWriter(new_file, fieldnames=fieldnames)

            # Create a DictReader object to read from the input file
            reader = csv.DictReader(file)

            # Write the header row to the output file
            writer.writeheader()

            # Iterate over each row in the input file
            for row in reader:
                # Write the "name" field to the output file
                last, first = row["name"].split(",")
                writer.writerow({"first": first.strip(), "last": last.strip(), "house": row["house"]})

except FileNotFoundError:
    sys.exit("Could not read " + sys.argv[1])

