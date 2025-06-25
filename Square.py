from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(length = side, width = side)
        self.side = side

if __name__ == "__main__":
    c = Square(10)
    print(c.get_area())
