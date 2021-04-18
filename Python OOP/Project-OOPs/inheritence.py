class Polygon:
    __width = None
    __height = None

    def set_values(self,width,height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


class Rectangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height()


class Triangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height() / 2


if __name__ == '__main__':
    rect1 = Rectangle()
    tri1 = Triangle()

    rect1.set_values(20, 30)
    print(rect1.area())
    tri1.set_values(20, 30)
    print(tri1.area())
