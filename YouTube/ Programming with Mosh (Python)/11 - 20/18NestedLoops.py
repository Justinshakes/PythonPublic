# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")



numbers = [2, 2, 2, 2, 5]

# for x_count in numbers:
#     print('x' * x_count)

# for x in range(len(numbers)):
#     for i in range(numbers[x]):
#         print("x", end="")
#     else:
#         print()

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
