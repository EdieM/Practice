tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat # prints I'm tabbed in with a tabbed space before
print persian_cat # prints I'm split, then 'on a line' is on a new line (because \n)
print backslash_cat # looks like \\ prints the actual \. it is the escape from the \ alone
print fat_cat # tabbed list with * in front of each item. new line, tabbed space after 
# Catnip, then * before the last item



# now I'm just gonna try some stuff with the escape sequences.

fat_cat = '''
I'll do a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print fat_cat # no difference between """ and '''

# now I'm just gonna try some stuff with the escape sequences.
print "*" * 10

a = "\tSwimming."
b = "\n\t\\Swimming\\" # new line, then tab
c = "\t\t\tSwimming." # this tabs it 3x


print a, b
print c, b

d = 'I don\'t like this to impede future performance'

print d 

e = "I don't like this to \"impede\" future performance."

print e

f = "jumping \aThrough the hoops." #unsure what it does
g = "jumping \bThrough the hoops." #removes the space between 'jumping' and 'through'
h = "jumping \fThrough \f\fthe hoops." #new line with tab
i = "jumping \nThrough the hoops." #just new line

print f
print g
print h
print i

k = "Am I doing \rsomething all together new." #removes the words before the \r
l = "Going \vsomewhere totally new and \v\v\vdifferent." 
	#newline with tab that starts where last word ended. more makes newlines + tab

print k, l
print l

m = "Now just a new \ooosentence to try"

print m

# and now to try something new with %r and %s
print "-" * 15

lick = "Cats do this"
thin = "I am this"
feeling = "I am emotional"

print "Sometimes I tell people %r." % lick
print 'Sometimes I tell people \'and they think\' %r.' % thin
print "Sometimes I tell people \"Listen to THIS.\" \v\"%s\"." % lick
print 'Sometimes I tell people \v\v\v\v\v%s.' % feeling










