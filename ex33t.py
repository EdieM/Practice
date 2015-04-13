
numbers = []

def test(i, r, z): 
	while i < r:
    		print "At the top i is %d" % i
    		numbers.append(i)

    		i = i + z
    		print "Numbers now: ", numbers
    		print "At the bottom i is %d" % i

test(12, 25, 2)

print "The numbers: "

for num in numbers:
	print num

    	
def new(i, r, z):
	for i in range(r, z):
		print "At the top i is %d" % i
		print "Numbers now: ", numbers
    	print "At the bottom i is %d" % i

new(5, 7, 10)