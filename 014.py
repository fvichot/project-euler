#!/usr/bin/python

max_len = 0
num = 0
for n in xrange(1,1000000):
	chain_len = 0
	c = n
	while c != 1:
		if c % 2 == 0:
			c = c / 2
		else:
			c = 3 * c + 1
		chain_len = chain_len + 1
#	print n, chain_len
	if chain_len > max_len:
		max_len = chain_len
		num = n

print "Num:", num, "Length:", max_len