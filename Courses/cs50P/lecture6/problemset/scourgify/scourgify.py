import csv

import csv

# Open the input CSV file
with open("before.csv") as file:
    # Open the output CSV file
    with open("after.csv", 'w', newline='') as new_file:
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
            first, last = row["name"].split(",")
            # print("first:" + first + "  Last: ")
            # writer.writerow({"first name": first_name, "last name": last_name, "house": row["house"]})
            writer.writerow({"first": first, "last": last, "house": " " + row["house"]})

# Print houses
# import csv
#
# with open("old.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         house = row["house"]
#         print(house)

# Print whole row
# with open("old.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)
