grocery_list = {}  # Create an empty dictionary to store the grocery items and their occurrences

while True:
    try:
        item = input().upper()  # Prompt the user to enter an item and convert it to uppercase

        if item in grocery_list:  # Check if the item is already present in the grocery list
            grocery_list[item] += 1  # If yes, increment the occurrence count of the item by 1
        else:
            grocery_list[item] = 1  # If not, add the item to the grocery list with an initial count of 1

    except EOFError:
        break  # Exit the loop immediately when Ctrl+D (EOF) is encountered

# Sort the grocery list dictionary alphabetically by item
sorted_list = sorted(grocery_list.items(), key=lambda x: x[0])

for item, count in sorted_list:  # Iterate over the sorted items and their counts
    print(f"{count} {item}")  # Print the count and the item in the desired format

"""
    item: This variable holds the value of the item (key) from the sorted list. It represents the name of the grocery item.

count: This variable holds the value of the count (value) associated with the item from the sorted list. It represents the number of occurrences of the grocery item.
"""