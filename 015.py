#!/usr/bin/python

from math import factorial as f
print f(40)/(f(40-20)*f(20)) # Combinations of 20 in 20 * 2

# MAX_DOWN = MAX_LEFT = 7
# def find_nb_paths(x = 0, y = 0):
# 	if x == MAX_LEFT and y == MAX_DOWN:
# 		return 1
# 	total = 0
# 	if x < MAX_LEFT:
# 		total += find_nb_paths(x + 1, y)
# 	if y < MAX_DOWN:
# 		total += find_nb_paths(x, y + 1)
# 	return total

# print "Total:", find_nb_paths()