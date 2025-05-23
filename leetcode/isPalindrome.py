import unittest
class Solution:
    def isPalindrome(self, s: str) ->bool:
        if len(s)<= 1:
            return True
        
        s = ''.join(char.lower() for char in s if char.isalnum())

        r = len(s)-1
        l = 0
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1

        return True

class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_example1(self):
        s = "A man, a plan, a canal: Panama"
        expected = True
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

    def test_example2(self):
        s = "race a car"
        expected = False
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

    def test_example3(self):
        s = " "
        expected = True
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

    def test_empty_string(self):
        s = ""
        expected = True
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

    def test_single_character(self):
        s = "a"
        expected = True
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

    def test_numbers_and_special_chars(self):
        s = "0P"
        expected = False
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

    def test_palindrome_with_numbers(self):
        s = "12321"
        expected = True
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

    def test_non_palindrome_with_numbers(self):
        s = "12345"
        expected = False
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
