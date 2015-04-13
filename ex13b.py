from sys import argv

script, first, second, third, fourth, fifth = argv

print raw_input("How do you unpack an argument? "), script
print "jump all over that.", first
print "if i don't type it...", second
print "just another extra.", third
print raw_input("script that takes arguments vs function that takes arguments? "), fourth
print "study drills", fifth

# 'script' ends up being what i entered into cmd line as raw_input

