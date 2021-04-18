class Car:
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color = color

    def set_speed(self,value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color


ford = Car(100,'Blue')

# ford.speed = 100
# ford.color = 'Blue'

ford.set_speed(200)
ford.set_color('Green')
print(ford.get_speed())
print(ford.get_color())

print(ford.__speed)
print(ford.__color)