# fString, (formatted string lateral) is used to format strings in python. if you want to put variables directly inside a string we use fstring.

'''
Very basic example:

name = "Mohit"
age = 22

print(f"Hi, i am {name} and i am {age} years old.")
'''
# There are multiple ways to format a string you can use fstring, or use string concatination, earlier there was a format function.

name = input("Whats your name: ")
work = input("Where do your work: ")
live = input("Where do you live: ")

# string concatination:
print(name +" works at "+work+" and lives in "+live)

# format function
print("{} works at {} and lives in {}.".format(name, work, live))

# fstring
print(f"{name} works at {work} and lives in {live}.")