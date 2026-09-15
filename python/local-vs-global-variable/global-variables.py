# Global variable

x = 89   # x = 89 is also a global variable.   # If you have defined x above the function even if its a global variable, it will call it, but if its below and outside of function it will not call.
def nmb():
    x = 72   # Its a local variable and now the print statement inside the function will call this variable and not the global x = 89.
    print(x)   # The print statement will throw an error saying x is not defined, i am talking about the x  = 99.

nmb()
x = 99   # Here x is a global variable.


# Global Keyword, Use of Global keyword helps to change to the global variable inside a function.

x = 78   # Global variable.
def show_value():
    global x   # This will modify the scope x = 89  to global variable.
    x = 89   # Local Variable, now Local --> Global.
    print(x)

show_value()
print(x)   # I know that this will print the global variable x = 78 everytime i call it, what if i want to call x = 89 it will not cause its a local variable.


# Note (observation): If you will comment or remove show_value() from which you call the function, the print(x) will print the x = 78 and not x = 89.

'''
Summary --> * variables inside the function is called local variable, and it can only be used within that function.
* And variables oustide of all function is called global variable, they can accessed/used from anywhere in the program.
* But if you want to modify or change the global variable from inside a function use global keyword.
'''