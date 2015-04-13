from random import randint
randint(1,101) #Inclusive






























prompt = "> "

# script, num = argv

print """
Time to play a guessing game. Guess what number I\'m thinking. 
It\'s between 1 and 100.
"""

guess = raw_input(prompt)
guess = int(guess)
prog_num = int(num)

print guess	
print num
# if guess


# def analyser(guess)
# for guess in range(1, 100):
if guess == prog_num:
 	print "Righty!"
elif guess > prog_num:
 	print "Too high. Guess again. \n:>" 
else:
 	print "Too low. Guess again. \n:>"
# raw_input()