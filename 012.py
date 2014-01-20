#!/usr/bin/python

from collections import OrderedDict

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
			n = n / p
		else:
			i += 1
			if i == len(primes):
				# mofo is prime...
				return [1, n]
			p = primes[i]
	return factors

def nb_divisors(n):
	f = find_prime_factors(n)
	divisors = []
	def try_other_powers(f, index, x):

	divisors += [1,n]
	divisors = list(OrderedDict.fromkeys(divisors))
	return len(divisors), divisors

n = 1
divisors = []
num = 0
nb = 0 
prime_max = primes[-1] ** 2
max_divisors = 0
while True:
	num = (n*(n+1))/2
	if num > prime_max:
		## moar primes !
		print "Moaaaaaaaar!",
		find_primes(len(primes) + 500)
		prime_max = primes[-1] ** 2
		print primes[-1], prime_max

	nb, divisors = nb_divisors(num)
	if nb > 500:
		break
	if nb > max_divisors:
		max_divisors = nb
		print "New max : ", max_divisors, "(%d)" % num
	n += 1

print num, nb, divisors