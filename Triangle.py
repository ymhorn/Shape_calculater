from Rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self,base,height):
        super().__init__(length = base,width = height)
        self.base = base
        self.height = height
    def get_area(self):
        return super().get_area()/2
if __name__=="__main__":
    d = Triangle(10,15)
    print(d.get_area())