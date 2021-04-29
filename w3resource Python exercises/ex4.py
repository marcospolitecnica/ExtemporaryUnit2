def reverse (str):
	rstring = ''
	string = len(str)
	while string > 0:
		rstring += str[string - 1]
		string = string -1
	return rstring
print(reverse('1234abcd'))
