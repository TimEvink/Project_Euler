from Some_modules import sublistsofsize

polies = {k:[] for k in range(3,9)}

for s in range(3,9):
	poly = 0
	i = 0
	while True:
		poly += (s-2)* i + 1
		l = len(str(poly))
		if l == 4:
			polies[s].append(poly)
		if l > 4:
			break
		i += 1

array = {}
for d in range(10,100):
	for s in range(3,9):
		for poly in polies[s]:
			if str(d) == str(poly)[:2]:
				if (d,s) in array:
					array[(d,s)].append(poly)
				else:
					array[(d,s)] = [poly]


for L in sublistsofsize.permutations([4,5,6,7,8]): #we take triangle numbers as starting point and loop over all possible other orders in which the other poly numbers occur
	current = [[n] for n in polies[3]]
	for i in range(5):
		B = []
		for prev in current:
			teststr = str(prev[-1])[2:]
			if teststr[0] == '0':
				continue
			testint = int(teststr)
			if (testint,L[i]) in array:
				for newcand in array[(testint,L[i])]:
					B.append(prev + [newcand])
		current = B
	for cand in current:
		if str(cand[0])[:2] == str(cand[5])[2:]:
			print(L,cand)
			print(sum(cand))







# print(polies[3])

# digitoptions = {k:[] for k in range(10,100)}
# digitoptionsred = {k:[] for k in range(10,100)}
# for k in range(10,100):
# 	for s in range(3,9):
# 		for a in polies[s]:
# 			if str(k) == str(a)[:2]:
# 				digitoptions[k].append([a,s])
# 				digitoptionsred[k].append(a)

# print(digitoptions[13])
# print(digitoptionsred[13])


# for a in range(10,100):
# 	for b in range(10,100):
# 		for c in range(10,100):
# 			ar = int(str(a)+str(b))
# 			br = int(str(b)+str(c))
# 			cr = int(str(c)+str(a))
