# Task1

def oops():
    #raise IndexError()
    raise KeyError() #Замінюємо

def call_oops():
    try:
        oops()
    except IndexError:
        print("IndexError is catched")


call_oops() # Програму зупинено. KeyError світиться в консолі.

# Task2

def function(a, b):
    a = int(a)
    b = int(b)
    return a**2/b

a = input("Input first argument: ")
b = input("Input second argument: ")

try:
    print(function(a,b))
except ValueError:
    print("Arguments should be integers")
except ZeroDivisionError:
    print("Devider should not be zero")