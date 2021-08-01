#!/usr/bin/python3

list = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]

def namelist(chr):
	str = ''
	if len(chr) != 0:
		arr = []
		for i in range(0, len(chr)-1):
			arr.append(chr[i]['name'])
			str = ', '.join(arr)
			str += ' & ' + chr[-1]['name']
	print(str)




namelist(list)
