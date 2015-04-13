# import an argument from the system
from sys import argv

# input_file will be the file we will work with
script, input_file = argv

# defining the function print_all as reading and printing f 
# (which is the file we're working with)
def print_all(f):
	print f.read()

# defining the function rewind. f.seek() is moving the file to the 0 byte, starting to 
# read from there. 
def rewind(f):
	f.seek(0)
	
# defining the function print_a_line. 
def print_a_line(line_count, f):
	print line_count, f.readline() # add a , to end will remove extra spaces between lines
	
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# here, current line is just starting at line 1, then adding 1 manually each time we print
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# previous can be written like this too, its the same thing
current_line += 1
print_a_line(current_line, current_file)
