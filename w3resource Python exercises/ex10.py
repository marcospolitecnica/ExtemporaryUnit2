def is_even_num(l): ##defines is_even_num in a list
	enum = [] ##enum equals to the list in square brackets
	for n in l: ##for n in l as list
		if n% 2 == 0: ##if division residual is 0
			enum.append(n) ##appends the enum in n
	return enum ##returns enum

print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9])) ##prints the even numbers as list
