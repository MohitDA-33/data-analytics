# Conditional statements in python, sometimes you want to run/execute a block of code based of a condition, for that we have conditional statements.



# if --> if checks the condition if it's true then it execute otherwise not.

age  = int(input("Enter you age: "))

# Note: remember input function always return an output as a string, so we are using the int() function to typecast.
 
if age >= 18:
    print("You are an adult!")

else: 
    print("You are a minor!")

# Whats happening here is we are taking an input asking for an age, if your age is above or equal to 18 it will print the if statement otherwise not then it will print the else.
# The whole code works in conjunctions, means if the condition is true then this will run and if not then else will run.


nm = int(input("Enter your number: "))

if nm >= 100:
    print("The number you have typed is greater or equal of 100")

else: 
    print("The number you have typed is less than 100")



nm = int(input("Enter a number: "))

if nm % 2 == 0:
    print("This number is even")   # The input number nm gets divided by 2 and if the remainder is 0 it's an even number.

else:
    print("Its an odd number")