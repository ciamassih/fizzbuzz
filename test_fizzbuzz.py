import unittest

from fizzbuzz import Fizzbuzz

class TestFizzbuzz(unittest.TestCase):


    def test_multiple_of_three_6(self):
        fizzbuzz = Fizzbuzz()
        self.assertEqual(fizzbuzz.process(6), "Fizz")

    def test_multiple_of_three_9(self):
        fizzbuzz = Fizzbuzz()
        self.assertEqual(fizzbuzz.process(9), "Fizz")

    def test_multiple_of_five_10(self):
        fizzbuzz = Fizzbuzz()
        self.assertEqual(fizzbuzz.process(10), "Buzz")


