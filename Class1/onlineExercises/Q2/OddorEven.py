"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
"""

def getNum():
    num = int(input("Give me a number"))
    check = int(input("Give me a second number"))

    if num % 2 == 0:
        print("Your first number is even")
    else:
        print("Your first number is odd")

    if num % 4 ==0:
        print("Your first number is a multiple of 4")
    else:
        print("Your first number is not a multiple of 4")

    if num % check == 0:
        print(str(check) + " divides evenly into " + str(num))

    else:
        print(str(check) + " does not divide evenly into " + str(num))
getNum()
