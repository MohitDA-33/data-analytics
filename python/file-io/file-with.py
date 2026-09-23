# Use of with, with is keyword that if you use, then you dont have to close the file.

a = "\nfew more lines about myself..."

with open("Write.txt", "a") as file:   # you can also write file as 'f' too, file -_> 'f'.
    file.write(a)

# usecase of with --> just to make the syntax simple nothing else, and it will automatically close the file.

with open("Write.txt", "r") as file:
    content = file.read()
    print(content)

'''
Summary :
open() with "w" = Writing
.write() = writing content
.close() = Close the file
"r" = reading
.read() = reading the whole content
.readlines() = getting the lines as a list
"a" = appending
with open(...) = automatically handles the closing of file
\n = new line
'''