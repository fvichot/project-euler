#!/usr/bin/python

import euler_utils as e

if __name__ == '__main__':
	t_n = 1
	t_d = 1
	for a in xrange(10,100):
		a_s = str(a)
		for i in xrange(0,2):
			for j in xrange(0,2):
				for b in xrange(1,10):
					b_s = (a_s[j] + str(b) if i == 0 else str(b) + a_s[j])

					res = abs(int(a_s)/float(b_s) - int(a_s[i])/float(b)) < 0.0000001

					if b_s <= a_s:
						continue

					if not res:
						continue

					if (a % 10) == 0 and (int(b_s) % 10) == 0:
						continue

					t_n *= int(a_s)
					t_d *= int(b_s)

	g = e.gcd(t_n,t_d)
	print t_n/g,'/',t_d/g

