import random

def main():
    level = get_level()
    score = 0
    counter = 0

    while counter < 10:
        errors_counter = 0
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        while True:
            try:
                if errors_counter == 3:
                    print(f"{x} + {y} = {answer}")
                    counter += 1
                    break

                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == answer:
                    score += 1
                    counter += 1
                    break
                else:
                    print("EEE")
                    errors_counter += 1
                    continue
            except ValueError as e:
                print("EEE")
                errors_counter += 1
                continue
    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Invalid level")

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()