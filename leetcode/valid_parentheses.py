from typing import List
import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.
        
        Args:
            s: A string containing only parentheses characters
            
        Returns:
            True if the input string is valid, False otherwise.
            
        A string is valid if:
        - Open brackets must be closed by the same type of brackets.
        - Open brackets must be closed in the correct order.
        - Every close bracket has a corresponding open bracket of the same type.
        """
        valid = {'(':')','[':']','{':'}'}
        stack=[]
        for i in s:
            if i in valid:
                stack.append(i)
                continue
            
            if not stack:
                return False
            
            peak = stack[-1]
            if peak in valid and valid[peak]==i:
                stack.pop()
        
        return not stack

class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        s = "()"
        self.assertTrue(self.solution.isValid(s))
    
    def test_example2(self):
        s = "()[]{}"
        self.assertTrue(self.solution.isValid(s))
    
    def test_example3(self):
        s = "(]"
        self.assertFalse(self.solution.isValid(s))
    
    def test_nested_valid(self):
        s = "([{}])"
        self.assertTrue(self.solution.isValid(s))
    
    def test_unmatched_open(self):
        s = "("
        self.assertFalse(self.solution.isValid(s))
    
    def test_unmatched_close(self):
        s = ")"
        self.assertFalse(self.solution.isValid(s))
    
    def test_mixed_invalid(self):
        s = "([)]"
        self.assertFalse(self.solution.isValid(s))
    
    def test_empty_string(self):
        s = ""
        self.assertTrue(self.solution.isValid(s))
    
    def test_complex_valid(self):
        s = "{[]}"
        self.assertTrue(self.solution.isValid(s))
    
    def test_complex_invalid(self):
        s = "((("
        self.assertFalse(self.solution.isValid(s))

if __name__ == '__main__':
    unittest.main() 