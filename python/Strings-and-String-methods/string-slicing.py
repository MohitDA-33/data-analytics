# Slicing, to get or access a range of elements we use slicing.

name = "Mohit Rajpal"

print(name[0:5])
print(name[6:13])
print(name[0:13])
print(name[-6:])
print(name[-12:-7])
print(name[-1])
print(name[-6])
print(name[-8])
print(name[-12])
print(name[0])
print(name[4])
print(name[6])
print(name[11])

# Note: if you are getting confused in negative indices/indexes, convert it from negative to positive just by adding the length of the string to negative indices.

# Example:

city = "Lucknow"
print(len(city))
print(city[-1])   # -1 --->  7 + (-1) = 6
print(city[-7])   # -7 --->  7 + (-7) = 0