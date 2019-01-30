class Fruit(object):
    def __init__(self):
        print("Welcome to the fruit class")

    def nutrition(self):
        print("This fruit is very nutricious")

    def fruit_shape(self):
        print("This fruit has a generic fruit shape")

class Orange(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("Welcome to the orange class")

    def nutrition(self):
        super(Orange,self).nutrition()
        print("Orange is very high in Vitamin C")

    def color(self):
        print("The color this fruit is oragnge")

f1 = Fruit()
f1.nutrition()
f1.fruit_shape()
print(10*"=== ")
f2 = Orange()
f2.nutrition()
f2.color()
f2.fruit_shape()