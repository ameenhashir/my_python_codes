from rectangle import Rectangle
from triangle import Triangle


if __name__ == '__main__':
    rect1 = Rectangle()
    tri1 = Triangle()

    rect1.set_values(20, 30)
    print(rect1.area())
    tri1.set_values(20, 30)
    print(tri1.area())

    rect1.set_color('Blue')
    print(rect1.get_color())