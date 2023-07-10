# numbers = [5, 2, 1, 5, 7, 4]
# numbers.append(20)
# numbers.insert(0, 10)
# numbers.remove(5)
# numbers.clear()
# numbers.pop()
# print(numbers.index(5))
# print(numbers.index(50))
# print(50 in numbers)
# print(numbers.count(5))
# numbers.sort()
# numbers.reverse()
# numbers2 = numbers.copy()
# numbers2.sort()
# print(numbers)
# print(numbers2)

numbers = [5, 2, 1, 5, 7, 4, 3, 1, 3, 5, 6, 8, 2]
uniques = []

for num in numbers:
    found_self = False
    for other_num in numbers:
        if num == other_num and not found_self:
            found_self = True
        elif num == other_num and found_self:
            numbers.remove(other_num)
numbers.sort()
print(numbers)

for number in numbers:
    if number not in uniques:
        uniques.append(number)
uniques.sort()
print(uniques)





