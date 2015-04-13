# from the system, import an argument variable.
from sys import argv

# this is a script, and the argument variable is the filename we are working with.
script, filename = argv

# 'target' is the name of the file (filename) being opened
target = open(filename)

print "We're going to open %r" % target
print "If you want that, hit RETURN"

raw_input("? ")

print "Opening the file..."

# printing out the contents of the file for us  to read
print target.read()

