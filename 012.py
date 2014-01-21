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

def find_prime_factors(n):
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

def nb_divisors(n):
    f = find_prime_factors(n)
    prime, power = (f[0],0)
    total = 1
    for p in f:
        power += 1
        if p != prime:
            total *= power
            prime = p
            power = 1
    total *= (power+1)
    return total

n, num, nb = (2,0,0)
while True:
    num = (n*(n+1))/2
    nb = nb_divisors(num)
    if nb > 500:
        break
    n += 1

print num, nb