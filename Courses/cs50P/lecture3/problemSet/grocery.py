def create_grocery_list():
    grocery_list = {}
    while True:
        try:
            item = input().upper()

            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

        except EOFError:
            return grocery_list


def print_list(grocery_list):
    print("keys: ", grocery_list.keys())
    print("values: ", grocery_list.values())
    print("items: ", grocery_list.items())

    for key in sorted(grocery_list.keys()):
        print(grocery_list[key], key)


def main():
    print("Create your grocery list: ")
    grocery_list = create_grocery_list()
    print_list(grocery_list)


if __name__ == "__main__":
    main()
