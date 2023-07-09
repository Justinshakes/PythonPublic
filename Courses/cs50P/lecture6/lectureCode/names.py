names = []

# with open("names.txt") as file:
#     for line in sorted(file):
#         names.append(line.rstrip())
#
# for name in names:
#     print(f"Hello, {name}")


with open("names.csv") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"Hello, {name}")












# with open("names.txt", "r") as file:
#     for line in file:
#         print("Hello,", line.rstrip())


# with open("names.txt", "r") as file:
#     lines = file.readlines()
#
# for line in lines:
#     print("hello,", line.rsplit())

# name = input("What's you name? ")
#
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
