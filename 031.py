#!/usr/bin/python

import sys
from operator import mul,add

if __name__ == '__main__':
	target = 200
	if len(sys.argv) == 2:
		target = int(sys.argv[1])

	coin_values = [1,2,5,10,20,50,100,200]
	coin_values.reverse()

	def split(coin):
		s = []
		i = 0
		while coin != 0:
			value = coin_values[i]
			if i == len(coin_values)-1:
				s += [value]
				break
			if value < coin or (s != [] and value == coin):
				s += [value] * (coin // value)
				coin = coin % value
			else:
				i += 1
		return s

	def descend(coins):
		hits = 0
		i = 0
		while i < len(coins):
			# print coins
			s = split(coins[i])
			coins = coins[:i] + s + coins[i+1:]
			hits += 1
			if coins[i] == coin_values[-1]:
				i += 1
		return hits


	
	print descend([target])
	#sys.exit(0)

	hits = 0
	coin_values = [1,2,5,10,20,50,100,200]
	counts = [0]*len(coin_values)
	limits = map(lambda x: target // x, coin_values)
	i = 0
	total = 0
	while i < len(coin_values):
		total = sum(map(mul, coin_values, counts))
		if total == target:
			hits += 1

		i = 0
		while i < len(coin_values):
			counts[i] += 1
			if counts[i] > limits[i] or sum(map(mul, coin_values, counts)) > target:
				for j in xrange(0,i+1):
					counts[j] = 0
				i += 1
			else:
				break
		# print counts

	print hits