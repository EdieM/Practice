print "How old are you?", 
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# the comma at the end keeps the 'print' from ending with a newline 

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you are %s years old, %s tall and %s heavy." % (age, height, weight)

print "*" * 15

print "So...what's your name?",
name = raw_input()
print "\t...do you have a boyfriend?",
boy_or_girl = raw_input()
print "\t\t...and how old is this person?!",
old = int(raw_input()) #gets number as a string, converts into an integer. int()
print "...WELL, \nWHATEVER \nTHEN! I don't need %s, %s or %s!" % (name, boy_or_girl, old)
