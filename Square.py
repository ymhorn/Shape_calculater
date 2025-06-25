from Rectangle import Rectangle

class Square(Rectangle):
    """A square shape"""
    def __init__(self, side):
        super().__init__(length = side, width = side)
        self.side = side

