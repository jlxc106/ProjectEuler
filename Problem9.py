#! /usr/bin/python
#problem statement: Special Pythagorean triplet
import math


def f():
	for a in range(1,333):
		for b in range(a,500):
			c=math.sqrt(a*a + b*b)
			if a+b+c==1000:
				print  "a: "+str(a)
				print  "b: "+str(b)
				print  "c: "+str(c)
				print  "a*b*c: "+str(a*b*c)



f()
