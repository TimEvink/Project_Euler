from Some_modules import sieve


B = 5 * 10 ** 7
r = B
s = 1
while(r > s): #uses babylonian sqrt method to compute r = floor(sqrt(B))
	r = (r+s) // 2
	s = B // r

primes = sieve.sieve(r+50)


collection = set([])


i,j,k = 0,0,0
while True:
	p = primes[i]
	first = p ** 2
	if first > B:
		break
	while True:
		q = primes[j]
		temp = first + q ** 3
		if temp > B:
			break
		while True:
			r = primes[k]
			n = temp + r ** 4
			if n > B:
				break
			collection.add(n)
			k += 1
		j += 1
		k = 0
	i += 1
	j = 0

print(len(collection))

