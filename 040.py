#!/usr/bin/python
# -*- coding: utf-8 -*-

# An irrational decimal fraction is created by concatenating the positive integers:
# 0.12345678910 1 112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following 
# expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def slow_nth_digit(n):
	i = 1
	count = 0
	while True:
		for l in str(i):
			count += 1
			if count == n:
				return int(l)
		i += 1
	

def fast_nth_digit(n):
	if n < 10:
		return n
	i = 1
	m = 1 # because we count starting from one
	while True:
		skip = i * (10**i - 10**(i-1)) + m
		if skip > n:
			i = i-1
			skip = m
			q = n - skip
			a = q // (i+1)
			b = q % (i+1)
			r = (10**i + a)//(10**(i-b))
			k = r - (r//10)*10
			return k
		m = skip
		i += 1



def main():
	result = 1
	for i in xrange(0,7):
		result *= fast_nth_digit(10**i)

	print "Result:", result

if __name__ == '__main__':
	main()