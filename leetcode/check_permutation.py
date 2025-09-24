import unittest

class Solution:
    # Solution nlogn
    def checkPermutation2(self, s1:str, s2:str)-> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)

        return s1 == s2
    def checkPermutation(self, s1:str, s2:str)-> bool:
        #  aab {a: 2, b: 1}, baa {a:2, b:1}
        hasha = {}
        hashb = {}
        for i,val in enumerate(s1):
            if not val in hasha:
                hasha[val] = 1
            else:
                hasha[val] +=1
        
        for i,val in enumerate(s2):
            if not val in hashb:
                hashb[val] = 1
            else:
                hashb[val]+=1


        return hasha == hashb



class TestCheckPermutation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_permutations(self):
        self.assertTrue(self.solution.checkPermutation("abc", "bca"))
        self.assertTrue(self.solution.checkPermutation("aabbcc", "abcabc"))
        self.assertTrue(self.solution.checkPermutation("", ""))
        self.assertTrue(self.solution.checkPermutation("a", "a"))
        self.assertTrue(self.solution.checkPermutation("123", "321"))

    def test_not_permutations(self):
        self.assertFalse(self.solution.checkPermutation("abc", "ab"))
        self.assertFalse(self.solution.checkPermutation("abc", "abd"))
        self.assertFalse(self.solution.checkPermutation("aabbcc", "aabbc"))
        self.assertFalse(self.solution.checkPermutation("abc", "def"))
        self.assertFalse(self.solution.checkPermutation("a", "b"))

    def test_case_sensitivity(self):
        self.assertFalse(self.solution.checkPermutation("abc", "Abc"))
        self.assertFalse(self.solution.checkPermutation("aBc", "abc"))

    def test_special_characters(self):
        self.assertTrue(self.solution.checkPermutation("!@#", "#!@"))
        self.assertFalse(self.solution.checkPermutation("!@#", "!@!"))

if __name__ == "__main__":
    unittest.main()
