# String Methods: by using methods and functions you can do string manipulation.

# Remember: string is an immutable data type means (cannot be changed after creation).

name = "  Mohit  "
city = "Delhi"
email = "example@gmail.com"

# String length:
print(len(name))   # len function tells you the length of the string.

# Common string Methods:

# lower() and upper()
print(name.lower())   # Will return a new string with all the characters in lower case. 
print(name.upper())   # Returns a new string with all the characters in upper case.

# strip()
print(name.strip())   # Removes the extra beginning and the ending spaces.
print(len(name.strip()))   # To check if it has removed the extra spaces or not.

# replace()
print(city.replace("Delhi", "lucknow"))   # Replaces a particular part of the string.

# split()
fruits = "apple,banana,orange,guava"
items = fruits.split(",")   # Splits a string into a list, based of a seperator here the seperator is (,).
print(items)

# join()
items = ["apple", "banana", "orange"]
text = ",".join(items)   # .Join, joins the elements of a list into a string. 
print(text)

# find()
print(email.find("@"))

# Startswith() and endswidth()
print(email.startswith("example"))   # IF a string starts with a given value then True.
print(email.endswith("com"))   # # IF a string ends with a given value then True.

# String concatination, means combining 2 or more strings, you can do that by using + operator.
first_name = "Mohit"
last_name = "Rajpal"
print(first_name +" "+ last_name)

# String Formatting, allows you to insert values into a string, there are two methods 1- .format and 2- f-string.
name = "Mohit"
age = 22
print("My name is {}, i am {} years old.".format(name, age))   # .format method.
print(f"My name is {name}, i am {age} years old.")   #  Use of f-string.

# Checking string contents
print(city.isalpha())   # Is it a alphabetical string.
# Note: .isalpha, if it contains a single space it will show a false.
print(name.isnumeric())   # Is it a numerical string.
print(name.isalnum())   # And is it a alpha-numeric string.

'''
Strings are immutable:
name[0] = "R"   Error, str does not support item assignment, remember strings are immutable.
print(name)
'''
