from Some_modules import sublistsofsize


def reduce(q): #input is a rational number q, stored as tuple q=(numerator,denominator). Output reduces the fraction uniquely in a form q=t/n for t>0 and gcd(t,n)=1
	if q[1] == 0:
		return (0,0)
	else:
		r = q[0]
		s = q[1]
		while s != 0:
			s,r = r % s,s
		if q[1] < 0:
			sign = -1
		else:
			sign = 1
		return (sign * q[0] // r,sign *q[1] // r)
def add(q,r): #does the operations on rational numbers, where t/n is stored as the tuple (t,n).
	return reduce((r[1]*q[0]+r[0]*q[1],q[1]*r[1]))
def diff(q,r):
	return reduce((r[1]*q[0]-r[0]*q[1],q[1]*r[1]))
def mul(q,r):
	return reduce((q[0]*r[0],q[1]*r[1]))
def quo(q,r):
	return reduce((q[0]*r[1],q[1]*r[0]))

record = 0

for digits in sublistsofsize.sublists(list(range(0,10)),4):
	A = set([])
	for func0 in [add,diff,mul,quo]:
		for func1 in [add,diff,mul,quo]:
			for func2 in [add,diff,mul,quo]:
				for numbers in sublistsofsize.permutations(digits):
					a = func0((numbers[0],1),(numbers[1],1))
					if a[1] != 0:
						b = func1(a,(numbers[2],1))
						if b[1] != 0:
							c = func2(b,(numbers[3],1))
							if c[1] == 1 and c[0] > 0:
								A.add(c[0])
						b = func1((numbers[2],1),(numbers[3],1))
						if b[1] != 0:
							c = func2(a,b)
							if c[1] == 1 and c[0] > 0:
								A.add(c[0])

	if 1 in A:
		k = 0
		while True:
			k += 1
			if not k in A:
				break
		if k > record:
			print(digits,k-1)
			record = k








