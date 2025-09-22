from typing import List
import unittest


class Solution:
    def lengthOfLastWord(self, s:str)->int:
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == " ":
                if count == 0:
                    continue
                return count
            count+=1
        return count


class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "Hello World"
        expected = 5
        self.assertEqual(self.solution.lengthOfLastWord(s), expected)

    def test_example2(self):
        s = "   fly me   to   the moon  "
        expected = 4
        self.assertEqual(self.solution.lengthOfLastWord(s), expected)

    def test_example3(self):
        s = "luffy is still joyboy"
        expected = 6
        self.assertEqual(self.solution.lengthOfLastWord(s), expected)

    def test_single_word(self):
        s = "word"
        expected = 4
        self.assertEqual(self.solution.lengthOfLastWord(s), expected)

    def test_trailing_spaces(self):
        s = "word   "
        expected = 4
        self.assertEqual(self.solution.lengthOfLastWord(s), expected)

    def test_leading_spaces(self):
        s = "   word"
        expected = 4
        self.assertEqual(self.solution.lengthOfLastWord(s), expected)

    def test_all_spaces(self):
        s = "     "
        expected = 0
        self.assertEqual(self.solution.lengthOfLastWord(s), expected)

    def test_empty_string(self):
        s = ""
        expected = 0
        self.assertEqual(self.solution.lengthOfLastWord(s), expected)

    def test_multiple_spaces_between_words(self):
        s = "a  b   c"
        expected = 1
        self.assertEqual(self.solution.lengthOfLastWord(s), expected)

    def test_word_with_punctuation(self):
        s = "hello world!"
        expected = 6
        self.assertEqual(self.solution.lengthOfLastWord(s), expected)

if __name__ == "__main__":
    unittest.main()
