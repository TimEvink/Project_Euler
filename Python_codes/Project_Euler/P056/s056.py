import sys
sys.path.insert(1, __file__[:__file__.find('Python_codes')+13]+'Some_modules')

max = 0
B = 100

for a in range(1,B):
	for b in range(1,B):
		digits = [int(d) for d in str(a**b)]
		if sum(digits) > max:
			max = sum(digits[:])
			print(a,b,max)