#!/usr/bin/python

if __name__ == '__main__':
	count = 0
	items = {}
	for a in xrange(2,101):
		for b in xrange(2,101):
			items[a**b] = None
	print len(items.keys())

