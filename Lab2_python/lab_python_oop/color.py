from geometric_shape import Geometric_Shape

class Color(Geometric_Shape):
    def __init__(self, color):
        self.color = color

    def calculate(self):
        return self.color