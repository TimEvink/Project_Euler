import sys
sys.path.insert(1, __file__[:__file__.find('Python_codes')+13]+'Some_modules')

with open('0083_matrix.txt', 'r') as f:
	s = f.readlines()

A = []
for _ in range(80):
	A.append([])

for i in range(80):
	L = s[i].split(",")
	L[-1] = L[-1][:-1]
	for j in range(80):
		A[i].append(int(L[j]))

def neighbors(i,j):
	if i == 0 and j == 0:
		return [(0,1),(1,0)]
	if i == 0 and j == 79:
		return [(0,78),(1,79)]
	if i == 79 and j == 0:
		return [(78,0),(79,1)]
	if i == 79 and j == 79: 
		return [(78,79),(79,78)]
	#all 4 corners are now covered. Next are the edges
	if i == 0:
		return [(0,j-1),(1,j),(0,j+1)]
	if i == 79:
		return [(79,j-1),(78,j),(79,j+1)]
	if j == 0:
		return [(i-1,0),(i,1),(i+1,0)]
	if j == 79:
		return [(i-1,79),(i,78),(i+1,79)]
	# now only interior options remain
	return [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]

positions = [(i,j) for i in range(80) for j in range(80)]
candidates = [(0,0)]
marked = []

distances = {(0,0):A[0][0]}

while not candidates == []:
	mindis = min([distances[u] for u in candidates].copy())
	for u in candidates:
		if distances[u] == mindis:
			currentnode = u
			break
	candidates.remove(currentnode)
	marked.append(currentnode)
	for x in neighbors(currentnode[0],currentnode[1]):
		if x in marked:
			continue
		if not x in distances.keys(): #means no path to x is yet there
			distances[x] = mindis + A[x[0]][x[1]]
			candidates.append(x)
		elif mindis + A[x[0]][x[1]] < distances[x]:
			distances[x] = mindis + A[x[0]][x[1]]
	

print(distances[(79,79)])

