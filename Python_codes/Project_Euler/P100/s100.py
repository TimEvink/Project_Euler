from Some_modules import contfrac


N = 8

bound = 10 ** 3

L = [1]

for _ in range(bound):
	L += [2]

conv = contfrac.convergents(L)

for q in conv:
	x = q[0]
	y = q[1]
	if x % 2 == 1 and y % 2 == 1:
		if x ** 2 - 2 * y ** 2 == -1:
			T = (1 + x) // 2
			B = (1 + y) // 2
			if T > 10 ** 12:
				print(B)