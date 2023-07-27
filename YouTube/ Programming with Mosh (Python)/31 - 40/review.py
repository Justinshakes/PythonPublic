#  Review Again Again
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def meow(self):
        print("Meow")


d1 = Dog()

c1 = Cat()

d1.bark()
d1.walk()

c1.meow()
c1.walk()
