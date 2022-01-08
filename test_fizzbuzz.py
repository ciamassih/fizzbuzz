import unittest

from fizzbuzz import Fizzbuzz

class TestFizzbuzz(unittest.TestCase):


    def test_multiple_of_three(self):
        fizzbuzz = Fizzbuzz()
        self.assertEqual(fizzbuzz.process(6), "Fizz")
