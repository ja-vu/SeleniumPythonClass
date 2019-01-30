"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
"""

def getInfo():
    name=input("What is your name")
    age = input("How old are you?")
    num=input("What's your favorite number?")
    #num=int(num)
    hundredyearsold = str(2019 + (100 - int(age)))
    for i in range(int(num)):
        print("Hi " + name + "! In 2019 you are " + age + " years old" + "\n")
        print("In the year " + hundredyearsold + ", you will be 100 years old" + "\n")



getInfo()