#!/usr/bin/python

_primes_cache = [2,3]
def find_primes_cache(nb):
    n = _primes_cache[-1]
    while len(_primes_cache) < nb:
        n += 2
        is_prime = True
        for i in _primes_cache:
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            _primes_cache.append(n)


def prime_factors(n):
    i = 0
    factors = []
    p = _primes_cache[0]
    while n > 1:
        if n % p == 0:
            factors.append(p)
            n //= p
        else:
            i += 1
            if i == len(_primes_cache):
                find_primes_cache(len(_primes_cache) + 500)
            p = _primes_cache[i]
    return factors


_divisors_cache = {0:[], 1:[1]}
def divisors(n):
    if n in _divisors_cache:
        return _divisors_cache[n]

    f = prime_factors(n)
    # get factors' power
    factors, powers = ([f[0]],[0])
    for p in f:
        if p != factors[-1]:
            factors.append(p)
            powers.append(0)
        powers[-1] += 1
    
    divs = []
    nb_factors = len(factors)
    powers_i = list(powers)
    done = False
    while not done:
    	from operator import mul
        d = reduce(mul, [factors[i]**powers_i[i] for i in xrange(0,nb_factors)])
        divs.append(d)
        i = 0
        while True:
            powers_i[i] -= 1
            if powers_i[i] < 0:
                powers_i[i] = powers[i]
                i += 1
                if i == nb_factors:
                    done = True
                    break
                continue
            break

    _divisors_cache[n] = divs
    return divs

def is_abundant(n):
	return sum(divisors(n)[1:]) > n

_abundant_cache = {}
for n in xrange(1, 28124):
	if is_abundant(n):
		_abundant_cache[n] = True
total = 0
for n in xrange(1, 28124):
	has_sum = False
	for a in _abundant_cache.keys():
		if a > n:
			break
		if (n-a) in _abundant_cache:
			has_sum = True
			break
	if not has_sum:
		# print "has no sum:", n
		total += n
print "Total:", total


