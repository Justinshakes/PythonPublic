import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if correct_format := re.search(
            r"^(([0-2]*[0-9]):*([0-5][0-9])*) ([A|P]M) to (([0-2]*[0-9]):*([0-5][0-9])*) ([A|P]M)$", s):

    else:
        raise ValueError


...

if __name__ == "__main__":
    main()
