
from rectangle import Rect
from geometric_shape import Geometric_Shape

class Square(Rect):
    name = "square"
    def __init__(self, height, color):
        self.height = height
        self.color = color

    def calculate(self):
        return self.height**2
    
    def __repr__(self):
         return "Share - {}, color - {}, height - {}, area - {}".format(self.name, self.color, self.height, self.calculate())