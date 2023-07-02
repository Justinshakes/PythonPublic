import inflect

# Create an instance of the inflect engine
p = inflect.engine()

# Create an empty list to store names
names = []

# Start an infinite loop to continuously prompt for names
while True:
    try:
        # Prompt the user to enter a name, or press Ctrl-D (EOF) to finish
        name = input("Enter a name (or press Ctrl-D to finish): ")

        # Append the entered name to the names list
        names.append(name)
    except EOFError:
        # If the user presses Ctrl-D (EOF), break out of the loop
        break

# Get the length of the names list
length = len(names)

# Join the names using the inflect engine's join method
joined_names = p.join(names[:])

# Print the farewell message with the joined names
print("Adieu, adieu, to " + joined_names)
