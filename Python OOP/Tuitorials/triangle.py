from module1.polygon import Polygon1
class Triangle1(Polygon1): # Triangle class inherites polygon class,all public varibale and methods in Polygon class no accessible to Triangle
    def area(self):
        return self.get_length() * self.get_width() / 2
