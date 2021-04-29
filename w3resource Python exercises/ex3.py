def multi (numbers): ##defines multplication of numbers
	total = 1 ##total must be 1
	for x in numbers: ##for x in the string of numbers
		total *= x ##total must be x
	return total ##returns the total string
print (multi((8, 2, 3, -1, 7))) ##prints the total of the example numbers
