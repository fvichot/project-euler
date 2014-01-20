#!/usr/bin/python

import sys
from termcolor import colored

triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

lines = triangle.split('\n')
cells = map(lambda x: x.split(' '), lines)

def find_path(path, depth, index, total):
	path = path + [index]
	total = total + int(cells[depth][index])

	if depth == len(cells)-1:
		return path, total

	lpath, ltotal = find_path(path, depth+1, index, total)
	rpath, rtotal = find_path(path, depth+1, index+1, total)
	if ltotal > rtotal:
		return lpath, ltotal
	else:
		return rpath, rtotal


def print_triangle(path):
	depth = 0
	nb_lines = len(cells)
	max_nb_cells = len(cells[nb_lines-1])
	max_width = 4*(max_nb_cells)-2
	for l in cells:
		nb_spaces = (nb_lines - 1 - depth)*2
		sys.stdout.write(' ' * nb_spaces)
		index = 0
		for c in l:
			if path[depth] == index:
				sys.stdout.write(colored(c, 'red') + "  ")
			else:
				sys.stdout.write(c + "  ")
			index = index + 1
		depth = depth + 1
		print


path, total = find_path([], 0, 0, 0)
print_triangle(path)
print "Total:", total
