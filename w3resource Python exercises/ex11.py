def perfect_number(n): ##defines perfect number in n
	sum = 0 ##sum is 0
	for x in range(1, n): ##for x in range from 1 to n
		if n% x == 0: ##if n division residual is 0
			sum += x ##sum is more or equal to x
	return sum == n ##return the sum is equal to n
print(perfect_number(6)) ##prints the test number six
