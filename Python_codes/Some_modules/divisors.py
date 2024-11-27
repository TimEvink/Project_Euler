def factor(n): #gives the factorisation of n in the form of a list of lists of the form [p,valuation of n at p]
	# first pull out all the factors 2 and 3 manually.
	m = n
	k2, k3 = 0, 0
	facs = []
	while m % 2 == 0:
		k2 += 1
		m //= 2
	if k2 != 0:
		facs.append([2,k2])
	while m % 3 == 0: 
		k3 += 1
		m //= 3
	if k3 != 0:
		facs.append([3,k3])
	# here n=2^{k_2}* 3^{k_3} *m, with m not divisible by 2 and 3.
	k = 5
	while m != 1:
		r = m
		s = 1
		while(r > s): #after loop, r = floor(sqrt(m))
			r = (r+s) // 2
			s = m // r
		for d in range(k,r+1,6):
			for i in [0,2]:
				if m % (d + i) == 0: #if a factor is found, it must be prime. Looks for corresponding valuation.
					p = d + i
					m //= p
					kp = 1
					while m % p == 0:
						kp += 1
						m //= p
					facs.append([p,kp][:])
					k = d
					break
			else:
				continue
			break
		else: # being here means no factor is found up to sqrt(m), hence m itself must be prime
			facs.append([m,1][:])
			return facs
	return facs

def divisors(n): #using the prime factorisation of n we can list all the divisors.
	D = [1]
	F = factor(n)
	for i in range(len(F)):
		E = D[:]
		for k in range(1,F[i][1]+1):
			for d in E:
				D.append(d * F[i][0] ** k)
	return sorted(D)


for n in range(1,10 ** 6):
	factor(n)