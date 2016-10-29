#! /usr/bin/python
# problem statement: https://projecteuler.net/problem=6

accum_i=0
sum_squares=0
for i in range(1,101):
	sum_squares +=(i*i)
	accum_i +=i
square_sum = accum_i*accum_i
print square_sum - sum_squares
