#!/usr/bin/python
# -*- coding: utf-8 -*-

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are 
# exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

from math import sqrt

def integer_right_triangles():
	max_s,max_i = (0,0)
	for i in xrange(2,1001):
		sols = 0
		for a in xrange(1,i):
			for b in xrange(1,i-a):
				c = i - (a+b)
				if c*c == a*a+b*b:
					sols += 1
		if sols > max_s:
			max_s,max_i = (sols,i)
			print max_s,max_i
	return max_i

if __name__ == '__main__':
	r = integer_right_triangles()
	print "Max:", r