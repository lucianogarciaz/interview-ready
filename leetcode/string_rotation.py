import unittest

class Solution:
    def stringRotation(self, s:str, goal:str)->bool:
        n = len(s)
        if n!= len(goal):
            return False
        if s == "":
            return True
        
        for i in range(n):
            if s == goal:
                return True
            tmp = s[-1] # last element 
            s = s[:-1]
            s = tmp + s
        
        return False

class TestStringRotation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_rotation(self):
        s = "abcde"
        goal = "cdeab"
        self.assertTrue(self.solution.stringRotation(s, goal))

    def test_no_rotation(self):
        s = "abcde"
        goal = "abced"
        self.assertFalse(self.solution.stringRotation(s, goal))

    def test_same_string(self):
        s = "abcde"
        goal = "abcde"
        self.assertTrue(self.solution.stringRotation(s, goal))

    def test_empty_strings(self):
        s = ""
        goal = ""
        self.assertTrue(self.solution.stringRotation(s, goal))

    def test_different_lengths(self):
        s = "abc"
        goal = "abcd"
        self.assertFalse(self.solution.stringRotation(s, goal))

    def test_single_character(self):
        s = "a"
        goal = "a"
        self.assertTrue(self.solution.stringRotation(s, goal))

    def test_single_character_false(self):
        s = "a"
        goal = "b"
        self.assertFalse(self.solution.stringRotation(s, goal))

    def test_rotation_full_cycle(self):
        s = "waterbottle"
        goal = "erbottlewat"
        self.assertTrue(self.solution.stringRotation(s, goal))

if __name__ == "__main__":
    unittest.main()
