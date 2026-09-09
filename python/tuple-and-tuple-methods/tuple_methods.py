# Tuple Methods, by using methods we can perform operations on elements/values, we can access these values but we cant change an existing value, add a new one, or remove existing one.

fruits = ("Apple", "Banana", "Orange", "Banana")
print(fruits)

print(len(fruits))   # Len is function that returns the number of elements in a tuple.

'''
fruits[0] = "Strawberry"   # Example of = tuples are immutable you cannot change the actual value.
print(fruits)
'''

print(fruits.count("Banana"))   # .count, counts the number of time an element appeared.

print(fruits.index("Banana"))   # .index, returns the index number of an element, but only the first occurance one.


numbers = (19, 23, 9, 3, 1)   # You can create a loop of tuple elements using a for loop.

for number in numbers:
    print(number)


# Tuple Packing and Unpacking

# Packing:
data  = 10, 20, 30, 99   # Multiple values can be packed inside a tuple.
print(data)

# Unpacking:
a, b, c, d = data   # Here the tuple values are getting unpacked in seperate variables.
print(a)
print(c)
print(d)


# Converting a tuple into a list, sometimes we want to change a value, add or remove one but i know that in tuple i cant do that so i will convert the tuple into a list and then change the values.

mix = (99, "Mohit", 5.11, True)   # This is a tuple with mixed data types.
print(type(mix))

lst = list(mix)   # Here we typecasted the tuple into a list.
print(lst)
print(type(lst))

lst[0] = 100   # And now we change the values and after changing the values.
lst[2] = 6.1
lst[1] = "Rohit"
print(lst)

new_mix = tuple(lst)   # We converted it back to a tuple.
print(new_mix)