print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do? <----it printed the period 10 times!

# all of this below is just naming each string.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "b"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens. with the comma, it prints Cheese burger on one line
# without the comma, it prints Cheese burger on two lines.
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# why did he put these last bits on two lines? because (apparently) it is bad style to 
# make any lines longer than 80 characters.
# how could i remove the space between cheese and burger though?