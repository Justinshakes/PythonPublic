def convert(time):
    hours, minutes = time.split(':')
    return round(float(hours) + float(minutes) / 60, 2)


def what_time(time):
    if 7 <= time <= 8:
        return "Breakfast time"
    elif 12 <= time <= 13:
        return "Lunch time"
    elif 18 <= time <= 19:
        return "Dinner time"
    else:
        return ""


def main():
    user_input = input("What time is it in 24 hour format: ")
    converted_time = convert(user_input)
    meal_time = what_time(converted_time)


if __name__ == "__main__":
    main()
