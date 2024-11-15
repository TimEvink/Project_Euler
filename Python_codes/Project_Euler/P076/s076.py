
B = 100

pents = [0]
cur = 0
for k in range(B): #construct list of the the first B pentagonal numbers, pents[i] is the ith one and pents[0] = 0.
	cur += 3*k+1
	pents.append(cur)

print(pents)
partitions = [1]

for n in range(1,B+1):
	A = []
	k = 1
	sign = 1
	while True:
		if pents[k] + k <= n:
			diff = n - pents[k]
			A.append(sign * partitions[diff])
			A.append(sign * partitions[diff - k])
			k += 1
			sign *= -1
		elif pents[k] <= n:
			A.append(sign * partitions[n - pents[k]])
			break
		else:
			break
	partitions.append(sum(A))

for d in [5,100]:
	print(partitions[d])


