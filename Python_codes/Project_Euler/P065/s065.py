from Some_modules import contfrac

e = [2,1]
for k in range(1,50):
	e.append(2*k)
	e.append(1)
	e.append(1)
print(e)

fracs = contfrac.convergents(e)
print(fracs[99])
print(sum([int(d) for d in str(fracs[99][0])]))