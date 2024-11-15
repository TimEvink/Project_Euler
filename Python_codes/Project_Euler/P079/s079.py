import sys
sys.path.insert(1, __file__[:__file__.find('Python_codes')+13]+'Some_modules')

import sublistsofsize
import copy

logs = []

with open('p079_keylog.txt', 'r') as file:
	for item in file:
		logs.append(item[:3])

print(logs)


def adddigits(L,digits): #L is a list of strings, and digits is a  strings. Makes a list of all options of making strings out of strings in L by adding 1 digit from the string digits.
	A = []
	for s in L:
		for d in digits:
			for i in range(len(s)+1):
				A.append(s[:i]+ d +s[i:])
	return A

def isin(s,reply): #s and reply are strings, with reply having 3 elts. returns true iff reply can be obtained from s.
	I = sublistsofsize.sublists(list(s),3)
	if list(reply) in I:
		return True
	return False



passcands = ['']

for reply in logs:
	newcands = []
	for s in passcands:
		if isin(s,reply):
			newcands.append(s)
	if not newcands == []: #means some candidates already contain the new reply, so we take those
		passcands = list(set(newcands.copy()))
		print(passcands)
		continue
	newcands = passcands.copy()
	for _ in range(3): #iterates the 'add a digit' procedure intil it finds hits
		newcands = adddigits(newcands,reply)
		aux = []
		for s in newcands:
			if isin(s,reply):
				aux.append(s)
		if not aux == []: #means some candidates contain the new reply, so we take those
			passcands = list(set(aux.copy()))
			print(passcands)
			break

print(passcands)







# def addlog(passcode,reply):
# 	n = len(passcode)
# 	I = sublistsofsize.sublists(list(passcode),3)
# 	for i in I:
# 		if i == list(reply) #means reply is already in passcode
# 			return [passcode]
# 	I = sublistsofsize.sublists(list(passcode),2)
# 	for i in I:
# 		if i == list(reply)[:2]
# 			extradigit = reply[2]



