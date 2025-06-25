from Rectangle import Rectangle
from Square import Square
from Triangle import RightTriangle
from Circle import Circle
from Hexagon import Hexagon

class Calculater(RightTriangle,Circle,Hexagon):
    """All the methods of the shape calculater"""
    @staticmethod
    def shape():
        """To receive a shape from the user"""
        shape = input("Pick a shape\n "
              "1. Rectangle\n"
              "2. Square\n"
              "3. Triangle\n"
              "4. Circle\n"
              "5. Hexagon\n")
        if shape == "1":
            while True:
                try:
                    length = int(input("what is the length\n"))
                    break
                except ValueError:
                    print("sorry we need a number")
            while True:
                try:
                    width = int(input("what is the width\n"))
                    break
                except ValueError:
                    print("sorry we need a number")
            return Rectangle(length,width)
        elif shape == "2":
            while True:
                try:
                    side = int(input("what is the length of the side\n"))
                    break
                except ValueError:
                    print("sorry we need a number")
            return Square(side)
        elif shape == "3":
            while True:
                try:
                    base = int(input("what is the length of the base\n"))
                    break
                except ValueError:
                    print("sorry we need a number")
            while True:
                try:
                    height = int(input("what is the height\n"))
                    break
                except ValueError:
                    print("sorry we need a number")
            return RightTriangle(base,height)
        elif shape == "4":
            while True:
                try:
                    radius = int(input("what is the radius\n"))
                    break
                except ValueError:
                    print("sorry we need a number")
            return Circle(radius)
        elif shape == "5":
            while True:
                try:
                    side = int(input("what is the length of the side\n"))
                    break
                except ValueError:
                    print("sorry we need a number")
            return Hexagon(side)
        else:
            print("invalid option please try again")
            return Calculater.shape()
    @staticmethod
    def function(shape):
        """To receive the type of function from the user"""
        options = input("What would you like to me to do:\n"
                        "1. print the area of the shape\n"
                        "2. print the circumference of the shape\n"
                        "3. print the type of shape\n"
                        "4. Add it with the area of another shape\n"
                        "5. Print a length of the shape\n"
                        "6. The difference between the shape and another shape\n"
                        "7. Do you want to know if the shape is round?")
        if options == "1":
            print(shape.get_area())
            return
        elif options == "2":
            print(shape.get_circumference())
            return
        elif options == "3":
            print(str(shape))
            return
        elif options == "4":
            second_shape = Calculater.shape()
            print(shape + second_shape)
            return
        elif options == "5":
            print(len(shape))
            return
        elif options == "6":
            second_shape = Calculater.shape()
            print(shape - second_shape)
            return
        elif options == "7":
            print(round(shape))
            return
        else:
            print("invalid option please try again")
            return Calculater.function(shape)




