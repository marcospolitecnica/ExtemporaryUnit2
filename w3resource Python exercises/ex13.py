def pascal_triangle(n): ##defines the pascal_triangle as n
	trow = [1] ##trow is equal to 1 as item list
	y = [0] ##y is equal to 0 as item list
	for x in range(max(n,0)): ##for x in range of max of n to 0
		print(trow) ##print trow
		trow=[l+r for l,r in zip(trow+y, y+trow)] ##trow is equal to l + r for l, r in zip of trow + y and y + trow
	return n>=1 ##return n is more or equal to 1
pascal_triangle(6) ##test pascal triangle in 6
