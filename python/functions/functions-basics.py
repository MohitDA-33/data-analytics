# Functions in python, helps us to wrap a block of code, that are resuable. functions packages code so it can be used again and again.

print("Good Morning")
print("How are you!")
print("Thank You")   # If you want to print these statements ex- 50 times you have to write it manually, rather you have two choices 1- make a loop or 2- pack it inside a function.

# Choice 1- Make a loop
greet = ["Good morning", "How are you!", "Thank You"]

for i in range(5):
    print(greet[0])
    print(greet[1])
    print(greet[2])

# Choice 2- Pack it inside a function.
def greet():   # def, is a keyword in python used to create a function.
    print("Good Morning")
    print("How are you!")
    print("Thank You")

greet()   # This is how we call a function.


def greetings(fname, lname):   # fname and lname are parameters in function (greetings) that asks for value, it allow us to pass data to variables.  
    print("Hi", fname, lname, "nice to see you!")

greetings("Mohit", "Rajpal")


def add(a, b):
    return a + b   # To return a value we use return statement, it sends the value back from the function.

total = add(9, 19)   # Total is a variable, which will get the retured value from the function. 
print(total)