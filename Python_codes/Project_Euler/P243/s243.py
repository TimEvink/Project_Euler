import sys
sys.path.insert(1, __file__[:__file__.find('Python_codes')+13]+'Some_modules')

import divisors
import simpleprimetest


def eulerphi(n):
	F = divisors.factor(n)
	prod = 1
	for d in F:
		prod *= (d[0] - 1) * d[0] ** (d[1] - 1)
	return prod

n = 0
mil = 1
while True:
	n += 2
	F = divisors.factor(n)
	prod = 1
	for d in F:
		prod *= (d[0] - 1) * d[0] ** (d[1] - 1)
	if 6 * prod < n-1:
		if 94744 * prod < (n-1) * 15499:
			print(n)
			break
