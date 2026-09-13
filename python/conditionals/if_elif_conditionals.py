age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to get a driving license")

elif age >= 16:   # elif stands for else if, works when the if condition is false.
    print("You are not eligible but i can assign a temporary license!")   # I can use as much elif as i want. 

else:
    print("You are just a minor and cannot drive")

# If you write elif all three will work together as a ladder with each other.

# Whats happening here is we are asking age as an input, and according to the age there are conditions, and if it matches the condition it fits, it will print/return statement inside.


# Another example:

score = int(input("Enter your score to check your grade: "))

if score >= 90:
    print("Grade A")

elif score >=75:
    print("Grade B")

elif score >=55:
    print("Grade C")

elif score >=35:
    print("Grade D")

else: 
    print("Grade E")


# Use of comparision operator in python, condition sometimes use comparision operators.

x = 10

if x == 10:
    print("Equal")

if x != 5:
    print("not equal!")


# Use of logical operators in conditions, allows us to combine multiple conditions.
# You can use (and) operator in logical to combine conditions.

age = int(input("Enter you age: "))
country = input("Enter your country name: ")

if age >= 18 and country == "India":
    print("Allowed")

else:
    print("Sorry you are not allowed!")


# Nested conditionals, conditionals can be placed inside other conditionals.

age = int(input("Enter your age: "))

if age >=18:
    if age >= 60:
        print("You are in your 60s")

    elif age >= 50:
        print("You are in your 50s")

    elif age >= 40:
        print("You are in your 40s")

    elif age >= 30:
        print("You are in your 30s")

    elif age >= 20:
        print("You are in your 20s")

    else:
        print("You are above 18 but less than 20!")


# You can use (pass) statement in conditonal, yes there are statements in python that you can use like break, continue and pass.

nmb = int(input("Enter a number between 0 to 100: "))

if nmb >= 50:
    pass

else:
    pass