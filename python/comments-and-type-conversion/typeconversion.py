# Typeconversion / Typecasting : means to convert one data type to another data type.

'''
age = "45"
print(age + 5)    It will show an error, cause you can't add a string to an integer.
'''

# Revised version : string to integer

age = "35"
print(int(age) + 5)   # You are converting a string to an integer, here you want the integer value of age + 5 to get add, int(age) converts the string value to integer.

# Another example : string to float

price = "1999.99"
print(float(price) + 5)

'''
Will this example show an error ? yes it will, cause its not a valid value/string. Not every string can be converted into a number.

num = "456fghfgh"
print(int(num))
'''

# For type conversion/typecasting you have functions like int(), bool(), str(), float()

# Few more examples :

# Converting string to integer
age = "25"
age = int(age)
print(age)
print(type(age))

# Converting string to float
price = "499.99"
price = float(price)
print(price)
print(type(price))

# Converting number to string
total = 1000
message = "total sales: " + str(total)
print(message)

'''
Common error in type conversion : example : not every string can be converted into an integer. This will cause an error

value = "abc"
print(int(value))
'''