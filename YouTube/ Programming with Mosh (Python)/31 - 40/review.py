
class Mammal:

    def __init__(self, name):
        self.name = name
    def walk(self):
        print(f"{self.name} is walking")


class Dog(Mammal):
    def bark(self):
        print("Bark")

    # def walk(self):
    #     print("Dog walk")


class Cat(Mammal):
    def meow(self):
        print("Meow")

    # def walk(self):
    #     print("Cat walk")


m1 = Mammal("Humman")
m1.walk()

d1 = Dog("Rex")
c1 = Cat("Tiggs")

d1.bark()
d1.walk()

c1.meow()
c1.walk()


