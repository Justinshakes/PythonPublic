def combat(health, damage):
    remaining_health = max(health - damage, 0)
    return remaining_health


def main():
    result1 = combat(100, 5)
    result2 = combat(20, 30)
    print(result1)
    print(result2)


main()
