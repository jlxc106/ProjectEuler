#!/usr/bin/python
# problem statement: projecteuler.net/problem=15

i=0

def f(x,y):
	global i
	if x < 20:
		f(x+1,y)
	if y < 20:
		f(x,y+1)
	if x==20 and y==20:
		i +=1
		print i


f(0,0)
print i
