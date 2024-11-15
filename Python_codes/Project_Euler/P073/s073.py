def gcd(a,b):
	if a < b:
		a,b = b,a
	r = a
	s = b
	while s != 0:
		s,r = r % s,s
	return r

B = 12000

count = -2

for d in range(2,B+1):
	lower = d // 3
	upper = d // 2
	if d % 3 != 0:
		lower += 1
	for n in range(lower,upper+1):
		if gcd(d,n) == 1:
			count += 1
print(count)