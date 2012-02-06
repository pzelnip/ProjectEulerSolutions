'''
The nth term of the sequence of triangle numbers is given by, tn = 0.5n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

Created on 2012-02-03

@author: aparkin
'''
from timeit import Timer
from math import sqrt

first100_tnums = {0.5 * n * (n + 1) for n in range(1, 1000)}

def is_tnum_set(num):
    '''
    Test if num is a triangle number by doing set lookup.
    '''
    return num in first100_tnums

def is_tnum_builtinsqrt(num):
    '''
    Test if num is a triangle number by doing fancy math.
    '''
    fac = (1 + 8 * num)
    return int(sqrt(fac))**2 == fac

def prob42(words, testfn = is_tnum_set):
    '''
    Solve problem #42.  Returns a count of how many words in the supplied list
    correspond to triangle numbers.  Use testfn to test if a given value is a
    triangle number or not.

    @param words: a list of words
    @type words: [ str ]

    @param testfn: a predicate function which takes an integer as an argument 
    and returns True if the number is a triangle number, False otherwise
    @type testfn: function (int) -> bool

    @return: a count of how many words in words correspond to triangle numbers
    @rtype: count
    '''
    letter_mapping = dict(zip("\nABCDEFGHIJKLMNOPQRSTUVWXYZ", range(0,100)))
    triangle_count = 0
    for word in words:
        total = sum([letter_mapping[letter] for letter in word])
        if testfn(total):
            triangle_count += 1

    return triangle_count

if __name__ == "__main__":
    # Q & D way of opening the file & converting to a list.
    fobj = open ("words.txt", "r")
    lines = fobj.readline().upper().split('"')[0].split(",")
    fobj.close()
    
    # test runs, do num_iter iterations using different triangle num test
    # functions.
    num_iter = 100
    v1 = Timer("""prob42(lines)""", """from __main__ import prob42, lines""")
    print "Using is_tnum_set: %s" % v1.timeit(num_iter)
    
    v3 = Timer("""prob42(lines, is_tnum_builtinsqrt)""",  
               """from __main__ import prob42, is_tnum_builtinsqrt, lines""")
    print "Using is_tnum_builtinsqrt: %s" % v3.timeit(num_iter)
    
    # Print out the answer for the given input
    print prob42(lines, is_tnum_set)
    print prob42(lines, is_tnum_builtinsqrt) 
