from Shape import Shape

class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length=length
        self.width = width
    def get_area(self):
            return self.length * self.width
if __name__=="__main__":
    b = Rectangle(10,15)
    print(b.get_area())
    print(str(b))
