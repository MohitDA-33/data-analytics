# File handling in python,

# write a file, write function.

Write = "Hi, i am Mohit nice to meet you!"   # Suppose i want to write this string in a file.

file = open("Write.txt", "w")   # open will open the file but in this case no file name Write.txt exists so it will create one.
# open function takes 2 arguments file name + mode (r = read, w = write, a = append... etc).
# "w" will write the string the file.

file.write(Write)   # .write is a function that will add this string in the file.

file.close()   # After the file is opened we tell the OS, that we are leaving/closing the file.

# When we run this program a new file Write.txt will be created.


# read a file, read function.

file = open("Read.txt", "r")   # "r" helps you to read the content of a file.
data = file.read()   # Whatever string is in the file Read.txt it will store it in the data. 
print(data)
file.close()


# readlines function, also helps you to read the content of a file but the content will not be in string it will be in a list.

file = open("Readlines.txt", "r")
content = file.readlines()
print(content)
file.close()

# Note: 'w' doesn't mean only write if the file exists it will replace/overwrite its exisiting content.