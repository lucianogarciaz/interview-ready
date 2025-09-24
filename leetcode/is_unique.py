import unittest

class Solution:
    def isUnique(self, s:str)->bool:
        # abcd : true -> simplest solution is to add a dict and add all values. if one of them already exists, then return false solution o(n)
        # without aditional data structures we cant because most sorting algo uses aditional data structures
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    return False
        
        return True

    def isUniqueWAditionalDS(self, s:str)->bool:
        myDict = {}
        for i in range(len(s)):
            myDict[s[i]] = s[i]

        for i in range(len(s)):
            if 



class TestIsUnique(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_unique_characters(self):
        self.assertTrue(self.solution.isUnique("abcd"))
        self.assertTrue(self.solution.isUnique(""))

    def test_duplicate_characters(self):
        self.assertFalse(self.solution.isUnique("aabc"))
        self.assertFalse(self.solution.isUnique("abcda"))
        self.assertFalse(self.solution.isUnique("aa"))

    def test_single_character(self):
        self.assertTrue(self.solution.isUnique("a"))

    def test_special_characters(self):
        self.assertTrue(self.solution.isUnique("a!b@c#"))
        self.assertFalse(self.solution.isUnique("a!b@c#a"))

    def test_numbers(self):
        self.assertTrue(self.solution.isUnique("123456"))
        self.assertFalse(self.solution.isUnique("1123456"))

if __name__ == "__main__":
    unittest.main()