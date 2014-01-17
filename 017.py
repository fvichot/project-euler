#!/usr/bin/python

digit_words = ["zero","one","two","three", "four", "five", "six", "seven", "eight", "nine"]
een_words = ["ten","eleven","twelve","thirteen","fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
decimals_words = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
power_words = ["hundred", "thousand"]
def number_to_words(n):
	if n == 0:
		return "zero"
	str_n = str(n)
	res = ""
	for power in xrange(0, len(str_n)):
		d = str_n[len(str_n)-power-1]
		if d == '0':
			continue
		if power == 0:
			res = digit_words[int(d)]
		elif power == 1:
			if d == '1':
				res = een_words[int(str_n[len(str_n)-1])]
			else:
				res = decimals_words[int(d)-1] + ("-" if res != "" else "") + res
		elif power == 2:
			res = digit_words[int(d)] + " hundred" + (" and " if res != "" else " ") + res
		elif power == 3:
			res = digit_words[int(d)] + " thousand " + res
	return res

sum = 0
for i in xrange(1,1001):
	words = number_to_words(i)
	print i, words
	sum = sum + len(words.replace(' ', '').replace('-',''))

print sum