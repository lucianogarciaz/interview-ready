import unittest
#  s1: ab  s2: aba -> true (action = insert)
#  s1: aba  s2: aa -> true (action remove an element)
#  s1: aba  s2: cba -> true (edit)
#  s1: saba  s2: casa -> false (two edits)
class Solution:
    def isOneAway(self, s1:str, s2: str)->bool:
        ls1 = len(s1)
        ls2 = len(s2)
        if abs(ls1 - ls2) >1:
            return False
        i = 0
        j = 0
        moves =0
        while i <ls1 and j<ls2:
            if s1[i] == s2[j]:
                i+=1
                j+=1
                continue
            moves +=1
            if ls1 > ls2:
                j +=1
            elif ls1 < ls2:
                i+=1
            else:
                i+=1
                j+=1
            
        return moves <= 1
class TestIsOneAway(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_insert(self):
        self.assertTrue(self.solution.isOneAway("ab", "aba"))
        self.assertTrue(self.solution.isOneAway("abc", "ab"))
        self.assertTrue(self.solution.isOneAway("a", ""))
        self.assertTrue(self.solution.isOneAway("", "a"))

    def test_remove(self):
        self.assertTrue(self.solution.isOneAway("aba", "aa"))
        self.assertTrue(self.solution.isOneAway("abc", "ac"))
        self.assertTrue(self.solution.isOneAway("a", ""))
        self.assertTrue(self.solution.isOneAway("", "a"))

    def test_edit(self):
        self.assertTrue(self.solution.isOneAway("aba", "cba"))
        self.assertTrue(self.solution.isOneAway("pale", "bale"))
        self.assertTrue(self.solution.isOneAway("pale", "pate"))
        self.assertTrue(self.solution.isOneAway("pale", "pale"))

    def test_false_cases(self):
        self.assertFalse(self.solution.isOneAway("saba", "casa"))
        self.assertFalse(self.solution.isOneAway("abc", "def"))
        self.assertFalse(self.solution.isOneAway("abc", "abcdde"))
        self.assertFalse(self.solution.isOneAway("abc", "a"))

    def test_empty_strings(self):
        self.assertTrue(self.solution.isOneAway("", ""))
        self.assertTrue(self.solution.isOneAway("a", ""))
        self.assertTrue(self.solution.isOneAway("", "a"))
        self.assertFalse(self.solution.isOneAway("ab", ""))

    def test_long_strings(self):
        self.assertTrue(self.solution.isOneAway("abcdef", "abcdeg"))
        self.assertTrue(self.solution.isOneAway("abcdef", "abcdf"))
        self.assertFalse(self.solution.isOneAway("abcdef", "abqxyz"))

if __name__ == "__main__":
    unittest.main()
