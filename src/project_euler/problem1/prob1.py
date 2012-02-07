'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Created on 2012-02-03

@author: aparkin
'''
from timeit import Timer

def prob1naive(num1, num2, limit):
    '''
    Naive (O(n)) solution to problem #1.
    '''
    total = 0
    for ival in range(limit):
        if ival % num1 == 0 or ival % num2 == 0:
            total += ival
            
    return total
    
def sumkn (k, n):
    '''
    Return the sum of all the numbers divisible by k, and less than n
    '''
    a = (n - 1) / k
    return k * (a * (a + 1)) / 2  

def prob1smart(num1, num2, limit):
    '''
    More intelligent solution to problem #1 using the inclusion-exclusion principle
    (http://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle).

    More efficient, O(1) time.
    '''
    return sumkn(num1, limit) + sumkn(num2, limit) - sumkn(num1 * num2, limit)

if __name__ == "__main__":
    num_iter = 1000
    t1 = Timer("""prob1naive(3,5,1000)""", """from __main__ import prob1naive""")
    print "Naive version: %s" % t1.timeit(num_iter)
    t2 = Timer("""prob1smart(3,5,1000)""", """from __main__ import prob1smart""")
    print "Smart version: %s" % t2.timeit(num_iter)

    print prob1naive(3, 5, 1000)
    print prob1smart(3, 5, 1000)
