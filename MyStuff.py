# Write two functions that will convert temperatures back and forth from the Celsius and Fahrenheit temperature scales. The formulas for making the conversion are as follows:

 # Tc=(5/9)*(Tf-32)
 # Tf=(9/5)*Tc+32
# where Tc is the Celsius temperature and Tf is the Fahrenheit temperature.
# http://openbookproject.net/pybiblio/practice/wilson/tempfinder.php

print "Temperature Converter"
print '-' * 20 
print "\n\n"

	
def temp_conversion():
	temp = float(raw_input("Enter a temperature: "))
	convert_to = str(raw_input("Convert to (F)ahrenheit or (C)elcius? "))
	
	if convert_to == "F" or convert_to == "f":
		ttf = temp * 9/5 + 32
		tf = "%.2f" % ttf
		print str(temp) + "C = " + str(tf) + "F"
		
	elif convert_to == "C" or convert_to == "c":
		ttc = (temp - 32) * 5 / 9
		tc = "%.2f" % ttc
		print str(temp) + "F = " + str(tc) + "C"
	
	else:
		print "Error"
	
		
temp_conversion()
