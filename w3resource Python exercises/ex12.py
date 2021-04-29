def isPalindrome(string): #defines isPalindrom as string
	left_pos = 0 ##left position is 0
	right_pos = len(string) - 1 ##right position is lenght of string - 1

	while right_pos >= left_pos: ##while the right pos is more or equal to the left position
		if not string[left_pos] == string[right_pos]: ##if string in left position is not equal to string in right position
			return False ##return False
		left_pos += 1 ##left position is more or equal to 1
		right_pos -= 1 ##right position is less or equal to 1
	return True ##Return True
print(isPalindrome('aza')) ##prints the test to aza
