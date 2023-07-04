import random


def main():
    # Get the level from the user
    level = get_level()
    score = 0
    counter = 0

    while counter < 10:
        errors_counter = 0
        # Generate two random integers based on the level
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        while True:
            try:
                if errors_counter == 3:
                    # If user has made 3 errors, reveal the correct answer
                    print(f"{x} + {y} = {answer}")
                    counter += 1
                    break

                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == answer:
                    # If user's answer is correct, increment score and counter
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

    print("Score:", score)


def get_level():
    # Prompt the user for the level and validate input
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    # Generate a random integer based on the level
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
