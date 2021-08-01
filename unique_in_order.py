#!/usr/bin/python3

def unique_in_order(iterable):
	ans = []
	if len(iterable) != 0:
		ans.append(iterable[0])
		j = 0
		for i in iterable:
			if str(i) in str(ans[j]):
				continue
			else:
				ans.append(i)
				j += 1
	else:
		pass
	print(ans)

unique_in_order('AAAABBBCCDAABBB')
unique_in_order('ABBCcAD')
unique_in_order('')
