def convert(mass):
    c = 300000000
    return int(mass) * (c ** 2)


def main():
    energy = convert(input("Mass in Kg's: "))

    print(energy)


if __name__ == "__main__":
    main()
