try:
    x = int(input("Enter a number: "))
    y = 10/x
    print(y)
except ValueError:
    print("Please a valid number")
except ZeroDivisionError:
    print("Division by zero is not allowed")
finally:   # finally always run no matter what, but we can print without finally to right ? yes you can.
    print("I hope you got your answer, thank you!")

# There are different ways of handling different exceptions, and the same way by applying different exceptions you can handle different types of errors.

# Suppose you are running a function, finally: is used when we have to return it to the function. and if there is no finally the function will not print/run this line.