# lambda Functions, are one liner functions, they help us to write functions in one line.

# Normally we write a function like this.

def add(a, b):
    return a + b

total = add(11, 28)
print(total)


# Now the lambda function way.

sum = lambda a, b: a + b
print(sum(1, 78))

# Another example:

def cube(a, b = 3):
    print(a ** b)

cube(12)


cube = lambda a, b = 3: a ** b
print(cube(15))
