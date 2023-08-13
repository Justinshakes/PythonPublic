def menu(item):
    menu_items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    return menu_items.get(item, 0)


def order_food():
    total = 0.00
    print("Ctrl+D to stop ordering")
    while True:
        try:
            item = input("Item: ")
            item_cost = menu((item.title()))
            if item_cost == 0:
                print(f"'{item}' is not on the menu")
            total += item_cost
            print(f"Total: ${total:.2f}")
        except EOFError:
            return total


def main():
    total = order_food()
    print(f"Grand total: ${total:.2f}")


if __name__ == "__main__":
    main()
