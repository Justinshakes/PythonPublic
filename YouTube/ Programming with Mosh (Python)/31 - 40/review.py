class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, I am {self.name}")


p1 = Person("Justin")

print(p1.name)

p1.talk()