# Write a method that takes a string and returns the number of vowels
# in the string. You may assume that all the letters are lower cased.
# You can treat "y" as a consonant.
#
# Difficulty: easy.

sentence = (raw_input('Tell me something. \n:> '))

def count_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = []
    
    for x in sentence:
	    if x.lower() in vowels:
	        chars.append(x)
    print ' '.join(chars)
    print len(chars)

count_vowels(sentence)

