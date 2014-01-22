#!/usr/bin/python

def permutations(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in permutations(elements[1:]):
            for i in xrange(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

print sorted(permutations("0123456789"))[1000000-1]