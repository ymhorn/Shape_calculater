from Shape import Shape
import math

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    def get_area(self):
        return math.pi * self.radius ** 2
