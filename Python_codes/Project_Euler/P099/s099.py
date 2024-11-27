import os
import math

#generates absolute path to .txt file
file_path = os.path.join(os.path.dirname(__file__), 'problemfile.txt')

A = []
with open(file_path, 'r') as f:
	for line in f:
		A.append(line.strip())

B = []
for s in A:
	t = s.split(',')
	B.append([int(t[0]),int(t[1])])
j = 1
maximum = B[1]
for i in range(1,1000):
	a = B[i][0]
	b = B[i][1]
	if b * math.log(a) > maximum[1] * math.log(maximum[0]):
		print(i)
		maximum = B[i] 
