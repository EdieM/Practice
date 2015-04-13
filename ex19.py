# this up here is just defining the function; giving it a thing to do
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# print this info, where 20 is the cheese_count and 30 is the boxes_of_crackers	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


# here just adding one (unnecessary) step. 
# (amount_of_cheese, amount_of_crackers) are defined as 10 and 50, and 
# (amount_of_cheese, amount_of_crackers) is just stand in for (cheese_count, boxes_of_crackers)
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50


cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# (10 + 20, 5 + 6) stand ins for (cheese_count, boxes_of_crackers)
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# using the variables defined earlier
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


