'''
Unit tests for the solution

Created on 2012-02-07

@author: aparkin
'''
from operator import mul
import unittest
from project_euler.problem3.problem3 import prob3

class TestProb3Soln(unittest.TestCase):
    def test_prob3with_prime(self):
        ''' test on a prime number '''
        # Arrange
        num = 5
        expected_factors = [5]
        
        # Act
        factors = prob3(num)
        
        # Assert
        self.assertEquals(num, reduce(mul, factors))
        self.assertEquals(set(factors), set(expected_factors))  
        
    def test_prob3with_all_unique_factors(self):
        ''' test on a number with no duplicate factors '''
        # Arrange
        num = 13195
        expected_factors = [5, 7, 13, 29]
        
        # Act
        factors = prob3(num)
        
        # Assert
        self.assertEquals(num, reduce(mul, factors))
        self.assertEquals(set(factors), set(expected_factors))  
        
    def test_prob3with_single_factor_duplicated(self):
        ''' test on a number with the same factor multiple times '''
        # Arrange
        num = 16
        expected_factors = [2, 2, 2, 2]
        
        # Act
        factors = prob3(num)
        
        # Assert
        self.assertEquals(num, reduce(mul, factors))
        self.assertEquals(set(factors), set(expected_factors))  
