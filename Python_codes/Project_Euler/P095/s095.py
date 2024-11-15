import sys
sys.path.insert(1, __file__[:__file__.find('Python_codes')+13]+'Some_modules')

import divisors
import sieve


B = 10 ** 6

longestchain = 1 #the divisor function was altered for this to return the sum of proper divisors in stead. Not up to date!

for n in range(2,B+1):
	L = [n][:]
	while True:
		m = divisors.divisors(L[-1])
		if m == 1:
			break
		if m > B:
			break
		elif m in L:
			i = L.index(m)
			l = len(L)
			if i == l: #this means m is perfect.
				break
			else:
				chainlength = l - i + 1
				if longestchain < chainlength:
					longestchain = chainlength
					print(L[i:])
				break
		else:
			L.append(m)

