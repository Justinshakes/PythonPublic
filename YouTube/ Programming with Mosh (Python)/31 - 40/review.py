class Point:

    def __init__(self, name):
        self.name = name
    def move(self):
        print(f"{self.name} Moved")

    def draw(self):
        print(f"{self.name} drawn")


point1 = Point("p1")
point1.move()
point1.draw()
point1.fdsakl = 10
point1.XDLMAO = 20


print(point1.XDLMAO)
print(point1.fdsakl)

point2 = Point("p2")
point2.move()
point2.draw()
