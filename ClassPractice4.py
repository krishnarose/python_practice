#   Create a class Shape with a method area(). Create subclasses Circle, Rectangle, and Triangle that override the area() method.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print(f"Area of Circle with radius {self.radius}, is {3.14 * self.radius * self.radius}")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print(f"Area of a rectangle with length {self.length} and breadth {self.breadth} is {self.length * self.breadth}")

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        print(f"Area of a triangle with base {self.base} and height {self.height} is {0.5 * self.base * self.height}")


# Create instances of each shape and calculate their areas
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4)

circle.area()
rectangle.area()
triangle.area()
