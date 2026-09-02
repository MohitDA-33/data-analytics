# String and String methods

# String, string is a collection of characters that can be created using single quotes or double quotes, basically string is a text in python inside a variable.

name = "Mohit"   
city = 'Delhi'
print(name)
print(city)

# Multi-line string, can be created using a single/double triple quotes.

poem = '''twinkle twinkle
little star
how i wonder what your are'''
print(poem)

# String indexing, to access any element/s we use indexing and slicing.

# Indexing, starts from 0 and goes from left to right.
print(name[0])
print(city[0])
print(name[2])
print(city[4])
print(name[-1])
print(city[-2])

# Note: if you try to get an index out of the character range, python will show an error. like- string index out of range.