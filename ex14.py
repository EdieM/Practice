from sys import argv

script, user_name, lovely_bones = argv
prompt = 'WRITE NOW! '

print "Hi %s, i'm the %s script." % (user_name, script)
print "i'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s...and how did you hear about %s?" % (user_name, lovely_bones)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is. 
And you have a %r computer. Nice.
""" % (likes, lives, computer)



