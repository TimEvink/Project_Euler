import sys
sys.path.insert(1, __file__[:__file__.find('Python_codes')+13]+'Some_modules')

import contfrac

# B = 1 
# T = 1 
# D = 0

# while True:
# 	if D <= 0:
# 		if D == 0:
# 			print(B,T)
# 		D += 2*B
# 		B += 1
# 	else:
# 		D -= T
# 		T += 1

N = 8

# r = N
# s = 1
# while(r > s): #uses babylonian sqrt method to compute r = floor(sqrt(N))
# 	r = (r+s) // 2
# 	s = N // r
# a,b = 1,r
# L = [[r,a,b]]
# count = 0
# while True:
# 	count += 1
# 	k = (N - b ** 2) // a
# 	q = (r + b) // k
# 	a,b = k,q*k-b
# 	if a ** 2 - N * b ** 2 == 1:
# 		print(a,b)
# 	if count > 100000000:
# 		break

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
			







