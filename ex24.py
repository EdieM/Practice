print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \n\t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted 
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

# five = 10 - 2 + 3 - 6
five = -5 + (-20 + (50 - (2 * 10)))
print "This should be five: %s" % five

def secret_formula(started, here):
	jelly_beans = started * 500 + here
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
	
start_point = 65
start_here = 8000
beans, jars, crates = secret_formula(start_point, start_here)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 3

print "We can also do that this way: \nWith a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point, start_here)
