def MillerRabin(n,b):
	if not n & 1: #checks if n is even by checking if last binary digit is 0 or 1. condition met means n is even
		if n == 2:
			return True
		return False
	if n == 1:
		return False
	s = 0
	t = n-1
	while not t & 1:#finds decomposition n-1=2^s*t with t odd
		t //= 2
		s += 1
	c = pow(b,t,n)
	if c == 1 or c == n-1:
		return True
	for _ in range(s-1):
		c **= 2
		c %= n
		if c == n-1:
			return True
	return False

