#!/usr/bin/python3


"""---This challenge is to delete the number if the count of the number is greater than given times of the number: -----"""

#delete_nth([1,1,3,3,7,2,2,2,2], 3)
delete_nth([20,37,20,21], 1)

def delete_nth(chr, n):
	arr = []
	for i in chr:
		if arr.count(i) < n:
			arr.append(i)
	print(arr)
