import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Enter a name (or press Ctrl-D to finish): ")
        names.append(name)

    except EOFError:
        break

joined_names = p.join(names[:])

print("Adieu, adieu, to " + joined_names)

