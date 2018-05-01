#!/usr/bin/python
# problem statement: projecteuler.net/problem=16

i=0

def f(x,y):
    global i
    sum = pow(x,y)
    while(sum > 0):
        i += sum % 10
        sum = sum/10


f(2, 1000)

print "result is: " + str(i)