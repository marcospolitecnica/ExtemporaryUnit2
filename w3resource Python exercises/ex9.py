def test_prime(n): ##defines te test_prime string to n
	if (n==1): ##if n equals to one
		return False ##Return false
	elif (n==2): ##else if n equals to 2
		return True ##Return True
	else: #else
		for x in range(2,n): ##for every x in range 2 to n
			if(n % x==0): ##if n division residual is 0
				return False ##Return false
		return True ##Else return True
print (test_prime(9)) ##Prints the test prime as 9
