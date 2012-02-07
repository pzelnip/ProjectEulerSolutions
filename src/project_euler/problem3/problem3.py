'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Created on 2012-02-07

@author: aparkin
'''

from operator import mul

def prob3(num):
    '''
    Find the prime factorization of num.  
    
    @param num: the number to factorize
    @type num: int
    
    @return: a list of prime factors that factorize num
    @rtype: [ int ]
    '''
    factors = []
    factor = 2
    while factor <= num: 
        if num % factor == 0:
            factors.append(factor)
            num = num / factor
        else:
            factor += 1
    return factors
    
def main():
    ''' Find solution to problem '''
    factors = prob3(600851475143)
    print "Factors of 600851475143: %s" % factors
    print "Biggest factor: %s" % max(factors)
    if reduce(mul, factors) != 600851475143:
        print "Factorization NOT CORRECT!"
    
    # extra tests    
    print prob3(13195)
    print prob3(8)
    
if __name__ == "__main__":
    main()