#!/usr/bin/python
# problem statement: projecteuler.net/problem=14
import timeit

#n -> n/2(n is even)
#n -> 3n + 1(n is odd)
gcounter = 0

def f(lcounter,x, originx):
	global gcounter
	if x%2==0: # even
		x = x/2
	else:
		x = 3*x + 1
	if x == 1:
		if lcounter > gcounter:
			gcounter = lcounter
			print str(originx) + " | counter: " + str(gcounter)
	else:
		lcounter += 1
		return f(lcounter, x, originx)



start = timeit.default_timer()
for i in range(999999,0,-1):
	f(0,i,i)
stop = timeit.default_timer()

print "time: " + str(stop-start)
