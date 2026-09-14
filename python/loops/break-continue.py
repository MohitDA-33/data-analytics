# Statements, you can use statements in loops to contol it.

# Break statement, stops the loop completely.

for i in range(11):
    if (i == 6):   # Whats happening here is, if the value of i is 6.
        break   # It will break the loop completely or stops the loop completely.
    print(i)


# Continue statement, stops the loop skips the current iteration and move on the next one.

for i in range(16):
    if (i == 10):   # If the value of i is 10 it will skip the iteration and will start the loop from 6. 
        continue
    print(i)

'''
Continue= 10 gets skipped.
Break= stops the loop at 5 and exits the loop.
'''

# Pass statement, acts as a placeholder where a statement is required.

for i in range(5):
    pass


# Looping with else 

for i in range(3):
    # if (i == 1):
    #     break
    print(i)
else:   # The else block runs when the loop finishes normally.
    print("Loop finished")

# Note: the else code does not run if the loop is stopped using break.
