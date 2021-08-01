#!/usr/bin/python3


"""----This challenge is to print the input to a pair of list form, if the length of input is odd, you have to add '_' in to the input."""

s = "asdfadsfg"

def solution(s):
	arr = [] 
	if len(s) % 2:
		s += "_"
	for i in range(0, len(s), 2):
		arr.append(s[i:i+2])
	print(arr)

solution(s)
