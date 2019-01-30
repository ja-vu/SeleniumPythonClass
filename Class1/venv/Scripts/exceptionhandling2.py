"""
Exceptions are errors
We should handle exceptions in our code to make
sure the code is working the way we want and is
handling all the unwanted issues
Link to 3.5 built-in exceptions - https://doc.python.org/3/library/exceptions.html

"""

def exceptionhandling():
    try:
        a = 10
        b = 20
        c = 0

        d = (a + b) / c
        print(d)
    except:
        print("In the except block")
        raise Exception("This is an exception")
    else:
        print("Because there was no exception, else is executed")
    finally:
        print("Finally, always executed")

exceptionhandling()