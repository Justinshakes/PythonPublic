def get_change(amount_due):
    valid_coins = (5, 10, 25)
    while True:
        coin = int(input("Insert Coin: "))
        if coin in valid_coins:
            return coin
        else:
            print("Amount Due:", amount_due)


def main():
    amount_due = 50
    while amount_due > 0:
        print("Amount Due:", amount_due)
        amount_due -= get_change(amount_due)
    print("Change Owed:", abs(amount_due))


if __name__ == "__main__":
    main()
