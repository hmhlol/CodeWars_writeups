#!/usr/bin/python3

def alphabet_war(fight):
	left_letter = "wpbs"
	left_dict = {'w': 4, 'p': 3, 'b': 2, 's': 1}
	right_letter = "mqdz"
	right_dict = {'m': 4, 'q':3 , 'd': 2, 'z': 1}
	left_power = 0
	right_power = 0
	for i in fight:
		if i in left_letter:
			left_power += left_dict[i]
		elif i in right_letter:
			right_power += right_dict[i]
	if left_power > right_power:
		print("Left side wins!")
	elif left_power == right_power:
		print("Let's fight again!")
	else:
		print("Right side wins!")


alphabet_war("zdqmwpbs")
