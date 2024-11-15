def dumbfac(n):
	if n <= 1:
		return 1
	if n <= 5:
		if n == 2:
			return 2
		if n == 3:
			return 6
		if n == 4:
			return 24
		return 120
	if n == 6:
		return 720
	if n == 7:
		return 5040
	if n == 8:
		return 40320
	return 362880

B = 10 ** 6
supercount = 0

for n in range(3,B+1):
	m = n
	count = 1
	while not m in [169,871,872,1454,45361,45362,363601]:
		new =  sum([dumbfac(int(d)) for d in str(m)])
		if new == m:
			break
		count += 1
		m = new
	if m in [169,1454,363601]:
		count += 2
	elif m in [871,872,45361,45362]:
		count += 1
	if count == 60:
		supercount += 1
		print(n,supercount)