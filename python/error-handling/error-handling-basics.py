# Error handling, ensures you are handling the errors property, to study error-handling we will create an error on purpose.
# And cause of error the python program crashes.

print("Intializing...")

a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:   # 1- If this line of code doesnt execute maybe cause of an error.
    print("The value of a/b is", a/b)   # It will throw an error if the value b is 0, and cause of that the lines of code written after is not goint to execute.

except Exception as error:   # 2- Then print this except.
    print("Some error occured!")
    print(error)   # It will throw an error: division by zero

print("Thank you")

# So to fix this or not get an error we will wrap it inside [try and except].

# And if you want to know what was the error or what error came use [Exception].