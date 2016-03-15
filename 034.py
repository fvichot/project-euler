#!/usr/bin/python

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math as m
import euler_utils as e

_factorial_cache = [m.factorial(i) for i in xrange(0,10)]
def factorial_sum(n):
	return sum([_factorial_cache[int(j)] for j in str(n)])


def find_curious():
	global _factorial_cache
	total = 0
	n = 3
	while n <= 100000:
		s = factorial_sum(n)
		if s == n:
			print n
			total += n
		else:
			d = 1
			while s > n:
				n = ((n // 10 ** d) + 1) * (10 ** d)
				s = factorial_sum(n)
		n += 1
	return total



if __name__ == '__main__':
	t = find_curious()
	print "Total:", t
