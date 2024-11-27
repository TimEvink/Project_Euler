array = {}

bound = 1500000

n = 1
while True:
	if 2*(n+1)*(2*n+1) > bound:
		break
	m = n + 1
	while True:
		per = 2*m*(m+n)
		if per > bound:
			break
		a = m ** 2 - n ** 2
		b = 2 * m * n
		c = m ** 2 + n ** 2
		s = 1
		while True:
			if s * per > bound:
				break
			triangle = sorted([s*a,s*b,s*c])
			newper = s * per
			if not newper in array:
				array[newper] = []
			if not triangle in array[newper]:
				array[newper].append(triangle)
			s += 1
		m += 1
	n += 1

count = 0

for d in array:
	if len(array[d]) == 1:
		count += 1

print(count)