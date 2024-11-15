import sys
sys.path.insert(1, __file__[:__file__.find('Python_codes')+13]+'Some_modules')

import sublistsofsize

digits = list('0123456789')
targets = ['01','04','09'] + [str(x ** 2) for x in range(4,10)]

count = 0

for L1 in sublistsofsize.sublists(digits,6):
	missing = []
	for s in '0123458': #
		if not (s in L1):
			missing.append(s)
	for L2 in sublistsofsize.sublists(digits,6):
		for s in missing:
			if not (s in L2): # dismisses choice of L2 if it cant complement the digits of L1
				break
		else:
			for L in [L1,L2]: #adds 6 or 9 to the list if the other is already there
				if '6' in L and not ('9' in L):
					L.append('9')
				if '9' in L and not ('6' in L):
					L.append('6')
			for t in targets:
				if not (t[0] in L1 and t[1] in L2) and not (t[1] in L1 and t[0] in L2): #results in a break if a target cannot be made
					break
			else:
				count += 1
print(count // 2) # corrects for overcount as you count the pairs in ordered fashion