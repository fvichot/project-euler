#!/usr/bin/python

_primes_cache = [2,3]
_primes_dict = {2:None,3:None}
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
            _primes_dict[n] = None

def is_prime(n):
    while n > _primes_cache[-1]:
        find_primes_cache(len(_primes_cache) + 50)
    return (n in _primes_dict)

def prime_sequence_length(a,b):
    n,p = (0,0)
    while True:
        p = n*n + a*n + b
        if not is_prime(p):
            break
        n += 1
    return n

if __name__ == '__main__':

    max_n = 0
    best_a,best_b = (0,0)
    for a in xrange(-999,1000):
        for b in xrange(-999,1000):
            n = prime_sequence_length(a,b)
            if n > max_n:
                max_n,best_a,best_b = (n, a, b)
    print "Max: %d -> %d,%d (%d)" % (max_n,best_a,best_b,best_a*best_b)