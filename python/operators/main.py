# Operators are symbols used to perform operations on operands / values and variable.

# Major operators are : Assignment, Arithmetic, Logical, Comparision operators.

'''
Arithmetic operators: are used to perform mathematical calculations.
'''

a = 9
b = 7

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)   # Floor division
print(a % b)   # Modulus (leaves remainder)
print(a ** b)   # exponentiation

'''
Assignment operators: are use to assign values to variables
'''

x = 10   # Assign
x += 5   # Add and assign
print(x)

y = 10
y -= 3   # Subtract and assign
print(y)

z = 10
z *= 7   # Multipy and assign
print(z)

g = 10
g /= 2   # Divide and assign
print(g)

h = 10 
h //= 2   # Floor divison and assign
print(h)

i = 10
i **= 3   # Exponentiation and assign
print(i)

j = 10
j %= 5   # Modulus and assign
print(j)

'''
Comparision operator = compare 2 values and return either True or False
'''

a = 10
b = 5

print(a == b)   # Equal to
print(a != b)   # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)   # Greater than or equal
print(a <= b)   # Less than or equal

'''
Logical operators: helps us to compare 2 booleans
'''

a = 51
b = 49

print(a and b)
print(b and b)
print(a and a)

print(True and False)
print(False and False)
print(True and True)   # In (and) to get a true both of the value has to be true. and vice versa for false


print(a or b)
print(b or b)
print(a or a)

print(True or False)   # In (or) to get a true atleast one of the value has to be true. and vice versa for false
print(False or False)
print(True or True)

print(not(a > 49))
print(not(b == 49))

print(not(True))   # Not reverses the output
print(not(False))

'''
Membership operators : are used to test whether a value exists in a sequence or not. 
Note: i haven't studied about the list or sequence yet, but i have seen the examples of membership and understand the concepts.

in = exists in sequence
not in = does not exist
'''

numbers = [1, 2, 3]
print(2 in numbers)
print(2  not in numbers)

fruits = ["Apple", "Banana"]
print("Apple" in fruits)
print("guava"  not in fruits)

'''
Identity Operators and Bitwise operators: for now the instructor told us to skip these as he will cover this in the later lectures.
'''

# Note: operator precedence/priority: python evaluates the operators in specific order(high to low), operators with the higher precedence are evaluated first, basically tells you the evaluation order, which will evaluate first depends on the priority. 