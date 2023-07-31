class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house  # Initialize the house attribute using the setter method

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house  # The getter method for the house attribute

    @house.setter
    def house(self, house):
        valid_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "farm"]
        if house not in valid_houses:
            raise ValueError(f"{house} is an invalid house")
        self._house = house  # The private attribute `_house` holds the actual value of the house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")  # Get the student's name from user input
    house = input("House: ")  # Get the student's house from user input
    return Student(name, house)  # Create a new Student object and return it


if __name__ == "__main__":
    main()
