#!/usr/bin/python

with open("022_names.txt") as f:
    content = f.readlines()
content = content[0].split(",")
content = sorted([x[1:-1] for x in content])

i = 1
total = 0
for l in content:
	total += sum([ord(x)-64 for x in l])*i
	i += 1
print total