#!/usr/bin/python3

"""----This challenge is to reverse only first letter and add 'ay' to the first letter.----------"""

s = "Quis custodiet ipsos custodes ?"

def pig_it(text):
	chr = text.split(' ')
	str = ''
	arr = []
	for i in range(0, len(chr)):
		if  chr[i] in '?!@#$%^&*()':
			arr.append(chr[i])
			str = ' '.join(arr)
		else:
			arr.append(chr[i][1:]+chr[i][0]+'ay')
			str = ' ' .join(arr)
	print(str)

pig_it(s)
