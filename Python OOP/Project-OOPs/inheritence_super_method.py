class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent __init__", name)


class Parent2:
    def __init__(self, name):
        self.name = name
        print("Parent2 __init__", name)


class Child(Parent2 , Parent):
    def __init__(self):
        print("Child __init__")
        super().__init__('ameen') # in multiple inheritance , super() refers first inherited class only
        Parent.__init__(self,'ameen1') # need to call wih class name


child = Child()
