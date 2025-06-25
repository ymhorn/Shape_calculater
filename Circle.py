from Shape import Shape
import math

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    def get_area(self):
        return math.pi * self.radius ** 2

if __name__ == "__main__":
    e = Circle(5)
    print(e.get_area())