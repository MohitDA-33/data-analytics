# List and List Methods

# List, are used to store multiple values in a single variable and its ordered and mutable.

names = ["Harry", "Larry", "Garry"]   # To create a list we use square brackets.
print(names)
print(type(names))   # Type will tell you the type of the data structure, that its a list in this case.

fruits = ["Apple", "Grapes", "Orange"]

mixed_list = ["Mohit", 5.11, 22, True]   # Inside a list you can store any data type, and different data types under one.
print(mixed_list)

print(names[1])   # To access elements we use indexing and slicing.
print(mixed_list[1])
print(names[2])
print(mixed_list[-1])   # Example of negative indices.
print(mixed_list[-4])

print(names[0:3])   # Examples of string slicing.
print(names[1:3])
print(mixed_list[-4:])

fruits[0] = "Mango"   # You can modify a list element by telling its index number.
print(fruits[0])
mixed_list[0]="Rohit"
print(mixed_list[0])