import re

name = input("What's your name? ").strip()

print(name)

if matches := re.search(r"^(.+), +(.+)$", name):
    name = f"{matches.group(2)} {matches.group(1)}"

print(f"hello, {name}")













# if "," in name:  # ? zero or on thing to the left _?
#     last, first = name.split(", ?")
#     name = f"{first} {last}"
# print(f"hello, {name}")

