import unittest

class Solution:
    def stringCompression(self, s:str)->str:
        s = s.lower()
        # aaabd   a3b1c1d3   edge cases like when fast reaches the last element
        # l       f     lv      fv     count    res
        # 0       1     a       a       2
        # 0       2     a       a       3
        # 0       3     a       b       1       a3
        # 3       4     b       d       1       b1
        # 4       5

        res = ""
        length = len(s)
        f = 1
        l = 0
        count = 1
        while f < length:
            lv = s[l]
            lf = s[f]
            if lv == lf:
                count +=1  
                f+=1
                continue
            res += f'{lv}{count}'
            count = 1
            l = f
            f +=1
        if length > 0:
            res += f'{s[l]}{count}'
        return res if len(res)<len(s) else s

class TestStringCompression(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic(self):
        self.assertEqual(self.solution.stringCompression("aaabbc"), "aaabbc")
        self.assertEqual(self.solution.stringCompression("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(self.solution.stringCompression("abc"), "abc")
        self.assertEqual(self.solution.stringCompression("a"), "a")
        self.assertEqual(self.solution.stringCompression(""), "")

    def test_single_character(self):
        self.assertEqual(self.solution.stringCompression("z"), "z")
        self.assertEqual(self.solution.stringCompression("zzzz"), "z4")

    def test_mixed_case(self):
        self.assertEqual(self.solution.stringCompression("AAAbbCC"), "a3b2c2")
        self.assertEqual(self.solution.stringCompression("aAaA"), "a4")

    def test_all_unique(self):
        self.assertEqual(self.solution.stringCompression("abcdef"), "abcdef")

    def test_all_same(self):
        self.assertEqual(self.solution.stringCompression("bbbbbb"), "b6")

    def test_edge_cases(self):
        self.assertEqual(self.solution.stringCompression("aabbaa"), "aabbaa")
        self.assertEqual(self.solution.stringCompression("aaabbccdd"), "a3b2c2d2")
        self.assertEqual(self.solution.stringCompression("a"*100), "a100")

if __name__ == "__main__":
    unittest.main()
