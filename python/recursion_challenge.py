def factorial(x):
	if x == 1:
		return x
	else:
		return x * factorial(x - 1)

#print(factorial(7)) # Equals 5040

def palindrome(string):
	if len(string) <= 1:		# empty string and single letter are palindromes
		return True
	if string[0] != string[len(string) - 1]:  # first and last letters don't match
		return False
	return palindrome(string[1:-1])

	

print(palindrome('abcba'))	

def bottles(num):
	pass

def roman_num(num):
	pass