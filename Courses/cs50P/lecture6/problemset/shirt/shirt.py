import sys


def main():
    check_command_line_arg()


def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    print(sys.argv)


if __name__ == "__main__":
    main()
