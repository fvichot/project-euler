#!/usr/bin/python

for a in range(0,1001):
  for b in range(a+1, 1001):
    if a + b > 1000:
      break
    c = 1000 - a - b
    if c == a or c == b:
      break
    if (a*a)+(b*b) == c*c:
      print "A,B,C:", a,b,c
      print "ABC:", a*b*c
      exit(0)

