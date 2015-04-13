# Write a method that takes in a string. Return the longest word in
# the string. You may assume that the string contains only letters and
# spaces.
#
# You may use the String `split` method to aid you in your quest.
#
# Difficulty: easy.

x = raw_input("Give me a sentence of text: ")

def longest(list):
    list = x.split(' ')
    print list
    print max(list, key = len)
	
longest(list)

print "_" * 40
