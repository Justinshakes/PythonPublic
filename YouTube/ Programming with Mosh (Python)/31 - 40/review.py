class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello my name is {self.name}")


p1 = Person("Justin")

p1.talk()

print(p1.name)