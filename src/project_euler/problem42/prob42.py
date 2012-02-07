'''
The nth term of the sequence of triangle numbers is given by, tn = 0.5n(n+1); 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a 
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
containing nearly two-thousand common English words, how many are triangle 
words?

Created on 2012-02-03

@author: aparkin
'''
from math import sqrt
from project_euler.timing import timeruns, format_runs

FIRST_100_TNUMS = {0.5 * n * (n + 1) for n in range(1, 1000)}

def is_tnum_set(num):
    '''
    Test if num is a triangle number by doing set lookup.
    '''
    return num in FIRST_100_TNUMS

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
    letter_mapping = dict(zip("\nABCDEFGHIJKLMNOPQRSTUVWXYZ", range(0, 100)))
    triangle_count = 0
    for word in words:
        total = sum([letter_mapping[letter] for letter in word])
        if testfn(total):
            triangle_count += 1

    return triangle_count

def loadfile():
    ''' Q & D way of opening the file & converting to a list.'''
    fobj = open ("words.txt", "r")
    lines = fobj.readline().upper().split('"')[0].split(",")
    fobj.close()
    return lines

def main():
    '''
    Run the solution to the problem timing each approach
    '''
    # Print out the answer for the given input
    print "Answer: %d" % prob42(loadfile(), is_tnum_set)

    # time different approaches
    setup = """
from project_euler.problem42.prob42 import prob42, is_tnum_builtinsqrt, loadfile
lines = loadfile()
    """
    runs = [("""prob42(lines)""", setup, "Using Set Lookup"),
            ("""prob42(lines, is_tnum_builtinsqrt)""", setup, 
             "Solving quadratic"),
            ]
    num_iterations = 100
    print format_runs(timeruns(runs, num_iterations))
    
if __name__ == "__main__":
    main()