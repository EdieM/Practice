True and True
	True 
	
False and True
	false
	
1 == 1 and 2 == 1
	true and false
		true
		
"test" == "test"
	true
	
1 == 1 or 2 != 1
	true or true
		true
		
True and 1 == 1
	true and true
		true
		
False and 0 != 0
	false and false
		false
		
True or 1 == 1
	true or true
		true
		
"test" == "testing"
	false
	
1 != 0 and 2 == 1
	true and false
		false
		
"test" != "testing"
	true
	
"test" == 1
	true?   # false
	
not (True and False)
	not(false)
		true
		
not (1 == 1 and 0 != 1)
	not (true and true)
		not(true)
			false
			
not (10 == 1 or 1000 == 1000)
	not (false or true)
		not(true)
			false
			
not (1 != 10 or 3 == 4)
	not (true or false)
		not(true)
			false
			
not ("testing" == "testing" and "Zed" == "Cool Guy")
	not(true and false)
		not false
			true
			
1 == 1 and (not ("testing" == 1 or 1 == 0))
	true and (not (true? or false)
		# true
	
"chunky" == "bacon" and (not (3 == 4 or 3 == 3))
	false and (not(false or true))
		false and (not(true))
			false and false
				false
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
	true and (not(true or false))
		true and (not true)
			true and false
				false