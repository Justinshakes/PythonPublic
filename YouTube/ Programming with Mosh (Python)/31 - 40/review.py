class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


p1 = Point()

p1.x = 10

print(p1.x)

p1.draw()