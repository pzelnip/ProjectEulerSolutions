'''
2520 is the smallest number that can be divided by each of the numbers from 1 
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?

Created on Feb 18, 2012

@author: aparkin
'''
from project_euler.timing import timeruns, format_runs

def prob5(lim = 10):
    '''
    Solution to problem #5.
    
    @param lim: the "upper bound" on the list of numbers
    @type lim: int
    
    @return: the smallest positive number that is evenly divisible by all of 
    the numbers from 1 to lim
    @rtype: int
    '''
    
    # note that we only need test the upper half of the numbers, as if a number
    # is divisible by the upper half nums, then it must also be divisible by the
    # lower half nums.
    nums = range(lim / 2, lim+1)
    
    # and no need to test all numbers, only start at the largest number, and 
    # increment by multiples of this number
    x = iter = max(nums)
    while not all([x % num == 0 for num in nums]):
        x += iter
    return x
   
        
def prob5v2(lim = 10):
    '''
    Essentially same approach, but replace all() call with inner function to 
    take advantage of boolean short circuiting
    '''
    nums = range(lim / 2, lim+1)
    def divbynums(x):
        for num in nums:
            if x % num != 0:
                return False
        return True
    
    x = iter = max(nums)
    while not divbynums(x):
        x += iter
    return x
   
def main():
    print prob5v2(20)
    
    # time different approaches, using first 15 as doing 1st 20 takes too long
    setup = """
from project_euler.problem5.problem5 import prob5, prob5v2
    """
    runs = [("""prob5(15)""", setup, "Using all()"),
            ("""prob5v2(15)""", setup, "Inner pred function"),
            ]
    num_iterations = 100
    print format_runs(timeruns(runs, num_iterations))
    
if __name__ == "__main__":
    main()