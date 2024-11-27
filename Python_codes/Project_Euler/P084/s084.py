import random

numberofdigits = 6


board = list(range(40))
CC = [0,10] + 14 * ["dummy"]
CH = [0,10,11,24,39,5,"R","R","U","back"] + 6 * ["dummy"]

random.shuffle(CC)
random.shuffle(CH)
position = 0

numberofgames = 1000000
endtiles = 40*[0]


for _ in range(numberofgames):
	for k in range(3):
		dice1 = random.randint(1,numberofdigits)
		dice2 = random.randint(1,numberofdigits)
		if dice1 == dice2:
			double = True
		else:
			double = False
		if k == 2 and double == True:
			position = 10 #3rd double means go to jail and end turn
			break
		position += dice1 + dice2
		position %= 40
		if position in [7,22,36]: #means you hit CH
			card = CH.pop(0)
			if type(card) == int:
				position = card
			if card == "R":
				if position == 7:
					position = 15
				if position == 22:
					position = 25
				else:
					position = 5
			if card == "U":
				if position == 22:
					position = 28
				else:
					position = 12
			if card == "back":
				position -= 3
				position %= 40
			CH.append(card)
		if position in [2,17,33]: #means you hit CC
			card = CC.pop(0)
			if type(card) == int:
				position = card
			CC.append(card)
		if position == 30:
			position = 10
		if double == False:
			break
	endtiles[position] += 1

for d in range(40):
	print(d,float(100*endtiles[d]/float(numberofgames)))





