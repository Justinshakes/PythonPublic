from tabulate import tabulate

# table_data = [['Name', 'Age', 'Job'],
#          ['John', 24, 'Programmer'],
#          ['Jack', 28, 'Musician'],
#          ['Jill', 22, 'Artist'],
#          ['Jess', 32, 'Doctor'],
#          ['Jenny', 31, 'Lawyer']]

data = {
    'Name': ['John', 'Jack', 'Jill', 'Jess', 'Jenny'],
    'Age': [24, 28, 22, 32, 31],
    'Job': ['Programmer', 'Musician', 'Artist', 'Doctor', 'Lawyer']
}

print(tabulate(data, headers="keys", tablefmt="grid"))


# print(table_data)

# for row in table_data:
#     for col in row:
#         print(col, end='\t')
#     print()

# https://pypi.org/project/tabulate/

print(tabulate(table_data, headers="firstrow",
               tablefmt="grid"))

# with open('table.html', 'w') as f:
#     f.write(tabulate(table_data, headers="firstrow",
#                      tablefmt="html"))
