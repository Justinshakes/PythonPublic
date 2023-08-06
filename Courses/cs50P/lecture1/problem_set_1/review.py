def calculate(expression):
    num1, operator, num2 = expression.split(' ')
    return float(eval(num1 + operator + num2))


def main():
    expression = input("Expression: ")
    result = calculate(expression)
    print(f"{round(result, 1)}")


if __name__ == "__main__":
    main()
