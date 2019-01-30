import sys

"""
Examples to show available string methods in python


"""

#Accessing characters in a string

first = "nyc"[0]
city = "sfo"
print(first)

ft = city[0]

print("ft = " + ft)

"""
len()
lower()
upper()
str()
"""

str = "This is AMERICA"
print(len(str))
print(str.upper())


print("****************************************************************************************")

# Replace Method
a = "1abc2abc3abc4abc"
print(a.replace('abc','ABC', 1))

# Sub-Strings
# starting index is inclusive
# Ending index is inclusive

sub = a[1:6]
print("****************************************************************************************")
print(sub)


step= a[1:6:2]
print("****************************************************************************************")
print(step)
