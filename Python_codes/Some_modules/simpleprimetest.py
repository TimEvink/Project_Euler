def primetest(n): #tests if an integer is prime. Negative integers return False
	assert type(n) == int, "input should be an integer"
	if n == 2 or n == 3 or n == 5:
		return True
	if n <= 1 or (not n & 1) or n % 3 == 0 or n % 5 == 0:
		return False
	r,s = n,1
	while r > s: #uses babylonian sqrt method to compute r = floor(sqrt(n))
		r = (r+s) // 2
		s = n // r
	for k in [7,11,13,17,19,23,29,31]:
		for d in range(k,r+1,30):
			if n % d == 0:
				return False
	return True


for k in range(10 ** 7):
	primetest(k)