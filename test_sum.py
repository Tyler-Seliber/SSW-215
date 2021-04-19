import unittest
# Imports sum() from the my_sum package you created
from my_sum import sum
from fractions import Fraction

# Defines a new test case class called TestSum, which inherits from unittest.TestCase
class TestSum(unittest.TestCase):
    
    # Defines a test method, .test_list_int(), to test a list of integers.
    def test_list_int(self):
        """ Test that it can sum a list of integers """
        data = [1, 2, 3]
        result = sum(data)
        # Assert that the value of result equals 6 by using the .assertEqual() method on the unittest.TestCase class
        self.assertEqual(result,6)

    def test_list_fraction(self):
        """ Test that it can sum a list of fractions """
        data = [Fraction(1,4), Fraction(1,4), Fraction(2,4)]
        result = sum(data)
        self.assertEqual(result, 1)

# Defines a command-line entry point, which runs the unittest test-runner .main()
if __name__ == '__main__':
    unittest.main()