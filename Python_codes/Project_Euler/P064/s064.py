bound = 10000

oddcount = 0

for N in range(2,bound+1):
	r = N
	s = 1
	while(r > s): #uses babylonian sqrt method to compute r = floor(sqrt(N))
		r = (r+s) // 2
		s = N // r
	if r ** 2 == N:
		continue
	a,b = 1,r
	L = [[r,a,b]]
	count = 0
	while True:
		count += 1
		k = (N - b ** 2) // a
		q = (r + b) // k
		a,b = k,q*k-b
		if [q,a,b] in L:
			ind = L.index([q,a,b])
			period = count - ind
			# print(N,period)
			break
		L.append([q,a,b])
	if period % 2 == 1:
		oddcount += 1

print(oddcount)



