'''
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Created on Feb 18, 2012

@author: aparkin
'''
from project_euler.timing import timeruns, format_runs

def ispalindrome(num):
    '''
    Simple predicate to test if num is a palindromic number.
    
    @return: true if num is a palindrome, false otherwise
    '''
    str_num = str(num)
    return str_num == (str_num[::-1]) 
    
def prob4(numdigits=3):
    '''
    1st attempt to solve problem 4, pretty much brute force.
    
    @param numdigits: how many digits should the two factors have.
    @type numdigits: int
    
    @return: a 3-tuple (factor1, factor2, num) such that num is the largest
    palindrome that is a product of two numdigits numbers: factor1 and factor2
    @rtype: (int, int, int)
    '''
    biggest = 10**numdigits-1
    smallest = 10**(numdigits-1)
    palindromes = {}
    
    # loop over all possible 3 digit factors, taking advantage of the 
    # commutivity of multiplication (ie 3 x 4 == 4 x 3)
    for num1 in range(biggest, smallest, -1):
        for num2 in range(num1, smallest, -1):
            if ispalindrome(num1 * num2):
                palindromes[num1*num2] = (num1, num2, num1 * num2)
                
    return palindromes[sorted(palindromes, reverse=True)[0]]

def prob4v2(numdigits=3):
    '''
    Same as v1, but using a dict comprehension to see if the move from nested
    for loop to nested dict comprehension would be faster
    '''
    biggest = 10**numdigits-1
    smallest = 10**(numdigits-1)-1
    palindromes = {i * j : (i, j, i * j) for i in range(biggest, smallest, -1) 
            for j in range(i, smallest, -1)
            if ispalindrome(i * j)}    
    return palindromes[sorted(palindromes, reverse=True)[0]]

def main():
    print prob4(3)    
    print prob4v2(3)

    # time different approaches
    setup = """
from project_euler.problem4.problem4 import prob4, prob4v2
    """
    runs = [("""prob4(3)""", setup, "Nested For Loop"),
            ("""prob4v2(3)""", setup, "Dict comprehension"),
            ]
    num_iterations = 100
    print format_runs(timeruns(runs, num_iterations))
    
if __name__ == "__main__":
    main()