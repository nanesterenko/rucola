import unittest
from blossom import blossom

class RetryTestCase(unittest.TestCase):

    def test_no_params(self): #@blossom()
        expected = "expected"
        self.assertEqual(expected, blossom())

    def test_with_null(self):  # @blossom(0)
        expected = "Число не целое или меньше 1"
        act = blossom(0)
        self.assertEqual(expected, act)

    def test_sussecs(self):  # @blossom(3)
        expected = "expected"
        self.assertEqual(expected, blossom(3))

    def test_negative_number(self):  # @blossom(-3)
        expected = "Число не целое или меньше 1"
        self.assertEqual(expected, blossom(-3))

    def test_fractional_number(self):  # @blossom(5.5)
        expected = "Число не целое или меньше 1"
        self.assertEqual(expected, blossom(5.5))

    def test_not_number(self):  # @blossom(f)
        expected = "NameError: name 'k' is not defined"
        self.assertEqual(expected, blossom(f))

# if __name__ == '__main__':
#     unittest.main()