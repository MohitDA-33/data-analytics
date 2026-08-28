# Input() function : is used to take user input, it pauses the program in between and asks for the user to type something.

# Example:

name = input("whats your name: ")
print("Hi! " + name)

# (+) helps to concatinates 2 strings.
# Important note: Input function always returns a string. by default all the inputs taken by the function is a string

age  = input("Enter your age! ")
print(age)

# What if i want the integer version of age, or what if i to want add 10 to age, i can't cause its a string so here i will use int() function

age = int(input("Enter your age again! "))
print(age + 10)

price = float(input("Whats the price: "))
print("The price is ", price)

# The string written inside the input function is called an optional string, by this you can guide a user by showing a message.

# Few more examples: 

# The input function:
name = input()

# Input() function with a prompt message

name = input("Enter your name: ")

# Converting user input to integer

age = int(input("Enter your age: "))

# Converting user input to float

price = float(input("Enter product price: "))

# Taking user input for calculations
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))

total = quantity * price
print("Total amount:", total)

# Common input errors: when a user enters invalid data, it will show an error. example - a string instead of an integer an error will occur
