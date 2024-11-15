import copy

def deduction(A): #inputs a suduko in array form, outputs a new sudoku based on deduction and a true/false. false means a contradiction was found, so the sudoku wasn't valid.
	while True:
		for i in range(9):
			for j in range(9):
				if A[i][j] == 0:
					digits = list(range(1,10))
					rowquo, columnquo = i // 3, j // 3
					for r in range(3): #exclude the digits in the same 3x3 subblock
						for s in range(3):
							k = A[3 * rowquo + r][3 * columnquo + s]
							if k in digits:
								digits.remove(k)
					for k in range(9): #exclude the digits in the same row 
						if A[i][k] in digits:
							digits.remove(A[i][k])
					for k in range(9): #exclude the digits in the same column
						if A[k][j] in digits:
							digits.remove(A[k][j])
					if len(digits) == 1:
						A[i][j] = digits[0]
						break
					if digits == []:
						return A, False
			else:
				continue
			break
		else:
			break
	return A, True

A = [[0,0,3,0,2,0,6,0,0],[9,0,0,3,0,5,0,0,1],[0,0,1,8,0,6,4,0,0],[0,0,8,1,0,2,9,0,0],[7,0,0,0,0,0,0,0,8],[0,0,6,7,0,8,2,0,0],[0,0,2,6,0,9,5,0,0],[8,0,0,2,0,3,0,0,9],[0,0,5,0,1,0,3,0,0]];

def solver(A):
	Adeduc,_ = deduction(A)
	for i in range(9):
		if 0 in Adeduc[i]:
			break
	else:
		return Adeduc,0
	bigguesslist = [Adeduc]
	count = 0
	while True:
		curA = bigguesslist.pop(0)
		lowest = 10
		for i in range(9):
			for j in range(9):
				if curA[i][j] == 0:
					digits = list(range(1,10))
					rowquo, columnquo = i // 3, j // 3
					for r in range(3): #exclude the digits in the same 3x3 subblock
						for s in range(3):
							k = curA[3 * rowquo + r][3 * columnquo + s]
							if k in digits:
								digits.remove(k)
					for k in range(9): #exclude the digits in the same row 
						if curA[i][k] in digits:
							digits.remove(curA[i][k])
					for k in range(9): #exclude the digits in the same column
						if curA[k][j] in digits:
							digits.remove(curA[k][j])
					if len(digits) == 2:
						i0,j0 = i,j
						lowest = 2
						guesscands = digits
						break
					if len(digits) < lowest:
						i0,j0 = i,j
						lowest = len(digits)
						guesscands = digits
			else:
				continue
			break
		for d in guesscands:
			guess = copy.deepcopy(curA)
			guess[i0][j0] = d
			guessded, flag = deduction(guess)
			count += 1
			if flag == True:
				for i in range(9): #if valid, check if its actually solved
					if 0 in guessded[i]:
						bigguesslist.append(copy.deepcopy(guessded)) #if not solved, add to list of guesses.
						break
				else:
					return guessded,count


S = 0
A = []

with open('p096_sudoku_hard.txt') as f: #makes the matrix from the txt file.
	for line in f.readlines():
		if (line[0] == 'G'):
			if line[5:7] == '01':
				continue
			B,count = solver(A)
			d = int(str(B[0][0])+str(B[0][1])+str(B[0][2]))
			print(B,count,d)
			S += d
			A = []
			continue
		A.append([int(t) for t in line[:9]])

B,count = solver(A)
d = int(str(B[0][0])+str(B[0][1])+str(B[0][2]))
print(B,d)
S += d
print(S)