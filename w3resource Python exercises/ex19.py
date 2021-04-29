def test(a): ##defines test as a
	def add(b): ##defines add as b
		nonlocal a ##nonlocal as a
		a += 1 ##a is more or equal to 1
		return a+b ##returns sum of a + b
	return add ##returns add function
func= test(4) ##function is equal to the test of 4
print(func(4)) ##prints the function of 4
