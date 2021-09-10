from figure import Figure
import math

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self.__radius = value
            return self.radius
        raise ValueError(f"Radius value is not valid: {value}")

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius