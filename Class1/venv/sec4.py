"""
Sec 4 - 22
"""

cars = ["bmw", "audi", "lexus"]
empty_list = []
print(cars)
print(empty_list)


print("*#" * 20)


print(cars[0])

num_list = [1, 2, 3]
sum_num = num_list[0] + num_list[1]

print(sum_num)

more_cars = ["honda", "toyota", "KIA"]
print(more_cars[1])

more_cars[1] = "Benz"

print(more_cars[1])
print(more_cars)

"""
Lecture 13
"""

cars_2 = ["bmw", "honda", "audi"]
length = len(cars_2)
print(length)
cars_2.append("Benz")
print(cars_2)

cars_2.insert(1, "Jeep")
print(cars_2)

x = cars_2.index("honda")
print(x)

y = cars_2.pop()
print(y)
print(cars_2)

cars_2.remove("Jeep")
print(cars_2)

slicing = cars_2[1:]
print(slicing)
print("*#" * 20)

print(cars_2)
cars_2.sort()
print(cars_2)