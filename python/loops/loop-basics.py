# Loops: loops in python are used to execute a block of code multiple times. for ex- if i want to print 1 to 1000, in manually i have to write print(1) to 1000, 1000 times so to not do this manually we use loops.

# For loop
items = ["Apple", 99, "Banana", 80, "Oranges", 50]   # Its a list with some values inside.

for item in items:   # This is will create a loop of the items in your list, by printing them one by one.
    print(item)

# This is a basic example of how you can create a for loop on a list.


# Use of range function in for loop: range function generates a sequence of numbers.

for i in range(0, 11):   # You can also write just (10) it understands that you are saying (0, 11). By using range function you can iterate on a range , here it will create a loop from 0 to 10 so the value of i will be 0 to 10.
    print(i)


# Start and step:

for i in range(1, 21, 2):   # It will create a loop and you can assign a step in here its- 2, so it will skip/move forward the loop by 1 it will print 1, 3, 5, 7...
    print(i)

# In this case the start is 1 and the step is 2.


# For loop through a string

for char in "Mohit":   # It will create a loop and will print all the character of the string one by one.
    print(char)


# While loop, is very similar to for loop.

count = 1   # Count is a variable.

while count <= 10:   # Here we are creating a condition that if 1 <= 10 is true it will print count. till the condition is true it will keep printing, it will run till the condition is false. 
    print(count)
    count += 1   # It updates the value of count from 1 to 2 to 3 to 4 till its 10. otherwise the value of count will always be 1 cause of that it will keep printing stuck in an infinite loop.
    