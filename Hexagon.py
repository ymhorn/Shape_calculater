from Square import Square
import math

class Hexagon(Square):
    def __init__(self,side):
        super().__init__(side)
    def get_area(self):
        return ((3 * math.sqrt(3)) / 2) * (self.side ** 2)
    def get_circumference(self):
        return self.side * 6