# Write a method that replaces all spaces with '%20'
import unittest
class Solution:
    # hola como estas -> 'hola%20como%20estas'
    def urlify2(self, s:str)->str:
        # options to do it, make it an slice and the replace it.
        s = list(s)
        for i, val in enumerate(s):
            if val ==" ":
                s[i]="%20"
        return "".join(s)
    # The idea here is to iterate through the string and replace the spaces with %20.
    def urlify(self, s:str)->str:
        res = ""
        for i, val in enumerate(s):
            tmp = val
            if val == " ":
                tmp = "%20"
            res += tmp
        return res




class TestUrlify(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic(self):
        self.assertEqual(self.solution.urlify("Mr John Smith"), "Mr%20John%20Smith")
        self.assertEqual(self.solution.urlify("Hello World"), "Hello%20World")
        self.assertEqual(self.solution.urlify("a b c"), "a%20b%20c")

    def test_no_spaces(self):
        self.assertEqual(self.solution.urlify("HelloWorld"), "HelloWorld")
        self.assertEqual(self.solution.urlify("abc"), "abc")

    def test_all_spaces(self):
        self.assertEqual(self.solution.urlify("   "), "%20%20%20")
        self.assertEqual(self.solution.urlify(" "), "%20")

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(self.solution.urlify("  leading"), "%20%20leading")
        self.assertEqual(self.solution.urlify("trailing  "), "trailing%20%20")
        self.assertEqual(self.solution.urlify("  both  "), "%20%20both%20%20")

    def test_empty_string(self):
        self.assertEqual(self.solution.urlify(""), "")

    def test_multiple_consecutive_spaces(self):
        self.assertEqual(self.solution.urlify("a  b"), "a%20%20b")
        self.assertEqual(self.solution.urlify("a   b"), "a%20%20%20b")

if __name__ == "__main__":
    unittest.main()
