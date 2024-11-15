#first step: create candidates of the form [[digits 0-9 without a and b],[10,a,b]]
candlist = []
for a in range(1,10):
	for b in range(1,10):
		if a != b:
			digits = list(range(1,10))
			digits.remove(a)
			digits.remove(b)
			candlist.append([digits,[10,a,b]])

#2nd step: repeat the following 3 times: check for each candidate how it can be extended 

for step in range(1,4):
	newlist = []
	for cand in candlist:
		digits = cand[0]
		recenttriple = cand[step]
		total = sum(recenttriple)
		for d in digits:
			e = total - d - recenttriple[2]
			if e != d and e in digits:
				newdigits = digits[:]
				newdigits.remove(d)
				newdigits.remove(e)
				newcand = [newdigits] + cand[1:]
				newcand.append([d,recenttriple[2],e])
				newlist.append(newcand)
	candlist = newlist
print(candlist)
#3rd step : check if the remaining digit makes it fit!

solutions = []

for cand in candlist:
	lasttriple = [cand[0][0], cand[4][2], cand[1][1]]
	if sum(cand[1]) == sum(lasttriple):
		sol = cand
		sol.pop(0)
		sol.append(lasttriple)
		solutions.append(sol)
for sol in solutions:
	print(sol)