def string_test(s): ##defines string_test
	d={"UPPER_CASE":0, "LOWER_CASE":0} ##detection of uppercase and lowercase letters
	for c in s: ##for c in s defined in string_test
		if c.isupper(): ##if c is uppercase
			d["UPPER_CASE"]+=1 ##detects uppercase plus or equal to 1
		elif c.islower(): ##else if c is lowercase
			d["LOWER_CASE"]+=1 ##detects lowercase plus or equal to 1
		else: ##else
			pass ##do nothing
	print ("Original String : ", s) ##Prints the original string
	print ("No. of Upper case characters : ", d["UPPER_CASE"]) ##Prints the total of uppercase letters
	print ("No. of Lower case characters : ", d["LOWER_CASE"]) ##Prints the total of lowercase letters

string_test('The quick Brown Fox') ##Uses the string_test to The quick Brown Fox.

