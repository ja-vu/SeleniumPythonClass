def exceptionHandling():
    try:
        car = {'make':'honda', 'model':'Civic','year':'2019'}
        print(car['make'])
        print(car['model'])
        print(car['year'])
        #print(car['color'])
    except:
        print("Undefined Key")
    finally:
        print("Please try a different key")

exceptionHandling()






