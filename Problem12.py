#! /usr/bin/python
# problem statement: projecteuler.net/problem=12
import timeit
import math
from Problem7 import primes

def f2(x):
	new_primes = primes(10001)
	l = 10001
	s = 1
	inc = 1
	div = 0
	while(div < 500):
		div =1
		inc = inc + 1
		s = s+inc
		temp = s
		for i in range(0,l):
			if (new_primes[i]*new_primes[i]) > temp:
				div = div*2
				break
			exp = 1
			while temp % new_primes[i]==0:
				exp +=1
				temp = temp/new_primes[i]
			if exp > 1:
				div = div * exp
			if temp ==1:
				break
	print s


def f(x):
	s = 1
	inc = 1
	div = 0
	while(div < 500):
		inc +=1
		s += inc
		for i in range(1,s+1):
			if s % i ==0:
				div +=1
		if div > x:
			return s
		div = 0
		
#def f(x):
#	s = sum(range(x+1))
#	inc = x+1
#	#i=1
#	while(True):
#		div = 0
#		ss = math.sqrt(s)
#		for n in range(1, ss+1):
#			if s%n == 0:
#				div +=2
#		if ss*ss == s:
#			div -=1
#		
#		for n in range (1, s+1):
#			if s%n == 0:
#				div +=1
#		if div > x:
#			print "success! length: " + str(div)
#			print inc
#			return s
#		#else:
#		#	print "no dice. length: " + str(len(array))
#		s += inc
#		inc +=1
#
#def g(x):
#	i=1
#	s = sum(range(x+i)
#	while():
#		array = []
#		temp = s
#		n = 2
#		while temp > n:
#			if temp % n == 0:
#				temp = temp/n
#				array.append(n)
#		# do something with array
#		if 
#		
#		i+=1
#		s += x+i
#		del array[:]






start = timeit.default_timer()

f2(500)
stop = timeit.default_timer()

print "time: " + str(stop - start)
