from Some_modules import sieve
from Some_modules import simpleprimetest


# is quite inefficient and takes 5 minutes or so.
# obvious improvent would be to use a sieve to generate the primes up to some bound and use binary search to check if the various concatenations are primes, in stead of invoking a rather naive prime test.

bound1 = 100
bound2 = 10 ** 4
bound3 = 2 * (10 ** 4)
bound4 = 2 * (10 ** 4)
bound5 = 3 * (10 ** 4)

tot = 34427

Primes = sieve.sieve(bound5)
print(len(Primes))
index1 = 0
index2 = 0
index3 = 0
index4 = 0 
while True:
	if Primes[index1+1] <= bound1:
		index1 += 1
	else:
		break
while True:
	if Primes[index2+1] <= bound2:
		index2 += 1
	else:
		break
while True:
	if Primes[index3+1] <= bound3:
		index3 += 1
	else:
		break # finds indices indexi such that P[indexi] is the largest prime <= boundi
while True:
	if Primes[index4+1] <= bound4:
		index4 += 1
	else:
		break

cands = []

for p in Primes[:index1]: #makes list cands of triples T=[p,q,r] with p<q<r that form a 3 prime set, with T[i] <= boundi
	for q in Primes[Primes.index(p)+1:index2]:
		for r in Primes[Primes.index(q)+1:index3]:
			L = [p,q,r]
			for I in [[0,1],[1,0],[0,2],[2,0],[1,2],[2,1]]:
				if not simpleprimetest.primetest(int(str(L[I[0]])+str(L[I[1]]))):
					break
			else:
				cands.append([p,q,r])
print(cands)
cands2 = []
for L in cands:
	for p in Primes[Primes.index(L[2])+1:index4]:
		if sum(L) + p > tot:
			break
		for l in L:
			if not simpleprimetest.primetest(int(str(l)+str(p))) or not simpleprimetest.primetest(int(str(p)+str(l))):
				break
		else:
			cands2.append(L+[p])
print(cands2)
cands3 = []
for L in cands2:
	for p in Primes[Primes.index(L[3])+1:]:
		if sum(L) + p > tot:
			break
		for l in L:
			if not simpleprimetest.primetest(int(str(l)+str(p))) or not simpleprimetest.primetest(int(str(p)+str(l))):
				break
		else:
			cands3.append(L+[p])
for L in cands3:
	print(L,sum(L))








# # bound1 = 2 * (10 ** 2)
# # bound2 = 10 ** 7

# Primes = sieve.sieve(bound2)

# for _ in range(4):
# 	Primes.pop(0)

# cands = []
# relevantprimes = []

# for p in Primes:
# 	s = str(p)
# 	for k in range(1,len(s)):
# 		if s[k-1] in ['0','2','4','6','8'] or s[k] == '0':
# 			continue
# 		else:
# 			if simpleprimetest.primetest(int(s[:k])) == True and simpleprimetest.primetest(int(s[k:])) == True:
# 				cands.append([int(s[:k]),int(s[k:])])
# 				if int(s[:k]) in relevantprimes:
# 					continue
# 				else:
# 					relevantprimes.append(int(s[:k]))

# cands2 = [] 
# for L in cands: # forms list with members [p,q], p < q primes, st the concatenations pq and qp are prime.
# 	if L[0] < L[1] and L[::-1] in cands:
# 		cands2.append(L)
# cands2=sorted(cands2)
# print(relevantprimes)

# currentgroups = [] #=cands2

# for L in cands2:
# 	if L[0] <= bound1 and L[1] <= bound1:
# 		currentgroups.append(L)

# print(currentgroups)
# for _ in range(3):
# 	auxgroup = []
# 	for r in relevantprimes:
# 		for L in currentgroups:
# 			if r <= L[-1]:
# 				continue
# 			for p in L:
# 				if not [p,r] in cands2:
# 					break
# 			else:
# 				A = L[:]
# 				A.append(r)
# 				auxgroup.append(A)
# 	currentgroups = auxgroup
# 	print(currentgroups)


