# Local and Global Variable, variables in python have a scope and scope defines where the variables can be accessed.

# Local variable

def show_value():
    x = 11   # x is a local variable.
    print(x)

show_value()
x = 78   # And here x is a global variable, not inside any function, its outside of program.
show_value()   # The function show_value will not call this x = 78 cause it has no relation with and has its own variable (x = 11).  
print(x)   # This will print x = 78, cause this print() is not inside any function and will print the global variable.
