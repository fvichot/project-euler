#!/usr/bin/python

def fib():
    n1,n2 = (1,1)
    yield n1
    yield n2
    while True:
        n = n1 + n2
        yield n
        n1, n2 = (n2, n)

f = fib()
n = f.next()
i = 1
while len(str(n)) < 1000:
    n = f.next()
    i += 1
print i, n