
# Problem 1: Multiples of 3 and 5
Simple problem to find find numbers below 1000 that are multiples of 3 and 5 and sum them up.
Solution involves if statements using modulo within a for loop.


# Problem 2: Even Fibonacci numbers
The Fibonacci sequence is a series of numbers starting with: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
The general rule for finding the value of a number in the Fibonacci sequence is: Fib(n) = Fib(n-2) + Fib(n-1)

The problem statement asks us to find the sum of all the even-valued terms less than 4 million. 
A while loop limits the Fibonacci elements to 4 million. Fib(n-2) and Fib(n-1) are stored in variables.
In each iteration, Fib(n-2) and Fib(n-1) are updated(because n increases).


# Problem 3: Large prime factor
The problem statement gives us a large number(600851475143) and 
asks us to find the largest prime factor. For instance, given a 
number 13195, the prime factors are: 5, 7, 13, 29.

A solution can be found by dividing the seed/large number by prime
numbers(2, 3, 5, ...) while it is divisible.(i.e. seed%2). If the seed
is not divisible by 2, we can move on to dividing it by 3, then 5, and so
on and so forth. Because the seed will no longer be divisible by 2 or 3 
non-prime numbers such as 6 or 9 will not be divisible by the seed.
The final number that divides the seed is the largest prime factor.


# Problem 4: Largest palindrome product
A palindrome is something that reads the same back from the back as it does from the 
front. For example, "racecar" is a palindrome because the starting and ending characters
are both 'r' followed by 'a', 'c' and 'e'. The problem statement asks us to find the largest
palindrome made from the product of two 3-digit numbers. Intuitively, one can access that
the largest palindrome will be the product of two large 3-digit numbers.

Multiples of 3-digit numbers range from 6-digits(e.g. 999 * 999 = 998001) 
to 5-digits(e.g. 100 * 100 = 10000). Because there is no guarantee that a 
6-digit palindrome exists, we need to check all possibilities(or until we find
the first palindrome in the sequence). The first position of the number is 
compared to the last position(array[0] == array[5]) then the next positions 
are compared(array[1] == array[4]) and so on. However, in the case that
array[0]==0, we are working with a 5-digit number and need to compare
array[1] to array[5], and so on.

