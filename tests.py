import unittest
from main import blossom

class RetryTestCase(unittest.TestCase):

    def test_no_params(self): #@blossom()
        expected = "expected"
        self.assertEqual(blossom(), expected)

    def test_with_null(self):  # @blossom(0)
        expected = "Число не целое или меньше 1"
        self.assertEqual(blossom(0), expected)

    def test_sussecs(self):  # @blossom(3)
        expected = "expected"
        self.assertEqual(blossom(3), expected)

    def test_negative_number(self):  # @blossom(-3)
        expected = "Число не целое или меньше 1"
        self.assertEqual(blossom(-3), expected)

    def test_fractional_number(self):  # @blossom(-5.5)
        expected = "Число не целое или меньше 1"
        self.assertEqual(blossom(5.5), expected)

    def test_not_number(self):  # @blossom(f)
        expected = "Число не целое или меньше 1"
        self.assertEqual(blossom(f), expected)

if __name__ == '__main__':
    unittest.main()