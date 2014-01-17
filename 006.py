#!/usr/bin/python

sum_square = 0
for i in range(1,101):
  sum_square = sum_square + (i*i)

print "Sum of squares:", sum_square

square_sum = 0
for i in range(1,101):
  square_sum = square_sum + i
square_sum = square_sum * square_sum

print "Square of sum:", square_sum

print "Diff: ", square_sum - sum_square
