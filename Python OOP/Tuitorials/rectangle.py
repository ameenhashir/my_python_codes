from module1.polygon import Polygon1
from module1.shape import Shape1
class Rectangle1(Polygon1,Shape1): # multiple inheritance
    def area(self):
        return self.get_length() * self.get_width()
