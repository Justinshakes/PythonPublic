def find_multiples(integer, limit):
    multiples = []
    tracker = integer

    while tracker <= limit:
        multiples.append(tracker)
        tracker += integer

    return multiples


def main():
    multiples = find_multiples(2, 6)
    print(multiples)


main()
