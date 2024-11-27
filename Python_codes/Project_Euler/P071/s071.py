maximum = 1

def gcd(a,b):
	if a == 0 or b == 0:
		return 0
	if a < b:
		a,b = b,a
	r = a
	s = b
	while s != 0:
		s,r = r % s,s
	return r

B = 10 ** 6

curmax = (0,1)
print(curmax)

for d in range(2,B+1):
	n = 3 * d // 7
	if 7 * n == 3 * d:
		n += -1
	if n > 0:
		while True:
			if gcd(d,n) == 1:
				if curmax[0] * d < curmax[1] * n:
					curmax = (n,d)
				break
			else:
				n += -1
print(curmax)