def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} form {student[1]}")
    

def get_student():
    name = input("Name: ").strip()
    house = input("House: ").strip()
    return [name, house]


if __name__ == "__main__":
    main()






