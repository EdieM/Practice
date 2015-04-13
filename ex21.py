def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
	
print "Let's do some math with just functions!"

# age = add(30, 5)
# height = subtract(78, 4)
# weight = multiply(90, 2)
# iq = divide(100, 2)

# print "Age: %d, Height: %d, Weight: %d, IQ %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
# print "Here is a puzzle."

# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# print "That becomes: ", what, "Can you do it by hand?"


age = add(46, 6)
height = subtract(98, 12)
weight = multiply(100, 3)
iq = divide(250, 2)

print "\nHere is a puzzle.\n"

this = add(age, subtract(height, multiply(weight, divide(iq, 4))))

print "And the answer becomes ", this
