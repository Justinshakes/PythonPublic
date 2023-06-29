# Menu dictionary with menu items as keys and their prices as values
Menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0.00

while True:
    try:
        order = input("Item: ").title()  # Prompt the user to enter the menu item they want to order
        # Check if the entered item exists in the menu
        if order in Menu:
            total += Menu[order] # Add the price of the ordered item to the total
            print("Total: $" + format(total, ".2f")) # Print total with 2 decimal places
        else:
            print("Invalid item. Please choose a valid item from the menu.")  # Inform the user about an invalid item
    except EOFError:
        break  # Exit the loop immediately when Ctrl+D (EOF) is encountered

print("Program closed.")

