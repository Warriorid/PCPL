#виртульное окружение
"""source .venv/bin/activate"""


import sys
sys.path.append('Lab2_python/lab_python_oop') 
from lab_python_oop.square import Square
from lab_python_oop.rectangle import Rect
from lab_python_oop.circle import Circle

square = Square(7, "red")
circle = Circle(7, "blue")
rectangle = Rect(7, 5, "green")
print(square)
print(circle)
print(rectangle)


