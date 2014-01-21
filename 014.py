#!/usr/bin/python
max_len, num = (0, 0)
_cache = {}
for n in xrange(1,1000000):
	chain_len, c = (0, n)
	while c != 1:
		if c in _cache:
			chain_len += _cache[c]
			break
		else:
			c = (c / 2) if (c % 2) == 0 else (3 * c + 1)
			chain_len += 1
	if chain_len > max_len:
		max_len, num = (chain_len, n)
	_cache[n] = chain_len
print "Num:", num, "Length:", max_len