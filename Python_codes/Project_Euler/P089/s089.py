import os

#generates absolute path to .txt file
file_path = os.path.join(os.path.dirname(__file__), 'p089_roman.txt')


A = []
with open(file_path, 'r') as f:
	for line in f:
		A.append(line.strip())

count = 0

alphabet = ['I','V','X','L','C','D','M']

for number in A:
	l = len(number)
	if l < 4:
		continue
	else:
		for i in range(l-3):
			if number[i] == number[i+3] and number[i] == number[i+1] and number[i] == number[i+2]:
				if i == 0:
					if number[0] == 'M':
						continue
					else:
						count += 2
				elif alphabet.index(number[i-1]) == alphabet.index(number[i]) + 1:
					count += 3
				else:
					count += 2



print(count)