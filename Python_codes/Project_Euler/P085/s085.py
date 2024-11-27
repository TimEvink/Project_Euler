n = 3
m = 2

val = 10 ** 4
print(sum([(n-a)*(m-b) for a in range(n) for b in range(m)]))

for n in range(100):
	for m in range(n+1):
		S = sum([(n-a)*(m-b) for a in range(n) for b in range(m)])
		if 199 * 10 ** 4 < S < 201 * 10 ** 4:
			if abs(S-2000000) < val:
				cur = (n,m)
				val = abs(S-2000000)
				print(n,m,n*m,S)