import sys
sys.path.insert(1, __file__[:__file__.find('Python_codes')+13]+'Some_modules')

import sublistsofsize


with open('0098_words.txt', 'r') as f:
	s = f.read()

t = "";
for d in s:
	if not d == "\"":
		t += d

words = t.split(",") #A list of all the words.

pairs = []

n = len(words)
for i in range(n): #a list of all anagram pairs
	for j in range(i+1,n):
		w1 = list(words[i])
		w2 = list(words[j])
		if len(w1) == len(w2):
			w1.sort()
			w2.sort()
			if w1 == w2:
				pairs.append((words[i],words[j])) 


m = 0
for P in pairs: # finds the maximum length of words occuring in a pair
	if len(P[0]) > m:
		m = len(P[0])

squares = []
n = 0
while True: #finds the list of all possible squarses, using the maximum word length as upper bound.
	n += 1
	if 10 ** m <= n ** 2:
		break
	if 10 ** 2 <= n ** 2:
		squares.append(n ** 2)

print(pairs)

for P in pairs:
	w1,w2 = P[0],P[1]
	k = len(w1)
	localsquares = []
	for val in squares: #takes the squares with suitables numberof digits
		vallength = len(str(val))
		if vallength < k:
			continue
		if vallength == k:
			localsquares.append(val)
		else:
			break
	print(P)
	for val in localsquares:
		strval = str(val)
		for d in '0123456789': #checks if val can result from digital substitution (distinct letters --> distinct numbers)
			indices = []
			for i in range(k):
				if d == strval[i]:
					indices.append(i)
			if len({w1[i] for i in indices}) > 1: #means multiple letters would get the same number
				break
		else: 
			t = ""
			for j in range(k):
				t += strval[w1.index(w2[j])]
			if int(t) in localsquares:
				print(val,int(t))








