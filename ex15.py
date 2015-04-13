# from the system, import an argument variable.
from sys import argv

# this is a script, and the argument variable is the filename we are working with.
script, filename = argv

# 'txt' is the name of the file (filename) being opened
txt = open(filename)

# print the text with the filename in place of the %r
print "Here's your file %r:" % filename
# print the opened file for us to read.
print txt.read()

# user, type this info, which will be named file_again. 
print "Type the filename again:"
file_again = raw_input("> ")

# txt_again opens the file named file_again
txt_again = open(file_again)

# print out the opened file for us to read.
print txt_again.read()
