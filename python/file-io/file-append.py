# Append function, is used to append line/lines in an existnig file.

append = "\nfew lines about myself..."   # \n is an escape sequence character, \n for new line.

file = open("Write.txt", "a")   # a stand for append mode.
file.write(append)
file.close()

file = open("Write.txt", "r")
content = file.read()
print(content)
file.close()