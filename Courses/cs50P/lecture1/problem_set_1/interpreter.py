def calculate(num1, operator, num2):
    return float(eval(num1 + operator + num2))


def main():
    try:
        num1, operator, num2 = input("Expression (e.g., 5 + 3): ").split()
        result = calculate(num1, operator, num2)
        print(round(result, 1))
    except ValueError:
        print("Invalid input. Please provide an expression like '5 + 3'.")


if __name__ == "__main__":
    main()
