import sys
sys.path.insert(1, __file__[:__file__.find('Python_codes')+13]+'Some_modules')

import sieve

A = []
size = 80

with open('p082_matrix.txt') as f: #makes the matrix from the txt file.
	for line in f.readlines():
		A.append([int(t) for t in line.split(',')])

B = [[A[i][0]] + [0]*(size-1) for i in range(size)]
for j in range(1,size):
	B[0][j] = B[0][j-1] + A[0][j]
	for i in range(1,size):
		B[i][j] = min([B[i-1][j],B[i][j-1]]) + A[i][j]
	for i in range(size-2,-1,-1):
		if B[i][j] > B[i+1][j] + A[i][j]:
			B[i][j] = B[i+1][j] + A[i][j]

print(min([B[i][size-1] for i in range(size)]))



