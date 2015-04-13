# Write a method that takes a string in and returns true if the letter
# "z" appears within three letters **after** an "a". You may assume
# that the string contains only lowercase letters.
#
# Difficulty: medium.

sentence = raw_input("tell: ")

def skipMultiples():
	zero = 0
	while zero < sentence.length:
		if sentence[zero] != "a"
			zero += 1
			print "True"
		else:
			print "False"
	
skipMultiples()