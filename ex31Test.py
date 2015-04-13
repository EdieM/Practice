print "You come to a clearing in the dark forest. Which way will you turn, R (right) or L (left)?"

direction = raw_input(": ")

if direction == "R" or direction == "right" or direction == "r" or direction == "Right":
	print "So you're going right, huh? Right into some rattlesnakes. Good job!"
	print "Choose 1 - Beat the snakes with a stick."
	print "or Choose 2 - Set the snakes on fire."
		
	snakes = raw_input(": ")
	
	if snakes == "2":
		print "The fire grows out of control! Quick! Run into the"
		print "1. lake or"
		print "2. waterfall?" 
		
		fire = raw_input(": ")
	
		if fire == "1":
			print "Great quick thinking. You'll live to see another day."
		else: 
			print """
			Things aren't looking so good...the pirahnas are taking little nibbles...
			\t...and larger nibbles...
			\t\t...and LARGER NIBBLES...
			\t\t\t...and...you die. Good job!
			"""
	else:
		print "The snakes bite you 1,000 times. Good luck with that."
		
elif direction == "L" or direction == "left" or direction == "Left" or direction == "l":
	print "You left behind safety and are now facing a bear. Good job!"
	print "Choose 1 - Act big and roar loud."
	print "or Choose 2 - play dead."
	
	bear = raw_input(": ")
	
	if bear == "2":
		print "Smart move. The bear moves on."
		print "Now, random choice. 1 or 2?"
	
	
		random = raw_input(": ")
	
		if random == "1":
			print "Aww...what luck! You immediately die from poisoned plants. Good job!"
		else:
			print "Giant ants crawl into your stomach and eat you from the inside out. Good job!"
		
	else:
		print "Brave, dude! You die. But so, SO brave!"
else:
	print "You stumble around and fall on a knife and die. Good job!"
