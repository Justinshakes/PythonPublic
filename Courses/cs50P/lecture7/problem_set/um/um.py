import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.search(r"(um)", s.lower())
    print(matches.groups())
    return "Success"


if __name__ == "__main__":
    main()