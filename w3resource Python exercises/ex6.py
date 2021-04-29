def test_range(n): ## defines the test_range string
	if n in range(3,9): ##if n in range 3 to 9
		print ( " %s is in the range"%str(n)) ## Prints the middle range of the item list
	else : ##else
		print("The number is outside the given range.") ##prints the error of outside range
test_range(5) ##test range automatic to 5
