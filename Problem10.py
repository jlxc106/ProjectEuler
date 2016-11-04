#! /usr/bin/python
#Problem statement: https://projecteuler.net/problem=10

import math

def primes(iterable):
i = 5
s=5
LIST = [2,3]
while i<iterable:
	if all(i%j != 0 for j in LIST):
		s+=i
		LIST.append(i)
	i+=2
print s

primes(2000000)
