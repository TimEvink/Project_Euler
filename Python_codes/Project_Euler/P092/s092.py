B = 10 ** 7

count = 0

for n in range(1,B):
	m = n
	while True:
		m = sum([int(d) ** 2 for d in str(m)])
		if m == 1:
			break
		elif m == 89:
			count += 1
			break

print(count)