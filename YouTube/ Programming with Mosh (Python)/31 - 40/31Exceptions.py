while True:
    try:
        age = int(input('Age: '))
        income = 20000
        risk = income / age
        break
    except ZeroDivisionError:
        print("Age cannot be 0.")
    except ValueError:
        print("Integers only")

print("Your age is", age)
