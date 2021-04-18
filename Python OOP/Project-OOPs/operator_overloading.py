import math


class Circle:
    def __init__(self,radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __add__(self, other):
        return Circle(self.get_radius() + other.get_radius())

    def __lt__(self, other):
        return self.get_radius() < other.get_radius()

    def __gt__(self, other):
        return self.get_radius() > other.get_radius()

    def __str__(self):
        return f'Circle Area = {self.area()}'


c1 = Circle(10)
c2 = Circle(20)
c3 = c1 + c2
print(c1.get_radius())
print(c2.get_radius())
print(c3.get_radius())
print(c3.area())

print(c1 < c2)
print(c3 > c2)

print(c1)
print(c2)
print(c3)


