import math
from abc import ABC, abstractmethod

def area_bad(shape):
    if shape["type"] == "circle":
        return math.pi * shape["radius"] ** 2
    if shape["type"] == "square":
        return shape["side"] ** 2


circle = {"type": "circle", "radius": 5}
square = {"type": "square", "side": 4}



print(area_bad(circle))
print(area_bad(square))

class Shape(ABC):
    @abstractmethod
    def area(self):
        """ TODO """


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base,height):
        self.base = base
        self.height = height


    def area(self):
        return 0.5 * self.base * self.height



print(Triangle(10,5).area())