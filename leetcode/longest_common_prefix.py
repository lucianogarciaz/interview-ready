import unittest
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            result = ""
            if len(strs)==0:
                return result
            strs = sorted(strs)
            for i,val in enumerate(strs[0]):
                j=1
                while j < len(strs):
                    if strs[j][i]!=val:
                        return result
                    j+=1
                
                result += val
            
            return result

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        
        first = strs[0]

        for i in range(len(first)):
            val = first[i]
            for s in strs[1:]:
                if i == len(s) or val!=s[i]:
                    return first[:i]

        return first


class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longestCommonPrefix_basic(self):
        strs = ["flower","flow","flight"]
        expected = "fl"
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)
        self.assertEqual(self.solution.longestCommonPrefix2(strs), expected)

    def test_longestCommonPrefix_no_common(self):
        strs = ["dog","racecar","car"]
        expected = ""
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)
        self.assertEqual(self.solution.longestCommonPrefix2(strs), expected)

    def test_longestCommonPrefix_empty_list(self):
        strs = []
        expected = ""
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)
        self.assertEqual(self.solution.longestCommonPrefix2(strs), expected)

    def test_longestCommonPrefix_single_string(self):
        strs = ["alone"]
        expected = "alone"
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)
        self.assertEqual(self.solution.longestCommonPrefix2(strs), expected)

    def test_longestCommonPrefix_identical_strings(self):
        strs = ["repeat", "repeat", "repeat"]
        expected = "repeat"
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)
        self.assertEqual(self.solution.longestCommonPrefix2(strs), expected)

    def test_longestCommonPrefix_partial_overlap(self):
        strs = ["interview", "internet", "internal", "interval"]
        expected = "inter"
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)
        self.assertEqual(self.solution.longestCommonPrefix2(strs), expected)

    def test_longestCommonPrefix_empty_string_in_list(self):
        strs = ["", "abc", "abcd"]
        expected = ""
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)
        self.assertEqual(self.solution.longestCommonPrefix2(strs), expected)

    def test_longestCommonPrefix_all_empty_strings(self):
        strs = ["", "", ""]
        expected = ""
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)
        self.assertEqual(self.solution.longestCommonPrefix2(strs), expected)

    def test_longestCommonPrefix_prefix_is_whole_first_word(self):
        strs = ["a", "ab", "abc"]
        expected = "a"
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)
        self.assertEqual(self.solution.longestCommonPrefix2(strs), expected)

if __name__ == '__main__':
    unittest.main()
