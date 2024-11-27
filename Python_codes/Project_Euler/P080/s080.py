
bound = 100

supercount = 0

for D in range(2,bound+1):
	r = D
	s = 1
	while(r > s): #uses babylonian sqrt method to compute r = floor(sqrt(n))
		r = (r+s) // 2
		s = D // r
	if r ** 2 == D: #checks if D is a square and skips to the next D if this is the case
		continue
	#step1:find cont'd frac expansion by computing period
	a,b = 1,r
	L = [[r,a,b]]
	period = -1
	while True:
		period += 1
		k = (D - b ** 2) // a
		q = (r + b) // k
		a,b = k,q*k-b
		L.append([q,a,b])
		if period >= 1 and L[-1] == L[1]:
			break
	A = [L[i][0] for i in range(period + 1)] #A[0] is the first constant term of the cont frac, the rest is the repeating part.
	periodpart = A[1:]
	conv = []
	i = 0
	while True:
		if i == 0:
			conv.append([A[0],1])
		if i == 1:
			conv.append([A[0]*A[1]+1,A[1]])
		if i >= 2:
			if i >= len(A):
				A += periodpart #if more terms are needed, add another period to the sequence
			conv.append([A[i]*conv[i-1][0]+conv[i-2][0],A[i]*conv[i-1][1]+conv[i-2][1]])
		t,n = conv[i][0],conv[i][1]
		if n >= 10 ** 101: #results in fraction t/n with the same first 100 decimal digits as sqrt(D)
			break
		i += 1
	first = divmod(t,n)
	t = first[1] #chops of the digits before the .
	digits = [int(s) for s in str(first[0])]
	for _ in range(100-len(digits)):
		t *= 10
		rem = divmod(t,n)
		digits.append(rem[0])
		t = rem[1]
	print(D,sum(digits))
	supercount += sum(digits)

print(supercount)
