
class Shape:
    def get_area(self):
        pass
    def __str__(self):
        return f"The shape is a {self.__class__.__name__}"
    def __add__(self, other):
        return self.get_area() + other.get_area()


