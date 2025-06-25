
class Shape:
    def get_area(self):
        pass
    def __str__(self):
        return f"The shape is a {self.__class__.__name__}"
    def __add__(self, other):
        return self.get_area() + other.get_area()
    def __len__(self):
        return self.length
    def __sub__(self, other):
        if self.get_area() > other.get_area():
            return self.get_area() - other.get_area()
        else:
            return other.get_area() - self.get_area()
    def __round__(self):
        if self.__class__.__name__ == "Circle":
            return True
        else:
            return False
