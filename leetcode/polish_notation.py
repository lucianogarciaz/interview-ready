from typing import List
class Solution:
    def evalRPN(self, tokens: List[str])-> int:
        stack: List[int]=[]
        for t in tokens:
            if t == "+":
                stack.append(stack.pop()+stack.pop())
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif t == "*":
                stack.append(stack.pop()*stack.pop())
            elif t == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(t))
        
        return stack.pop()
    
import unittest

class TestEvalRPN(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_basic_operations(self):
        tokens = ["2", "1", "+", "3", "*"]
        self.assertEqual(self.solution.evalRPN(tokens), 9)
        
        tokens = ["4", "13", "5", "/", "+"]
        self.assertEqual(self.solution.evalRPN(tokens), 6)
    
    def test_division_with_negative(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(self.solution.evalRPN(tokens), 22)
    
    def test_single_number(self):
        tokens = ["42"]
        self.assertEqual(self.solution.evalRPN(tokens), 42)
    
    def test_negative_numbers(self):
        tokens = ["-2", "3", "+"]
        self.assertEqual(self.solution.evalRPN(tokens), 1)
    
    def test_division_rounding(self):
        tokens = ["7", "2", "/"]
        self.assertEqual(self.solution.evalRPN(tokens), 3)  # Should round down to 3
    
    def test_complex_expression(self):
        tokens = ["4", "3", "-", "5", "*"]
        self.assertEqual(self.solution.evalRPN(tokens), 5)  # (4-3)*5 = 5

if __name__ == '__main__':
    unittest.main()
        