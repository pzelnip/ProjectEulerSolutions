'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
'''

#My forum answer:
#
#This is a trivial problem.  For each part (sum of squares, and square of sums) 
#there's two ways you can do either:
#
#1) naive method -- do loop from 1 up to n, adding to total
#2) smart method -- use Gauss' formula
#
#I did both, so that I could time both:
#
#[code]
#def squares_sum_loop(num):
#    '''
#    Returns the square of the sum of the 1st num numbers using naive loop
#    @param num: the limit to sum to
#    @type num: int
#    @return: (1+2+...+num)^2
#    @rtype: int
#    '''
#    total = 0
#    for factor in range(1, num+1):
#        total += factor 
#    return total**2
#    
#def squares_sum_gauss(num):
#    '''
#    Returns the square of the sum of the 1st num numbers using Gauss' method
#    for summing 1..n
#    @param num: the limit to sum to
#    @type num: int
#    @return: (1+2+...+num)^2
#    @rtype: int
#    '''
#    total = int(num * (num + 1) / 2)
#    return total * total
#
#def sum_squares_loop(num):
#    '''
#    Returns the sum of squares of the 1st num numbers using naive loop.
#    @param num: the limit to sum to
#    @type num: int
#    @return: (1^2+2^2+...+num^2)
#    @rtype: int
#    '''
#    total = 0
#    for factor in range(1, num+1):
#        total += factor ** 2
#    return total
#
#def sum_squares_formula(num):
#    '''
#    Returns the sum of squares of the 1st num numbers using smart formula:
#    n*(n+1)*(2n+1)/6
#    @param num: the limit to sum to
#    @type num: int
#    @return: (1^2+2^2+...+num^2)
#    @rtype: int
#    '''
#    return num * (num + 1) * (2 * num + 1) / 6
#
#def prob6(lim, sum_of_squares, square_of_sums):
#    '''
#    Solves problem #6 -- naive approach
#    '''
#    return square_of_sums(lim) - sum_of_squares(lim)
#
#print prob6(100, sum_squares_formula, squares_sum_gauss)
#[/code]
#
#Note my prob6 function is parameterized by the functions for calculating the 
#sum of squares and square of sums, thereby allowing me to "plug & play" 
#different ways of calculating these values.
#
#Using the timeit module, I got the following results for timing (numbers are 
#in secs for 10000 runs of calulating the 1..100 answer):
#
#Timing Results:
#--------------------
#Naive sumsquares, Gauss squaresum : 0.59817518707
#Naive sumsquares, naive squaresum : 0.8145099447
#Gauss sumsquares, naive squaresum : 0.281725470695
#Gauss sumsquares, Gauss squaresum : 0.0393293002323
#--------------------
#Fastest time: Gauss sumsquares, Gauss squaresum - 0.0393293002323 (95.0% faster 
#than slowest)
#Slowest time: Naive sumsquares, naive squaresum - 0.8145099447
#
#So that Gauss guy was pretty smart eh? :)
#
#If all you want is the answer, and want it fast, you could do it as a 1-liner:
#
#[code]
#int(num * (num + 1) / 2)**2 - num * (num + 1) * (2 * num + 1) / 6
#[/code]
#
#PS -- all my solutions to ProjectEuler problems can be found on GitHub at 
#https://github.com/pzelnip/ProjectEulerSolutions