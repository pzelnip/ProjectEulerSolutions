'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.

Created on Feb 20, 2012

@author: aparkin
'''
from project_euler.timing import timeruns, format_runs

def squares_sum_loop(num):
    '''
    Returns the square of the sum of the 1st num numbers using naive loop
    @param num: the limit to sum to
    @type num: int
    @return: (1+2+...+num)^2
    @rtype: int
    '''
    total = 0
    for factor in range(1, num+1):
        total += factor 
    return total**2
    
def squares_sum_gauss(num):
    '''
    Returns the square of the sum of the 1st num numbers using Gauss' method
    for summing 1..n
    @param num: the limit to sum to
    @type num: int
    @return: (1+2+...+num)^2
    @rtype: int
    '''
    total = int(num * (num + 1) / 2)
    return total * total

def sum_squares_loop(num):
    '''
    Returns the sum of squares of the 1st num numbers using naive loop.
    @param num: the limit to sum to
    @type num: int
    @return: (1^2+2^2+...+num^2)
    @rtype: int
    '''
    total = 0
    for factor in range(1, num+1):
        total += factor ** 2
    return total

def sum_squares_formula(num):
    '''
    Returns the sum of squares of the 1st num numbers using smart formula:
    n*(n+1)*(2n+1)/6
    @param num: the limit to sum to
    @type num: int
    @return: (1^2+2^2+...+num^2)
    @rtype: int
    '''
    return num * (num + 1) * (2 * num + 1) / 6

def prob6(lim, sum_of_squares, square_of_sums):
    '''
    Solves problem #6 -- naive approach
    '''
    return square_of_sums(lim) - sum_of_squares(lim)
    
def main():
    '''
    Run the solution to the problem timing each approach
    '''
    print prob6(100, sum_squares_formula, squares_sum_gauss)
    # time different approaches
    setup = """
from project_euler.problem6.prob6 import prob6, sum_squares_loop, \
    squares_sum_gauss, squares_sum_loop, sum_squares_formula
    """
    runs = [("""prob6(100, sum_squares_loop, squares_sum_gauss)""", setup, 
             "Naive sumsquares, Gauss squaresum"),
            ("""prob6(100, sum_squares_loop, squares_sum_loop)""", setup,
             "Naive sumsquares, naive squaresum"),
            ("""prob6(100, sum_squares_formula, squares_sum_gauss)""", setup,
             "Smart sumsquares, Gauss squaresum"),
            ("""prob6(100, sum_squares_formula, squares_sum_loop)""", setup,
             "Smart sumsquares, naive squaresum"),
            ]
    num_iterations = 10000
    print format_runs(timeruns(runs, num_iterations))
    
if __name__ == "__main__":
    main()