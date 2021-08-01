#!/usr/bin/python3

"""------this challenge is to order the string according to the number in each string!-------"""


def order(sentence):
	chr = sentence.split(' ')
	ans = ''
	for j in range(1,len(chr)+1):
		for i in chr:
			if str(j) in i:
				if j == len(chr):
					ans += i
				else:
					ans += f'{i} '
	print(ans)

order("4of Fo1r pe6ople g3ood th5e the2")
