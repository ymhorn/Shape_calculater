class Shape:
    def get_area(self):
        pass
    def __str__(self):
        return f"The shape is a {self.__class__.__name__}"

a = Shape()
print(str(a))

