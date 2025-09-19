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
    

class TestFirstOccurrence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_base(self):
        solution = Solution()
        self.assertEqual(self.solution.strStr("firstdadsad", "sad"), 8)

if __name__ == "__main__":
    unittest.main()
