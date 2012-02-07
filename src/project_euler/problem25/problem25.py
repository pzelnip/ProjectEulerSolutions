'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

Created on 2012-02-07

@author: aparkin
'''

def prob25(numdigits):
    '''
    Brute force in Python. Only "trick" was to loop until you find a fibonacci 
    number with the required number of digits, which I did using the 
    exponentiation operator (**). For example the smallest 2 digit number is 
    10**(2-1), 3 digit is 10**(3-1), n-digit is 10**(n-1).
    
    Horribly ineffecient and definitely *not* the best way of solving this 
    problem.
    '''
    if numdigits < 2:
        return 1
    fib1 = 1
    fib2 = 2
    curfib = fib1 + fib2
    term = 4
    
    while curfib < 10**(numdigits-1):           
        fib1 = fib2
        fib2 = curfib
        curfib = fib1 + fib2
        term += 1
    
    return (term, curfib)

if __name__ == "__main__":
    print prob25(1000)