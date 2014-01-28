#!/usr/bin/python

def recurring_cycle(n):
	d = 1
	vals = []
	while True:
		if d in vals:
			return (len(vals) - vals.index(d))
		if d >= n:
			vals.append(d)
			d = d % n
			if d == 0:
				return 0
		else:
			d *= 10


if __name__ == '__main__':
	print recurring_cycle(2)
	print recurring_cycle(3)
	print recurring_cycle(7)

	max_len = 0
	num = 0
	for n in xrange(2,1000):
		c = recurring_cycle(n)
		if c > max_len:
			max_len, num = (c, n)
	print "Max: %d -> %d (%f)" % (num,max_len,1/float(num))