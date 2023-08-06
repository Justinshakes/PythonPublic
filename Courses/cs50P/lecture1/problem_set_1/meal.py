def convert(time):
    hours, minutes = time.split(':')
    return float(hours) + float(minutes) / 60


def what_time(time):
    if 7.0 <= time <= 8.0:
        return "Breakfast time"
    elif 12.0 <= time <= 13.0:
        return "Lunch time"
    elif 18.0 <= time <= 19.0:
        return "Dinner time"


def main():
    user_input = input("What time is it? ")
    converted_time = convert(user_input)
    meal_time = what_time(converted_time)
    if meal_time:
        print(meal_time)


if __name__ == "__main__":
    main()
