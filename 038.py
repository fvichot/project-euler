#!/usr/bin/python
# -*- coding: utf-8 -*-

# Take the number 192 and multiply it by each of 1, 2, and 3:

#     192 × 1 = 192
#     192 × 2 = 384
#     192 × 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the # concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the 
# pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated 
# product of an integer with (1,2, ... , n) where n > 1?

def find_largest_pandigital():
	digits = "123456789"
	i = 1
	largest = 0
	for i in xrange(1,100000):
		r = []
		l = 0
		for j in xrange(1,10):
			s = str(i*j)
			r.append(s)
			l += len(s)
			if l >= 9:
				break
		if j > 1 and l == 9 and ''.join(sorted(''.join(r))) == digits:
			n = int(''.join(r))
			print i, j, r
			if n > largest:
				largest = n
	return largest



if __name__ == '__main__':
	largest = find_largest_pandigital()
	print "Largest:", largest