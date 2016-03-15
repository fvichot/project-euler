#!/usr/bin/python

import math
import collections
from sets import Set

_primes_cache = [2,3]
_primes_set = Set(_primes_cache)

def _is_prime_from_cache(n):
    is_prime = True
    for i in _primes_cache:
        if i*i > n:
            break
        if n % i == 0:
            is_prime = False
            break
    return is_prime

def _fill_primes_cache(target):
    global _primes_cache
    n = _primes_cache[-1]
    while n*n < target:
        n += 2
        if _is_prime_from_cache(n):
            _primes_cache.append(n)
            _primes_set.add(n)


def prime_factors(n):
    global _primes_cache
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
                _fill_primes_cache(n)
            p = _primes_cache[i]
    return factors


def is_prime(n):
    global _primes_cache,_primes_set
    if n == 1:
        return False
    if n in _primes_set:
        return True
    _fill_primes_cache(n)
    return _is_prime_from_cache(n)


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


def gcd(a,b):
	divs_a = divisors(a)
	divs_b = divisors(b)

	l1 = divs_a if a < b else divs_b
	l2 = divs_b if a < b else divs_a
	for i in l1:
		if i in l2:
			return i
