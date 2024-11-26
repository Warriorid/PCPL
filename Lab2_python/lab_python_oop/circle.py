from geometric_shape import Geometric_Shape
import math

class Circle(Geometric_Shape):
    name = "circle"
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def calculate(self):
         return math.pi * self.radius**2

    def __repr__(self):
        return "Shape - {}, radius - {}, color - {}, area - {}".format(self.name, self.radius, self.color, self.calculate())