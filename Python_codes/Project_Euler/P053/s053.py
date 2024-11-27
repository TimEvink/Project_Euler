B = 10 ** 6
M = 101

count = 0

A = []
for _ in range(M):
	A.append([1])
for n in range(1,M):
	for k in range(1,n):
		v = A[n-1][k] + A[n-1][k-1]
		if v > B:
			count += 1
		A[n].append(v)
	A[n].append(1)
print(count)