# Problem 5: Smallest multiple
The problem statement asks to find the smallest number that is evenly divisible by 
all the numbers from 1 to 20. For example, 6 is the smallest number divisible by 
numbers 1, 2, and 3. For it to be divisible by 4, it must be multiplied by 2 (12 is
divisible by 4, but 6 isn't). 

The solution can be found using a for loop from 1 to 20 and for each iteration, looking
for the smallest number that makes the multiple divisible by the current number.

# Problem 6: Sum square difference
This problem asks to determine the differnce between the
sum of squares and the square of sums for a given set of 
cumulative numbers.
(e.g. (1+2+....+n)^2 minus (1^2 + 2^2 + ... + n^2))

This problem can be solved using a single for loop(making 
the solution O(n) time complexity.) where the programmer can 
accumulate the counter(i.e. i) and the square of the counter(i.e. i^2).


# Problem 7: 10001st prime
In solving problem #7, the programmer is asked to find the 10001st
prime number, with 2 being the 1st, 3 being the 2nd, and so on and so forth.

The challenge of this problem lies in the programmer's ability 
to write an algorithm that quickly determines the primality of a 
number. While the primality test generally divides number n by all numbers
from 2 to square root of n, the vast majority of these numbers can be neglected
by only testing n's divisibility by primes less than n. For example, n's divisibility 
by an even number can be determined from the conditional "if n%2==0:".


# Problem 8: Largest product in series
The problem presents a 1000 digit number from which the programmer has to find the
13 digit sequence that gives the maximum product. For example, a 5 digit sequence
'12345' has a product of 1*2*3*4*5 = 120. 

A time efficient solution can be solved by using a nested for-loop, where the outer
for-loop ranges from 0 to 987(the first position of 13 digit sequence) and the 
inner for-loop ranges from 0 to 12. If the current iteration of product is greater than
the previous maximum, the maximum product is updated.


# Problem 9: Special Pythagorean triplet
A pythagorean triplet is a set of natural numbers(positive integers) that uphold the 
pythagorean theorem: a^2 + b^2 = c^2. The problem statement presents us with an example
of a=3, b=4, and c=5 and we are asked to find the unique product abc for which 
a+b+c=1000.

The problem can by approached by using a nested for-loop(for a and b) since they are 
the raw input. Because the value of c can be derived from the pythagorean theorem, there is 
no need to iterate through three for-loops. 

The range of values of a and b help us reduce the amount of iteration necessary in reaching
our solution. The problem statement clearly establishes that a is the smallest integer, b is 
the median integer, and c is the largest. 

The range of values of a is limited to positive numbers(hence greater than 0). By scaling the
3:4:5 triangle to meet the condition a+b+c=1000, we get a rough estimate for what the ceiling
for a should be. 

The value of b is limited to be greater than the that of a and less than 500(otherwise it would
be the largest value of the three integers).

Finally, we utilize our two seed integer values to calculate the value of c.


# Problem 10: Summation of primes
The problem statement asks to find the summation fo all primes numbers less than 2 million.
We can start all list of prime numbers from 2 and 3(the smallest primes). Outside of 2, 
prime numbers are odd(meaning we can skip testing 1 million numbers by incrementing wisely).

As stated in Problem 7, we only need to test a number's divisibility by other smaller prime numbers
(a number divisible by 4 or 6 is also divisble by 2). 

While running the script, iterating through a range of numbers(~20 seconds) had a faster run time 
than iterating through the list(~400 seconds). 

The above phenomenon is most likely due to the list changing during iteration(considered bad coding
practice).

# Problem 11: Largest product in a grid
Problem 11 presents us with a 20x20 "table" of small integer values and asks for the greatest product
of four adjacent numbers(horizontal, vertical or diagonal). 

Starting from an arbitrary value: there are 8 directions that one could go to calculate a product
(left and right), (top and bottom), (top left, top right, bottom left, bottom right). However, only 
four tests are necessary since some products results are bound to be overlaps of each other. In addition,
the high number of calculations can be reduced if the value of the current index is 0.


# Problem 12: 
Problem 12 introduces the concept of triangle numbers. Which is the sum of all the integers that precede it. For example, the 7th triangle number is 1+2+3+4+5+6+7 = 28. We are then asked to find the first triangle number with over 500 divisors. In the following paragraphs, I will present both basic and advanced solutions to the problem.

Basic: 
Starting from the sum = 1, add incrementing values(2,3,4,5,...) to the sum. One can then test all the numbers smaller than the sum if it is divisible(using modulo). If the total number of divisible numbers for the sum is less than or equal to 500, we increment the value of sum and repeat the process. There are several 
modifications to the algorithm that help with our run time, such as restricting the divisible numbers test to the sqrt of the sum by accounting for the counter and its multiple(i.e. 2 * 14 = 28). However, the most impactful modification involves the use of prime numbers(surprise surprise).

Advanced:
To help explain the thought process, consider the triangle number 28. 28 can be reduced to its roots(prime numbers) of 2*2*7 = 2^2 * 7. These numbers formulate the divisible numbers of 28(1,2,4,7,14,28) and using the following equation, help us determine the total number of divisors of any given triangle number. 

Number of Divisors = (a+1)*(b+1)*(c+1)...

Where a, b, and c are the exponent values of each unique sum. Applying this equation to the number 28 results in (3)*(2) = 6, which represents the total number of divisible numbers of 28. As long as one has the access to a list of unique prime numbers, this solution will help vastly improve the run time of the solution. 

# Problem 13:
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
https://projecteuler.net/problem=13 for array of large numbers

Create a list/array of numbers and sum up all the numbers in the array. pick the first 10 digits from that sum.

# Problem 14:
https://projecteuler.net/problem=14 
f(n) = n/2 if n = even; 3n+1 if n = odd; All numbers finish when they reach 1.
Which starting number, under one million, produces the longest chain?

This problem can be fixed by keeping a global counter for the longest chain, and a local counter for the current chain.
The local counter is incremented every pass in the recursion. 
Then running the function f(n) for all values between 999999 and 1(inclusive). Whenever the local counter exceeds the global counter, the global counter is updated
to match the local counter.


# Problem 15: 
https://projecteuler.net/problem=15
How many routes are possible through a 20x20 grid?

Basic/Brute Force: 
This problem can be fixed by using recursive function f(x,y) where if the current x or y location is less than 20, we recurse into f(x+1, y) and/or f(x,y+1). The default case is reaching the endpoint of (20,20) where we increment the counter by 1.  

Advanced:
https://www.mathblog.dk/project-euler-15/

This problem can be solved faster by utilizing this pattern: f(x,y) = f(x+1, y) + f(x, y+1). With boundary conditions of f(20,20) = 0, and f(x,20) = f(20,x)=1 where x is any integer between 0 and 19. Using this formula one can build a multidimensional array to record the number of paths possible from each grid point.

# Problem 16:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

This is a fairly straight forward problem. After one gets multiple using Python's built in pow() function, one can keep summing up the modulo of the sum while dividing by 10. Until the multiple reaches 0.

Note: using the Math library's pow() function returns a float, will result in the wrong answer. The built in pow() function returns an integer. (e.g. 123.45 % 10 = 3.45)

# Problem 17:
https://projecteuler.net/problem=17
Sum up all the numbers between 1 and 1000(inclusive) written into words. 

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

There are a couple ways to tackle this problem.
    1) use a formula that counts the number of letters each number is written out into words(the way that seems natural to people)
    2) count the number of 'hundred', 'and', 'twenty', 'five' in total and sum up the occurances of each

Because method 2) requries more work pre-programming(i.e. counting the number of occurances of hundreds between 100 and 999), I chose to utilize method 1)

# Problem 18:
https://projecteuler.net/problem=18
Find the maximum total from top to bottom by moving to adjacent numbers on the row immediately below. The brute force method will not suffice.

Break up the pyramid into smaller pieces by working from the bottom up.

Starting from the 2nd to last row, calculate the maximum sum assuming the current node is the root of the pyramid/tree. (ex. the max sum assuming root @ 63 is 125(63+62)). Repeat for all numbers in the 2nd to last row.

Starting from the next row([91, 71, 52, ...]), calculate the maximum sum using the maximum from the previous row(ex. assuming root @ 91, max is 255 (91+164)). Repeat for rest of the numbers & rows.
