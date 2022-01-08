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

    def test_multiple_of_five_20(self):
        fizzbuzz = Fizzbuzz()
        self.assertEqual(fizzbuzz.process(20), "Buzz")

    def test_multiple_of_five_and_three_15(self):
        fizzbuzz = Fizzbuzz()
        self.assertEqual(fizzbuzz.process(15), "Fizzbuzz")

    def test_multiple_of_five_and_three_30(self):
        fizzbuzz = Fizzbuzz()
        self.assertEqual(fizzbuzz.process(30), "Fizzbuzz")

    def test_other_numbers(self):
        fizzbuzz = Fizzbuzz()
        self.assertEqual(fizzbuzz.process(2), 2)



