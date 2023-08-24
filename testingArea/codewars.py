def say_hello(name, city, state):
    formatted_name = ' '.join(name)
    return f"Hello, {formatted_name}! Welcome to {city}, {state}!"

def main():
    result = say_hello(["John", "Smith"], "Phoenix", "Arizona")
    result2 = say_hello(["Wallace", "Russel", "Osbourne"], "Albany", "New York")

    print(result)
    print(result2)

    result3 = say_hello(["Former", "President", "Walker"], "Los Angeles", "California")
    result4 = say_hello(["Former", "President", "Garrett", "Walker"], "Los Angeles", "California")

    print(result3)
    print(result4)

main()
