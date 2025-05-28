import unittest
class Solution:
    def longestLengthSubstring(self, s:str)->int:
        res = 0
        l = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)

        return res


class TestLongestSubstring(unittest.TestCase):
    def test_example1(self):
        s = "abcabcbb"
        expected = 3
        solution = Solution()
        result = solution.longestLengthSubstring(s)
        self.assertEqual(result, expected)

    def test_example2(self):
        s = "bbbbb"
        expected = 1
        solution = Solution()
        result = solution.longestLengthSubstring(s)
        self.assertEqual(result, expected)

    def test_example3(self):
        s = "pwwkew"
        expected = 3
        solution = Solution()
        result = solution.longestLengthSubstring(s)
        self.assertEqual(result, expected)

    def test_empty_string(self):
        s = ""
        expected = 0
        solution = Solution()
        result = solution.longestLengthSubstring(s)
        self.assertEqual(result, expected)

    def test_single_character(self):
        s = "a"
        expected = 1
        solution = Solution()
        result = solution.longestLengthSubstring(s)
        self.assertEqual(result, expected)

    def test_all_unique(self):
        s = "abcdef"
        expected = 6
        solution = Solution()
        result = solution.longestLengthSubstring(s)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

