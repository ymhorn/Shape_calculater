from Rectangle import Rectangle
import math

class RightTriangle(Rectangle):
    """A right-angled triangle shape"""
    def __init__(self,base,height):
        super().__init__(length = base,width = height)
        self.base = base
        self.height = height
    def get_area(self):
        return super().get_area()/2
    def get_circumference(self):
        return math.sqrt((self.base ** 2) + (self.height ** 2)) + self.base + self.height
