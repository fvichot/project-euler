#!/usr/bin/python

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?


import math
import itertools as it

def is_prime(n):
	if n != 2 and n % 2 == 0:
		return False
	m = 3
	while m*m < n:
		if n % m == 0:
			return False
		m += 2
	return True


def is_circular(n):
	s = str(n)
	for d in xrange(0,len(s)):
		m = int(s[d:]+s[:d])
		if not is_prime(m):
			return False
	return True

def tuple_to_int(t):
	return reduce(lambda r,d: int(r)*10 + int(d), t) 


def find_circular_prime():
	count = 0
	print "Getting candidates..."
	candidates = iter([2,3,5,7])
	for i in xrange(2,7):
		candidates = it.chain(it.imap(tuple_to_int, it.product("1379",repeat=i)), candidates)
	print "Done"

	for i in candidates:
		if is_circular(i):
			count += 1
	return count


if __name__ == '__main__':
	count = find_circular_prime()
	print "Number of circular primes:", count
