def multi (numbers):
	total = 1
	for x in numbers:
		total *= x
	return total
print (multi((8, 2, 3, -1, 7)))
