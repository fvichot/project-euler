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

from operator import mul
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

def are_amicable(a,b):
    return (sum(divisors(a)[1:]) == b and sum(divisors(b)[1:]) == a)

def find_amicables(_from,_to):
    amicables = []
    for a in xrange(2, 10000):
        for b in xrange(_from, _to):
            if a != b and a not in amicables and b not in amicables and are_amicable(a,b):
                print "(%d, %d)" % (a, b)
                amicables += [a,b]
    return amicables

def amicable_runner(args):
    return find_amicables(*args)

from multiprocessing import Pool
if __name__ == '__main__':
    # split work:
    NB_THREADS = 8
    args = []
    slice_size = 10000/NB_THREADS
    for n in xrange(0,NB_THREADS):
        args.append((n*slice_size, (n+1)*slice_size-1))

    p = Pool(NB_THREADS)
    res = p.map(amicable_runner, args)
    print res
    print "Sum:", sum(list(set([item for sublist in res for item in sublist])))