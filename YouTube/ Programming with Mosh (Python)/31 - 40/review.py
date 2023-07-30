class Mammal:

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")


class Dog(Mammal):
    def bark(self):
        print(f"{self.name} is Barking")


class Cat(Mammal):
    def meow(self):
        print(f"{self.name} is Meowing")


Mammal = Mammal("Human")

dog1 = Dog("Doggo")

cat1 = Cat("Kitty Cat")

Mammal.walk()
dog1.walk()
cat1.walk()

dog1.bark()
cat1.meow()