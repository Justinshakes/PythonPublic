# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("Move")
#
#     def draw(self):
#         print("Draw")
#
#
# point = Point(10, 20)
# point.x = 11
# print(point.x)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, I am {self.name}")


p1 = Person("Justin")

print(p1.name)
p1.talk()

p2 = Person("Bob")

p2.talk()

