import random

while True:
    try:
        level = int(input("Level: "))
        if 1 <= level <= 100:
            break
        # Your code here that might raise exceptions
    except Exception as e:
        print("An exception occurred:", e)

random_num = random.randint(1, level)

while True:
    try:
        Guess = int(input("Guess: "))
        if Guess == random_num:
            print("Just right!")
            break
        elif Guess > random_num:
            print("Too large!")
        elif Guess < random_num:
            print("Too small!")
    except Exception as e:
        print("An exception occurred:", e)
