#!/usr/bin/python

primes = [2,3]

def find_primes(nb):
    n = primes[-1]
    while len(primes) < nb:
        n += 2
        is_prime = True
        for i in primes:
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)

def prime_factors(n):
    i = 0
    factors = []
    p = primes[0]
    while n > 1:
        if n % p == 0:
            factors.append(p)
            n //= p
        else:
            i += 1
            if i == len(primes):
                find_primes(len(primes) + 500)
            p = primes[i]
    return factors

from operator import mul
_divisors_cache = {}
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
    powers_i = [0]*nb_factors
    done = False
    while not done:
        d = reduce(mul, [factors[i]**powers_i[i] for i in xrange(0,nb_factors)])
        divs.append(d)
        i = 0
        while True:
            powers_i[i] += 1
            if powers_i[i] > powers[i]:
                powers_i[i] = 0
                i += 1
                if i == nb_factors:
                    done = True
                    break
                continue
            break

    _divisors_cache[n] = divs
    return divs

def are_amicable(a,b):
    return (sum(divisors(a)[:-1]) == b and sum(divisors(b)[:-1]) == a)

amicable = []
amicable_sum = 0
for a in xrange(2, 10000):
    for b in xrange(2, 10000):
        if a != b and a not in amicable and b not in amicable and are_amicable(a,b):
            print "(%d, %d)" % (a, b)
            amicable_sum += a + b
            amicable += [a,b]

print "Sum:", amicable_sum