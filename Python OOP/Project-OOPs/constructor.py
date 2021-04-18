class Person:
    def __init__(self,*args,**kwargs):
        self.name = args[0]
        self.age = args[1]
        self.height = args[2]
        self.weight = kwargs['weight']
        self.color = kwargs['color']


pakaran = Person('pakaran',32,170,weight=80,color='red')
print(pakaran.name)
print(pakaran.age)
print(pakaran.height)
print(pakaran.weight)
print(pakaran.color)