def dogs_and_cats(dogs_count, cats_count):
	print "There are %d dogs in here!" % dogs_count
	print "What about the %d cats? Pay attention to that!"% cats_count
	print "Better get a blanket.\n"
	
print "We can just give the function numbers directly:"
dogs_and_cats(45, 23)

print "Or we can use variables from our script:"
num_of_dogs = 56
num_of_cats = 25

dogs_and_cats(num_of_dogs, num_of_cats)

print "We can even do math inside too:"
dogs_and_cats(42 + 5 - 9, 3 * 25)

print "And we can combine the two:"
dogs_and_cats(num_of_dogs + 10, num_of_cats / 5)

print "This is making a new variable and multiplying the two"
num_of_dogs_b = 100
num_of_cats_b = 50

dogs_and_cats(num_of_dogs * num_of_dogs_b, num_of_cats * num_of_cats_b)

print "this is the total of dogs and cats in here"
dogs_and_cats(44, 66)

print "This is trying it with more math."
dogs_and_cats(100 / 4 * num_of_dogs_b, 33 * 2 - num_of_cats_b)

# Here we had to make sure to convert the raw input from a sting to an integer. int()
print "we can even use raw input"
dogs_count = int(raw_input("Give me a number: "))
cats_count = int(raw_input("Give me a number: "))

dogs_and_cats(dogs_count, cats_count)




