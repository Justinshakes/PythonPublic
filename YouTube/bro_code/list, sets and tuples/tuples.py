#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("apple", "orange", "banana", "coconut", "coconut")


# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))

# print("apple" in fruits)

# print(fruits.index("apple"))
print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit)
