# Write a method that will take in a number of minutes, and returns a
# string that formats the number into `hours:minutes`.
#
# Difficulty: easy.

minutes = float(raw_input("Tell me how many minutes to convert into hours: "))

def time_conversion(minutes):
    h, m = divmod(minutes, 60)
    print "%d:%02d" % (h, m)
	
time_conversion(minutes)

print 'time_conversion(15) == "0:15": ' + str(time_conversion(15) == '0:15')
print 'time_conversion(150) == "2:30": ' + str(time_conversion(150) == '2:30')
print 'time_conversion(360) == "6:00": ' + str(time_conversion(360) == '6:00')