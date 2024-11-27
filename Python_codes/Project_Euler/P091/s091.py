bound = 50

options1 = [(i,j) for i in range(1,bound + 1) for j in range(1,bound + 1)]
options2 = [(i,j) for i in range(0,bound + 1) for j in range(0,bound + 1)]

count1 = 0
triags = []

for P in options2:
	if P == (0,0):
		continue
	for Q in options2: #we make the line ortogonal to the line connecting P and O, and check if Q is on the line
		if Q == (0,0) or P == Q:
			continue
		if P[1] * (Q[1] - P[1]) + P[0] * (Q[0] - P[0]) == 0:
			count1 += 1
			triags.append([P,Q])


print(count1+bound ** 2)