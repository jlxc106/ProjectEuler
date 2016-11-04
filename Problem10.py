import math
import timeit

i = 5
s = 5
#LIST = [2,3]
start = timeit.default_timer()
while i<2000000:
	t = int(math.sqrt(i))
	if all(i%j != 0 for j in range(2,t+1)):		#~20 seconds
	#if all(i%j != 0 for j in LIST if j<t+1):	#~400 seconds
		s+=i
		#LIST.append(i)
	i+=2
stop = timeit.default_timer()

print s

print "time: " + str(stop - start)

