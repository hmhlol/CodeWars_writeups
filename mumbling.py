#!/usr/bin/python3


def accum(s):
	chr = list(s)
	arr = []
	for i in range(0, len(chr)):
		arr.append(f'{chr[i].upper()}{chr[i].lower()*i}')
		str = '-'.join(arr)
	print(str)

accum("ZpglnRxqenU")
