def unique_list(l): ##defines uniqe_list as l
	x = [] ## x equals to items in square brackets
	for a in l: ##for a in list on unique_list
		if a not in x: ##if a is not in x
			x.append(a) ##x appends to a
	return x ##returns x

print(unique_list([1,2,3,3,3,3,4,5])) ##prints the number of items with no repeated numbers
