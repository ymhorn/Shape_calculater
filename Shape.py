from abc import ABC, abstractmethod

class Shape(ABC):
    """ A base class for all shapes"""
    def get_area(self):
        """Returns the area of the shape"""
        pass
    def get_circumference(self):
        """Returns the circumference of the shape"""
        pass
    def __str__(self):
        """Returns the type of shape"""
        return f"The shape is a {self.__class__.__name__}"
    def __add__(self, other):
        """Adds the area of 2 shapes together"""
        return self.get_area() + other.get_area()
    def __len__(self):
        """Returns the length of a side or across the shape"""
        return self.length
    def __sub__(self, other):
        """Returns the difference in area between 2 shapes"""
        if self.get_area() > other.get_area():
            return self.get_area() - other.get_area()
        else:
            return other.get_area() - self.get_area()
    def __round__(self):
        """Returns if the shape is a circle"""
        if self.__class__.__name__ == "Circle":
            return True
        else:
            return False
