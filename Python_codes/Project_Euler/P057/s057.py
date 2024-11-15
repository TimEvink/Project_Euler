import sys
sys.path.insert(1, __file__[:__file__.find('Python_codes')+13]+'Some_modules')

import contfrac

print(contfrac.convergents([1,2,2,2,2]))

count = 0
B = 1000

fracs = contfrac.convergents([1]+[2]*B)
for i in range(1,B+1):
	t = fracs[i][0]
	n = fracs[i][1]
	if len(str(t)) > len(str(n)):
		count += 1

print(count)
