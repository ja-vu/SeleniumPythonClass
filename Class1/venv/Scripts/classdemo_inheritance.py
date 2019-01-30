"""
Inheritance
"""

class Car(object):
    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped")

class BMW(Car):
    def __init__(self):
        Car.__init__(self)
        print("You just created the BMW instance")

    def drive(self):
        super(BMW,self).drive()
        print("Print you are driving a BMW, Enjoy...")
        # will override the drive method in car

    def headup_display(self):
        print("This is a unique feature")


c1 = Car()
c1.drive()
c1.stop()

c2 = BMW()
c2.drive()
c2.stop()
c2.headup_display()