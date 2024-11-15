#input is a sorted list L and a potential element x.
#output is True if x in L, and False otherwise

def binarysearch(L,x):
	if L == [] or x < L[0] or L[-1] < x:
		return False
	n = len(L)
	k = n.bit_length()
	t = 0
	for i in range(k):
		if t + 2 ** (k-1-i) >= n: #means suggested increment of t exceeds index values of L
			continue
		if L[t + 2 ** (k-1-i)] == x:
			return True
		if L[t + 2 ** (k-1-i)] < x:
			t += 2 ** (k-1-i)
	return False