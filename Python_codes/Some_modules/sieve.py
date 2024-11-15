def sieve(n): #performs a sieve of Eratosthenes and produces list of primes up to n.
	assert type(n) == int, "input should be an integer"
	if n <= 1:
		return []
	r,s = n,1
	while (r > s): #uses babylonian sqrt method to compute r = floor(sqrt(n))
		r = (r+s) // 2
		s = n // r
	limit = (n-1) // 2
	rootlim = (r-1) // 2 + 1
	cands = [0]+[1 for _ in range(limit)]
	for i in range(1,rootlim):
		if cands[i] == 1:
			for k in range(2*i*(i+1),limit+1,2*i+1):
				cands[k] = 0
	return [2]+[2*i+1 for i in range(limit+1) if cands[i] == 1]