from Square import Square
import math

class Hexagon(Square):
    def __init__(self,side):
        super().__init__(side)
    def get_area(self):
        return ((3 * math.sqrt(3)) / 2) * (self.side ** 2)

if __name__ == "__main__":
    f = Hexagon(5)
    print(f.get_area())
    print(str(f))