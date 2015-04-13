my_name = 'Senalka McDonald'
my_age = 31
my_height = 64 # inches
my_weight = 145 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Lets talk about %s." % my_name
print "She's %d inches tall." % my_height
print "She's %d pounds." % my_weight
print "That's not too heavy." # yes it is!
print "Her eyes are %s and her hair is %s." % (my_eyes, my_hair)
print "Her teeth are %s.....as of now, anyway" % my_teeth

# this line is tricky, try to get it exactly right
print "if I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "-------------------------"

name = 'Senalka McDonald'
age = 31
height = 64 # inches
height_cm = height * 2.54 # height converted to centimeters
weight = 145 # lbs
weight_kg = weight * 0.453592 # weight converted to kilograms
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Lets talk about %s." % name
print "She's %d inches tall." % height
print "She's %d pounds." % weight
print "That's not too heavy." # yes it is!
print "Her eyes are %s and her hair is %s." % (eyes, hair)
print "Her teeth are %s.....as of now, anyway" % teeth

# this line is tricky, try to get it exactly right
print "if I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight) 

print "If we convert to centimeters and kilograms, she weighs %d kilograms and is %d centimeters tall." % (weight_kg, height_cm)
                                                    