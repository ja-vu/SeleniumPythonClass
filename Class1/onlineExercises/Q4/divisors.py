"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
"""

num = int(input("Please give me a number"))

x = range(1, num+1)

x2 = []

for i in range(len(x)):
    if num % x[i] == 0:
        x2.append(x[i])
print(x2)
