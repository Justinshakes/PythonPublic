import csv

name = input("What's your name? ").strip()
home = input("Where's your home? ").strip()

with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})


