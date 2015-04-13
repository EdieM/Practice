formatter = "%r %r %r %r"

# each print line below has the items in the parenthesis as stand in for the %r's in formatter

print formatter % (1, 2, 3, 4)  # this will print 1 2 3 4
print formatter % ("one", "two", "three", "four")  # this will print one two three four
print formatter % (True, False, False, True) # booleans
print formatter % (formatter, formatter, formatter, formatter) # I think this one will print 16 booleans, since they were the last used
# my previous comment was wrong. it actually just prints the %r's. it doesn't hold on to what
# was labeled previously. Because they are raw! everything prints with quotation marks too.
# trying again with s's below.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)


formatter = "%s %s %s %s"

# each print line below has the items in the parenthesis as stand in for the %r's in formatter

print formatter % (1, 2, 3, 4)  # this will print 1 2 3 4
print formatter % ("one", "two", "three", "four")  # this will print one two three four
print formatter % (True, False, False, True) # booleans
print formatter % (formatter, formatter, formatter, formatter) 
# with the %s's, it prints 16 %s's, with no quotation marks around them. Also, all the other 
# strings are printed without quotation marks around them.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
