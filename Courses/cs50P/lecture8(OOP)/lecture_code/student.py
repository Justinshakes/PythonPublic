class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house  # Initialize the house attribute using the setter method

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")  # Get the student's name from user input
        house = input("House: ")  # Get the student's house from user input
        return cls(name, house)  # Create a new Student object and return it


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
