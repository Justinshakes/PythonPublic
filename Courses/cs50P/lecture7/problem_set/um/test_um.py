import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    re.search(r"um[,\.]", s.lower())


...


if __name__ == "__main__":
    main()