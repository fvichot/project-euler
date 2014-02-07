#!/usr/bin/python

if __name__ == '__main__':
	sum = 0
	for n in xrange(10,4*9**5):
		str_n = str(n)
		sum_n = 0
		for d in str_n:
			sum_n += int(d)**5
		if sum_n == n:
			sum += n
			print n
	print sum
