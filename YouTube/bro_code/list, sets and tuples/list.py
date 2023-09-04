#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut"]

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))

# print("apple" in fruits)

# fruits[0] = "pineapple"
# for fruit in fruits:
#     print(fruit)

# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.index("pineapple"))

print(fruits.count("banana"))
print(fruits.count("pineapple"))

print(fruits)
# print(fruits[1])
# print(fruits[::2])
# print(fruits[:2])
# print(fruits[::-1])
