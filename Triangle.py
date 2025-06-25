from Rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self,base,height):
        super().__init__(length = base,width = height)
        self.base = base
        self.height = height
    def get_area(self):
        return super().get_area()/2
