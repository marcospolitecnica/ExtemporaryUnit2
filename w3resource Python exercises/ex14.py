import string, sys ##imports library of string and sys
def ispangram(str1, alphabet=string.ascii_lowercase): ##defines ispangram as str1 and alphabet
	alphaset = set(alphabet) ##alphaset is equal to the set of alphabet
	return alphaset <= set(str1.lower()) ##returns alphaset is less or equal to set in str1 lower

print(ispangram('The quick brown fox jumps over the lazy dog')) ##Test string with The quick brown fox jumps over the lazy dog
