# Default parameters values, in function you can pass default values to the parameters, and if you pass a value that default value will be overridden and if no value given it will pass the default one.

'''
def greet():
    print("Hi")

greet()   # This will run.
greet("Rohan")   # But This will throw an error cause there is no parameter in the function and you are passing a value to it
'''

"""
def greet(name):
    print("Hi", name)

greet()   # But This will not run, cause there is a parameter and its asking for a value.
greet("Mohit")   # This time it will run.
"""

def greet(name="User"):
    print("Hi", name)

greet()
greet("Mohit")
greet("Rohan")


# Keywords Arguments, arguments can be passed using the parameters name.

def user_info(name="", city=""):
    print("Hello", name, "You live in", city)

user_info(name="Mohit",city="Lucknow")   # Here you are assigning values to parameters while you are calling the function.


# Docstrings, and are used to attach information about the function.
def subtract(a, b):
    """Returns the difference of two numbers"""
    return a - b

sub = subtract(10, 4)
print(sub)
print(subtract.__doc__)