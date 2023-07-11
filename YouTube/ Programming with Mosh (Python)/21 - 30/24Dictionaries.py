# Name: John Smith
# Email: john@gmail.com
# Phone: 1234

# customer = {
#     "name": "John Smith",
#     "age":  30,
#     "is_verified": True
# }
#
# customer["name"] = "Jack Smith"
# print(customer["name"])
# customer["birthdate"] = "Jan 1 1980" # adding new key value pairs
# print(customer["birthdate"])
# print(customer.get("Birthdate", "Jan 1 1980"))
# print(customer.get("Birthdate", "Jan 1 1980"))


digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

# user_input = input("Phone: ")
#
# for ch in user_input:
#     print(digits_mapping.get(ch), end=" ")

user_input = input("Phone: ")
output = ""
for ch in user_input:
    output += digits_mapping.get(ch, "!") + " "
print(output)
