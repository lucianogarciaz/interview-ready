import unittest
class Solution:
    #  "firstsadbut"  "sad"  
    #  Space = O(1)
    #  Time = O(n)
    #  len neddle < len haystack : -1
    def strStr(self, haystack: str, needle: str)-> int:
        m = len(needle)
        l = 0
        r = l + m
        while r<=len(haystack):
            s = ''.join(haystack[l:r])
            if s == needle:
                return l
            l+=1
            r+=1
        
        return -1
 
    def setStr2(self, haystack:str, needle:str)->int:
        for i in range(len(haystack)):
            if len(needle)+i > len(haystack):
                return -1
            if haystack[i:i+len(needle)]==needle:
                return i
        
        return -1


class TestFirstOccurrence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_base(self):
        solution = Solution()
        self.assertEqual(self.solution.setStr2("firstdadsad", "sad"), 8)
    def test_found_at_start(self):
        self.assertEqual(self.solution.setStr2("sadbutsad", "sad"), 0)

    def test_found_at_end(self):
        self.assertEqual(self.solution.setStr2("sadbutsad", "sad"), 0)  # first occurrence

    def test_not_found(self):
        self.assertEqual(self.solution.setStr2("leetcode", "leeto"), -1)

    def test_single_char_match(self):
        self.assertEqual(self.solution.setStr2("a", "a"), 0)

    def test_single_char_not_found(self):
        self.assertEqual(self.solution.setStr2("ab", "b"), 1)
        self.assertEqual(self.solution.setStr2("ab", "c"), -1)

    def test_needle_longer_than_haystack(self):
        self.assertEqual(self.solution.setStr2("a", "ab"), -1)

    def test_empty_needle(self):
        self.assertEqual(self.solution.setStr2("abc", ""), 0)

    def test_empty_haystack(self):
        self.assertEqual(self.solution.setStr2("", "a"), -1)

    def test_both_empty(self):
        self.assertEqual(self.solution.setStr2("", ""), -1)

if __name__ == "__main__":
    unittest.main()
