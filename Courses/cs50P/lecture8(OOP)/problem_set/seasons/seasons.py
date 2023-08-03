from datetime import date

# def english_conversion():




def main():
    # date_of_birth_input = input("Input date of birth YYYY-MM-DD: ")
    date_of_birth_input = "1998-11-04"
    year, month, day = map(int, date_of_birth_input.split("-"))
    date_of_birth = date(year, month, day)

    print("Current date:", date.today())
    print("Date of birth:", date_of_birth)

    time_difference = date.today() - date_of_birth

    print("Time difference:", int(time_difference.days) * 60, "minutes")




if __name__ == "__main__":
    main()
