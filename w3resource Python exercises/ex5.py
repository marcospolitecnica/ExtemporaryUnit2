def factorial(n): ##defines factorial string
	if n == 0: ##if n is equal to 0
		return 1 ##return 0
	else: ## else
		return n * factorial(n-1) ##returns the multiply of n times the factorial minus - 1
n=int(input("Input a number to compute the factorial :")) ##Tells the user to input a number
print(factorial(n)) ##Prints the factorial
