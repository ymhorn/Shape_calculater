from Shape import Shape

class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length=length
        self.width = width
    def get_area(self):
        return self.length * self.width
    def get_circumference(self):
        return (self.length * 2) + (self.width * 2)


