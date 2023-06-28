grocery_list = {}  # Create an empty dictionary to store the grocery items and their occurrences

while True:
    try:
        item = input("Item: ").upper()  # Prompt the user to enter an item (convert it to uppercase for consistency)

        if item in grocery_list:  # Check if the item is already present in the grocery list
            grocery_list[item] += 1  # If yes, increment the occurrence count of the item by 1
        else:
            grocery_list[item] = 1  # If not, add the item to the grocery list with an initial count of 1

    except EOFError:
        break  # Exit the loop immediately when Ctrl+D (EOF) is encountered

for item, count in grocery_list.items():  # Iterate over the items and their counts in the grocery list dictionary
    print(f"{count} {item}")  # Print the count and the item in the desired format

print("Grocery list complete.")  # Print a message indicating that the grocery list is complete
