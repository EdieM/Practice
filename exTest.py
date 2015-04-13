# This will be my tester problem file. When I have figured out the problem, I will put a 
# hashtag in front of all the lines. ## means it was already a comment. 
# beginner problems are from http://www.upriss.org.uk/python/PythonCourse.html

# http://www.upriss.org.uk/python/session2.html
# F_temp = raw_input("What is the temperature outside? ") 
# C_temp = (int(F_temp) - 32) / 1.8
# print "Let's see if we can convert %s from Farenheit to Celsius." % F_temp
## print F_temp " minus 32 and divided by 1.8 = " C_temp <--won't work.
# print "%s Farenheit minus 32 and divided by 1.8 = %s Celsius" % (F_temp, C_temp)


# ____________________________________________________________
# print "hello\n"
# print "to print a newline us \\n"
# print "she said: \"hello\""
# print "\tthis is indented"
# print "this is a very, very, very, very, very, very \
# long print statement"
# print """
# this is amulti like print staement
# this is a mu
# fjsok
# """


# ____________________________________________________________
# write a python script that prints the following figure
# print "\t\\  |  /"
# print "\t  @ @"
# print "\t   *"
# print "\t \\\"\"\"/"

# write a python script that prints the following figure
# this is me trying to make it all onto less lines
# print """
# \t\\  |  /
# \t  @ @
# \t   *
# \t \\\"\"\"/
# """

# write a python script that prints the following figure
# this is me trying to make it all onto less lines AGAIN!
# print "\t\\  |  /\n\t  @ @\n\t   *\n\t \\\"\"\"/"


# ____________________________________________________________
# b = "the"
# c = "cat"
# d = " is on the mat"
# a = b + " " + c + d
# print a
# b = b + " "
# a = b * 5
# print a 
# print "The first character of ", c, "is" ,c[0]
# print "The word\""+ c +"\" has", len(c) , "characters"

# name = raw_input("Please, type in your name: ")
# name = (name + "!\n") * 5
# print name


# ____________________________________________________________
# I was supposed to write a program that asks for fave color, then prints it out in shape
# of a box. is a box when color is 3 letters long...how to get it to be a box no matter
# the number of letters in raw_input?
# fave_color = raw_input("What's your favorite color?\n>")
# print "\n"
# print (fave_color + " ") * 10
# print fave_color, "\t   " * 4, fave_color
# print fave_color, "\t   " * 4, fave_color
# print (fave_color + " ") * 10
# print "\n"


# ____________________________________________________________
# if statement

# answer = raw_input("Do you like Python?\n> ")
# if answer == "yes":
#	print "That is great!"
# elif answer == "no":
#	print "That is disappointing!"
# else:
#	print "Thats not really what I was asking..."

# ____________________________________________________________

# I want it to get user to input a number
# it must be between 1 and 100
# The computer will already have a number in mind, based on how I input the program.
	# basically what number i input
# based on what the person guesses, the computer will say too high or too low
# when the person guesses the number right, the comp will tell them how many guesses
# it took to get to the right answer. 

# trying to make a function(?) that i have to put the number in when i run the program
# def or imp program #d


# def num_guess(num_high, num_low)

# from sys import argv
from sys import randint
randint(1, 100)  # inclusive


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

	
	
# if int.guess > num
#	print "Too high. Guess again. \n:>"
#	if int.guess < num 
#	print "Too low. Guess again. \n:>"
#	else 
#	print "Great job! You got it right!"
	


# raw_input(num) # where number = the number i put in when running program
		# or would this also be number = raw_input()
	# if num_guess > num print "Too high. Guess again \n:>"
	# elsif num_guess < num print "Too low. Guess again \n:>"
	# else num_guess == num print "Nice job! That's right! It took you " #amount_of_guesses,
	# " to get it right."
	
	


