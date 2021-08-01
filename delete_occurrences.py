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



"""
def delete_nth(chr, n ):
	arr = []
	letter = ''
	for i in chr:
		if str(i) in letter:
			continue
		count = chr.count(i)
		letter += str(i)
		if count > n:
			for j in range(n):
				arr.append(i)
		else:
			for k in range(count):
				arr.append(i)
	print(arr, letter)

"""

"""def delete_nth(chr , n):
	arr = [0]*len(chr)
	letter = ''
	c = 0
	for i in chr:
		if str(i) in letter:
			continue
		count = chr.count(i)
		letter += str(i)
		if count > n:
			for j in range(n):
				index = chr.index(i,c,len(chr)+1)
				c = index+1
				arr[index] += i
		else:
			for k in range(count):
				index = chr.index(i,c,len(chr)+1)
				c = index+1
				arr[index] += i
	print(arr,count)
"""


		
