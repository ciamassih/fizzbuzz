import unittest

from fizzbuzz import Fizzbuzz

class TestFizzbuzz(unittest.TestCase):

    def test_imprimir_un_6(self):
        fizzbuzz = Fizzbuzz("Fizz")
        self.assertEqual(fizzbuzz.fizz, "Fizz")
