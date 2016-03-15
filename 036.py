#!/usr/bin/python

# The number 3797 has an interesting property. Being prime itself, it is possible to continuously 
# remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly
# we can work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to
# left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import math
import itertools as it
import euler_utils as e

def is_prime(n):
	if n == 1:
		return False
	if n != 2 and n % 2 == 0:
		return False
	m = 3
	while m*m <= n:
		if n % m == 0:
			return False
		m += 2
	return True


def is_truncatable(n):
	if not e.is_prime(n):
		return False
	
	s = str(n)
	for d in xrange(1,len(s)):
		r = int(s[d:])
		l = int(s[:d])
		if not e.is_prime(l) or not e.is_prime(r):
			return False
	return True

def tuple_to_int(t):
	return reduce(lambda r,d: int(r)*10 + int(d), t) 


def iter_to_infinity():
	for i in [2,3,5,7]:
		yield i
	i = 2
	while True:
		for n in it.imap(tuple_to_int, it.product("123579",repeat=i)):
			yield n
		i += 1
		

def find_truncatable_primes():
	total = 0
	count = 0
	c = 0
	
	for i in iter_to_infinity():
		c += 1
		if i < 10:
			continue
		if is_truncatable(i):
			print i
			total += i
			count += 1
			if count == 11:
				break
	print "C:",c
	return total


if __name__ == '__main__':
	total = find_truncatable_primes()
	print "Sum of truncatable primes:", total
