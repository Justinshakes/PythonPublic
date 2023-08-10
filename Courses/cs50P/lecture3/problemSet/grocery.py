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


def main():
    grocery_list = create_grocery_list()

    # print(grocery.keys())
    # print(grocery.values())
    # print(grocery.items())

    for key in sorted(grocery_list.keys()):
        print(grocery_list[key], key)


if __name__ == "__main__":
    main()
