#!/usr/bin/python
# problem statement: projecteuler.net/problem=15

import timeit

def f():
	Matrix = [[0 for x in range(21)] for y in range(21)]
	for x in range(20):
		Matrix[x][20] = 1
		Matrix[20][x] = 1
	for x in range(19,-1, -1):
		for y in range(19,-1,-1):
			Matrix[x][y] = Matrix[x+1][y] + Matrix[x][y+1]
	print Matrix[0][0]

start = timeit.default_timer()
f()
stop = timeit.default_timer()
print "time: " + str(stop-start)
