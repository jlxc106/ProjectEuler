#! /usr/bin/python
# problem statement: https://projecteuler.net/problem=7
import math

def primes(n):
	primes_list = [2]
	attempt = 3
	while len(primes_list) < n:
		if all(attempt%prime != 0 for prime in primes_list):
			primes_list.append(attempt)
		attempt +=2
	return primes_list


#print primes(10001)





