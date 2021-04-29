def max_of_two (x,y): ##defines max of 2 numbers
	if x>y: ##if x is bigger than y
		return x ## return x
	return y ##else return y
def max_of_three(x,y,z):  ##define max of 3 numbers
	return max_of_two (x, max_of_two (y,z)) ##return the max of the 2 and x
print(max_of_three(3, 6, -5)) ## prints the max of 3 numbers example
