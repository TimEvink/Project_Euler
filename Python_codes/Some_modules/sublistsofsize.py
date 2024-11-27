def sublists(L,k): # L is a list, k a positive integer. Outputs list of all sublists of L of size k.	
	n = len(L)
	if k <= 0 or k > n:
		return []
	if k == 1:
		return [[x] for x in L]
	curindex = list(range(k))
	sub = L[:k]
	sublists = [L[:k]]
	while True:
		if curindex[0] + k == n:
			break
		if curindex[-1] + 1 == n:
			j = k - 1
			while True:
				j += -1
				if curindex[j+1] >= 2 + curindex[j]:
					break
			v = curindex[j] + 1
			sub = sub[:j]
			for l in range(k-j):
				temp = v + l
				curindex[j+l] = temp
				sub.append(L[temp])
		else:
			curindex[-1] += 1
			sub[-1] = L[curindex[-1]]
		sublists.append(sub[:])
	return sublists


def permutations(L): #returns list of all permutations of the list L, so a list of length(L)! elements
	length = len(L)
	if length == 1:
		return [[L[0]]]
	else:
		last = L[-1]
		return [sub[:i]+[last]+sub[i:] for sub in permutations(L[:length - 1]) for i in range(length)]