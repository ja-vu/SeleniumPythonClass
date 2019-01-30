"""
https://docs.python.org/3/library/
"""

import math #This will import all of the math module, which will result in more memory use
from math import sqrt

#import modulesexternal.car as car
from modulesexternal.car import info

class ModulesDemo():
    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(25))

    def car_description(self):
        make = 'bmw'
        model = '550i'
        info(make,model)

m = ModulesDemo()
m.builtin_modules()
m.car_description()

