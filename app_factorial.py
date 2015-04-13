

# Write a method that takes an integer `n` in; it should return
# n*(n-1)*(n-2)*...*2*1. Assume n >= 0.
#
# As a special case, `factorial(0) == 1`.
#
# Difficulty: easy.


n = raw_input("Give me a number, please: ")
int_n = int(n)
	
def factorial(int_n):
	if int_n == 0:
		return 1
	else:	
		return int_n * factorial(int_n - 1)
	
print "The factorial of %d is %d. " % (int_n, factorial(int_n))


#These are tests to check that code is working. should all print True
print 'factorial(0) == 1: ' + str(factorial(0) == 1)
print 'factorial(1) == 1: ' + str(factorial(1) == 1)
print 'factorial(2) == 2: ' + str(factorial(2) == 2)
print 'factorial(3) == 6: ' + str(factorial(3) == 6)
print 'factorial(4) == 24: ' + str(factorial(4) == 24)
print "_" * 40


