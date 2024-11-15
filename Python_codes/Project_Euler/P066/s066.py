import sys
sys.path.insert(1, __file__[:__file__.find('Python_codes')+13]+'Some_modules')

import contfrac

bound = 1000

maximum = 0

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
	# print(D,A,period)
	#step2:compute convergents until Pells equation is hit up to sign. 
	# conv = [[A[0],1],[A[0]*A[1]+1,A[1]]]
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
		x,y = conv[i][0],conv[i][1]
		val = x ** 2 - D * y **2
		if val == 1:
			if x > maximum:
				maximum = x
				print(D,x)
			break
		i += 1




