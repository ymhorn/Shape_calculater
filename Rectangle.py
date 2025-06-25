from Shape import Shape

class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length=length
        self.width = width
    def get_area(self):
            return self.length * self.width


