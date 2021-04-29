def reverse (str): ##defines the reverse string
	rstring = '' ##reverse string is nothing for now
	string = len(str) ##string is the lenght of the string
	while string > 0: ##while the string is more than 0
		rstring += str[string - 1] ##rstring is more or equal to string[string minus 1]
		string = string -1 ##string is defined by string minus 1
	return rstring ##returns the rstring value
print(reverse('1234abcd')) ##prints the reverse example
