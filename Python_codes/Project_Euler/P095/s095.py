from Some_modules import divisors


B = 10 ** 6

longestchain = 1


for n in range(2,B+1):
	L = [n][:]
	while True:
		m = sum(divisors.divisors(L[-1]))-L[-1]
		if m == 1:
			break
		if m > B:
			break
		elif m in L:
			i = L.index(m)
			l = len(L)
			if i == l: #this means m is perfect.
				break
			else:
				chainlength = l - i + 1
				if longestchain < chainlength:
					longestchain = chainlength
					print(L[i:])
				break
		else:
			L.append(m)