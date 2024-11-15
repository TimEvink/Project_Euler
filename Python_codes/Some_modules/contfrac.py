def convergents(L): # input a list [a_0: a_1,...a_n] of length n+1, outputs the list of convergents, where each convergent is a list of the form [numerator,denominator]
	k = len(L)
	if k == 0:
		return []
	if k == 1:
		return [[L[0],1]]
	else:
		conv = [[L[0],1],[L[0]*L[1]+1,L[1]]]
		for i in range(2,k):
			conv.append([L[i]*conv[i-1][0]+conv[i-2][0],L[i]*conv[i-1][1]+conv[i-2][1]])
		return conv