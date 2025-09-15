import unittest
from demo.a520 import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome('madam'))
        self.assertTrue(is_palindrome('racecar'))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome('nurses run'))
        self.assertTrue(is_palindrome('A man a plan a canal Panama'))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('hello'))
        self.assertFalse(is_palindrome('python'))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_case_insensitivity(self):
        self.assertTrue(is_palindrome('MadAm'))
        self.assertTrue(is_palindrome('RaceCar'))

if __name__ == '__main__':
    unittest.main()
