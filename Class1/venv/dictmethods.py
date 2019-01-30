
"""
Dictionary Methods

"""
car = {'make': 'bmw', "model": '550i', 'year': 2016}
cars = {'bmw':{'model':'550i', 'year': 2016}, 'benz':{'model': 'E250', 'year': 2017}}

print()
print("*** KEYS METHOD ***")
print(car.keys())
print(cars.keys())

print()
print("*** VALUES METHOD ***")
print(car.values())
print(cars.values())

print()
print("*** ITEMS METHOD ***")
print(car.items())
print(cars.items())

print()
print("*** COPY METHOD ***")
car_copy = car.copy()
print(car_copy)


print()
print("*** POP METHOD ***")
print(car.pop('model'))
print(car)



print()
print("*** CLEAR METHOD ***")
car.clear()
print(car)