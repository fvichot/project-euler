#!/usr/bin/python

import sys

WIDTH=HEIGHT=7

def grid_cell(x,y):
	if x+y == WIDTH-1 and x >= WIDTH/2:
		return ((WIDTH/2-y)*2+1)**2
	return 0


if __name__ == '__main__':
	for y in xrange(HEIGHT):
		for x in xrange(WIDTH):
			print "%02d" % grid_cell(x,y),
		sys.stdout.write(" \n")