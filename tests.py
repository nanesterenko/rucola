import unittest
from blossom import blossom, get_page_content, ConfigurationError


class TestCaseRetry(unittest.TestCase):

    def test_sussess_with_params(self):  # @blossom(3)
        expected = " \"get_page_content\": \n \"is_success\" : False \n \"run\" : [' \"exception\": ConnectionError," \
                   "  \"return\": None', ' \"exception\": ConnectionError,  \"return\": None']"
        actual = get_page_content("http://very_fake_address.com")
        self.assertEqual(expected, actual)

    def test_with_null(self):  # @blossom(0)
        with self.assertRaises(ConfigurationError):
            blossom(0)

    def test_negative_number(self):  # @blossom(-3)
        with self.assertRaises(ConfigurationError):
            blossom(-3)

    def test_fractional_number(self):  # @blossom(5.5)
        with self.assertRaises(ConfigurationError):
            blossom(5.5)

    def test_not_number(self):  # @blossom(f)
        with self.assertRaises(TypeError):
            blossom('f')


if __name__ == '__main__':
    unittest.main()
