import sys
sys.path.insert(1, __file__[:__file__.find('Python_codes')+13]+'Some_modules')

import contfrac


bound = 10 ** 3

L = [1]

for _ in range(bound):
	L += [1,2]

conv = contfrac.convergents(L)

perimcount = 0

for q in conv:
	t = q[0]
	n = q[1]
	if t ** 2 == 1 + 3 * n ** 2:
		if (2 * t) % 3 == 2:
			a = (2 * t + 1) // 3
			perim = 3 * a + 1
		else:
			a = (2 * t - 1) // 3
			if not a == 1:
				perim = 3 * a - 1
			else:
				perim = 0
		if perim < 10 ** 9:
			print(a,perim)
			perimcount += perim

print(perimcount)