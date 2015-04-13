# Write a method that will take a string as input, and return a new
# string with the same letters in reverse order.
#
# Don't use String's reverse method; that would be too simple.
#
# Difficulty: easy.

word = raw_input("What word would you like reversed? ")

def reverse(word):
	print word[::-1]
				
reverse(word)
print "_" * 40