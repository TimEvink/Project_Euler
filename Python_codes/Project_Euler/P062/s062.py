dic = {}
k = 0
while True:
	k += 1
	s = str(k ** 3)
	val = []
	for d in range(10):
		count = 0
		for digits in s:
			if digits == str(d):
				count += 1
		val.append(count)
	tup = tuple(val)
	if tup in dic:
		dic[tup].append(k)
	else:
		dic[tup] = [k]
	if len(dic[tup]) == 5:
		print(dic[tup])
		print(dic[tup][1] ** 3)
		break

