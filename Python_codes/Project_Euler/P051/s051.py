from Some_modules import sieve
from Some_modules import sublistsofsize


primeset = sieve.sieve(1000000)
goal = 8
for starnumber in list(range(2,5)):
	firstprimecandidates = []
	for p in primeset:
		s = str(p)
		l = len(s)
		if starnumber > l:
			continue
		else:
			for d in ['0','1','2']:
				t = list(s)
				t.pop()
				if t.count(d) >= starnumber:
					firstprimecandidates.append(p)
					break

	for p in firstprimecandidates:
		s=str(p)
		l=len(s)
		for d in [0,1,2]:
			indices = []
			for j in range(l): # indices becomes the list of indices for which s[j]=d
				if s[j] == str(d):
					indices.append(j)
			for sub in sublistsofsize.sublists(indices,starnumber): 
				if sub[0] == 0 and d == 0:
					count = 1
				else:
					count = 0
				count += d
				for k in range(d+1,10):
					t = list(s)
					for j in sub:
						t[j] = str(k)
					w = int(''.join(t))
					if (w % 2) == 0 or (w % 3) == 0 or (w % 5) == 0 or (w % 7) == 0 or not(w in primeset):
						count += 1
					if count == 3:
						break
				else:
					print(p,d,sub)
