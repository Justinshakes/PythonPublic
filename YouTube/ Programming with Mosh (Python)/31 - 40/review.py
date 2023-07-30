class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, I am {self.name}")


p1 = Person("Justin")
p2 = Person("Calen")

p1.talk()

p2.talk()

p1.x = 3
print(p1.x)