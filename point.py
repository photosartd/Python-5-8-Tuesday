#Класс точки
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Point: x: " + str(self.x) + " y: " + str(self.y)
    def __add__(self, other):
        return Point(x=self.x + other.x, y=self.y + other.y)

point1 = Point(y=1,x=2)
print(str(point1))
point2 = Point(1,2)
point3 = point1 + point2
print(str(point3))