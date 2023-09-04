def remove_every_other(my_list):
    # Initialize an empty list to store the selected elements
    selected_elements = []

    # Iterate over the indices of elements in my_list
    for index in range(len(my_list)):
        # Check if the index is even (every other element)
        if index % 2 == 0:
            # Append the element at the current index to selected_elements
            selected_elements.append(my_list[index])

    # Return the list of selected elements
    return selected_elements


def main():
    result1 = remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # [1, 3, 5, 7, 9])
    result2 = remove_every_other(["Hello", "Goodbye", "Hello Again"])
    #  ['Hello', 'Hello Again'])
    print(result1)
    print(result2)


if __name__ == "__main__":
    main()
