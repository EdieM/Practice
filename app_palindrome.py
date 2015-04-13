# Write a method that takes a string and returns true if it is a
# palindrome. A palindrome is a string that is the same whether written
# backward or forward. Assume that there are no spaces; only lowercase
# letters will be given.
#
# Difficulty: easy.

string = raw_input("Do you think you know a palindrome? Take a guess: ")

def palindrome(string):
	if string[::-1] == string:
		print "True"
	else:
		print "False"
		
palindrome(string)