from geometric_shape import Geometric_Shape

class Rect(Geometric_Shape):
    name = "rectangle"
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
    
    def calculate(self):
        return self.height * self.width
    def __repr__(self):
        return "Shape - {}, color - {}, height - {}, width - {}, area - {}".format(self.name, self.color, self.height, self.width, self.calculate())
