def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")

# Positional Arugments
# greet_user("John", "Smith")

# Keyword Arguments
greet_user(last_name="Smith", first_name="John")

# calc_cost(50, 5, 0.1)
# calc_cost(total=50, shipping=5, discount=0.1)

print("Finish")

# main()