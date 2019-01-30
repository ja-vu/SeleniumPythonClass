"""
Data type to store more than one value in one variable name, in terms of key value pairs
Dictionary items are in brackets {} in key: value pairs, seperated with "," {'k1':'v1', 'k2':'v2'}
Not sequence, no indexing -> Mapping

"""

car = {'make': 'bmw', "model": '550i', 'year': 2016, 'transmission':"auto"}
print(car)

d = {}

model = car['model']

print(car['make'])
print(model)

d['one'] = 1
d['two'] = 2

print(d)

sum_1 = d['two'] + 8
print("Sum is equal to: " + str(sum_1))
d['two'] = d['two'] + 8
print(sum_1)