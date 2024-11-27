from Some_modules import sieve


def primepartitions(bound): #returns list L of length bound with L[i] the number of ways i can be written as a sum of primes.
	primes = sieve.sieve(bound)
	r = len(primes)
	def auxrec(s): #builds an auxiliary recursive function after calling the prime sieve, auxrec(r) determines a list L[i] using only the first r primes.
		if s == 1:
			L = [0] + [0,1] * ((bound-1) // 2)
			if bound % 2 == 0:
				L.append(0)
			return L
		else:
			p = primes[s-1] #p is the s'th prime.
			A = auxrec(s-1)
			B = []
			for n in range(bound):
				k = 1
				count = 0
				while k * p <= n:
					count += A[n - k * p]
					k += 1
				B.append(count+A[n])
			for k in range(p,bound,p):
				B[k] += 1
			return B
	return auxrec(r)

A = primepartitions(100)
print(A)

for i in range(len(A)):
	if A[i] > 5000:
		print(i)
		break