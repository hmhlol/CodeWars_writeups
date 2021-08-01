#!/usr/bin/python3

"""-----This challenge is to print the alphabet which are not in a-m and the length of the string!"""

def printer_error(s):
	arr = list(s)
	error = 0
	acceptable = "abcdefghijklm"
	for i in range(0 , len(arr)):
		if arr[i] not in acceptable:
			error += 1
			#print(error)
	print( f'There are:{error}/{len(s)} Errors')




s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"

printer_error(s)
