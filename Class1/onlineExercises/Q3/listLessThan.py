"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
"""


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in range(len(a)):
    if a[i] < 55:
        print(a[i])

print('===== ' * 5)

b = [1, 1, 2, 3]

print(b)

print('===== ' * 5)

print([1, 1, 2, 3])

print('===== ' * 5)

num = int(input("Give me a number \n"))

a2 = [i for i in a if i < num]
print(a2)
