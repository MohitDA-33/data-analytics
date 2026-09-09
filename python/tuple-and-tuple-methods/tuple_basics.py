# Tuple and Tuple Methods

# Tuple, is used to store multiple values in a single variable similar to lists but the difference is that tuples are immutable (cannot be changed after creation).

number = (91, 90, 19, 56 ,39)   # To create a tuple we use paranthesis(), and if you remember in lists it was square bracket[].
names = ("Mohit", "Harry", "Ritesh")
mixed = (88, "Hitesh", 9.55, True)

# In tuples you can access the values but you cant change, add or remove it.

print(names)
print(type(names))
print(names[1])   # You can access the values using (positive/negative) indexing or slicing.
print(names[2])
print(names[-3])
print(names[0:4])

print(number)
print(type(number))
print(number[0])
print(number[2])
print(number[4])
print(number[-4])
print(number[-2])
print(number[0:])

print(mixed)
print(type(mixed))
print(mixed[3])
print(mixed[-4])
print(mixed[-2])
print(mixed[1:3])

tup = ("Larry", )   # To create a tuple with a single value, we need to put a comma(,).
print(tup)
print(type(tup))
lst = ["Larry"]   # Unlike in lists you can create a single value list without using comma(,).
print(lst)
print(type(lst))