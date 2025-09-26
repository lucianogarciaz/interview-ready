import unittest

class Solution:
    # 
    def isUnique(self, s:str)->bool:
        s = sorted(s)
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return False
        
        return True

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