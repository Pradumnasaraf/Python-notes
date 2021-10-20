class Point:
    def move(self):
        print("move")

    def dwaw(self):
        print("Draw")

point1 = Point()
point1.x = 10
point1.y = 20

print(point1.x)
point1.dwaw()
point1.move()