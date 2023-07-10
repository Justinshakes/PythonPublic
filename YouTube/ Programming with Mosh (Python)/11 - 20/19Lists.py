# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[0] = 'Jon'
# print(names[2:])
# print(names)

list = [1, 6, 3, 9, 15, 6, 4, 8, 3]

# list.sort(reverse=True)
# print(list[0])

max = list[0]

for num in list[1:]:
    if num > max:
        max = num

print(f"Largest Number: {max}")
