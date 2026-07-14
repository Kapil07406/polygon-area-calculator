# Polygon Area Calculator

class Polygon:

    def area(self):
        pass

class Rectangle(Polygon):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Polygon):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

rect = Rectangle(10, 5)
tri = Triangle(8, 6)

print("Rectangle Area:", rect.area())
print("Triangle Area:", tri.area())