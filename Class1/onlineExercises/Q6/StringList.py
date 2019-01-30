"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
"""

word = input("Give me a word and I will check if this is a palindrome or not: ")

#laval

isPalindrome = False

if word == word[::-1]:
    isPalindrome = True
    print(word + " is a Palindrome")

else:
    print(word + " is not a Palindrome")
    print(word + " in reverse order is: " + word[::-1])
