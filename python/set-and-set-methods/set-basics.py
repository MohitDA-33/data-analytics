# Set and Set Methods

# Sets, are used to store multiple values in a single variable, it does not allow duplicate values and do not maintain any specific order.

s1 = {1, 5, 6, 9, 333, 31, 9, 1, 97}   # Its a syntax of how you create a set, we create one using curlybraces.
print(s1)

# Property of set: if you enter multiple duplicate values it will return/print only one. Set automatically remove duplicates.

# Creating an empty set

'''
s2 = {}    Thats not how you create an empty set, it will rather create a dictionary.
print(s2)
print(type(s2))
'''

s2 = set()   # This is how you create an empty set, set().
print(s2)
print(type(s2))
