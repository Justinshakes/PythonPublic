grocery_list = {}

while True:
    try:
        item = input().upper()

        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    except EOFError:
        break

sorted_list = sorted(grocery_list.items(), key=lambda x: x[0])

for item, count in sorted_list:
    print(f"{count} {item}")

