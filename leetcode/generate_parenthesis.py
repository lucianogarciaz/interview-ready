from typing import List

class Solution:
    def generateParenthesis(self, n: int)->List[str]:
        cur:List[str]=[]
        res:List[str]=[]
        def backtracking(open:int, close: int):
            if open==close==n:
                res.append(''.join(cur))
                return
            if open < n:
                cur.append('(')
                backtracking(open+1, close)
                cur.pop()
            if close<open:
                cur.append(')')
                backtracking(open, close+1)
                cur.pop()
        backtracking(0,0)

        return res
    

import unittest

class TestGenerateParenthesis(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_n_equals_1(self):
        n = 1
        expected = ["()"]
        self.assertEqual(sorted(self.solution.generateParenthesis(n)), sorted(expected))
    
    def test_n_equals_2(self):
        n = 2
        expected = ["(())", "()()"]
        self.assertEqual(sorted(self.solution.generateParenthesis(n)), sorted(expected))
    
    def test_n_equals_3(self):
        n = 3
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertEqual(sorted(self.solution.generateParenthesis(n)), sorted(expected))
    
    def test_n_equals_0(self):
        n = 0
        expected = [""]
        self.assertEqual(sorted(self.solution.generateParenthesis(n)), sorted(expected))
    
    def test_n_equals_4(self):
        n = 4
        result = self.solution.generateParenthesis(n)
        # Verify length of result
        self.assertEqual(len(result), 14)
        # Verify all strings are valid parentheses
        for s in result:
            self.assertTrue(self.isValid(s))
    
    def isValid(self, s: str) -> bool:
        """Helper method to verify if a string contains valid parentheses"""
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

if __name__ == '__main__':
    unittest.main()