from typing import List
import unittest

class MinStack:
    def __init__(self):
        self.min: List[int] = []
        self.stack: List[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = self.getMin()
        if not self.min or minVal >= val :
            self.min.append(val)

    def pop(self) -> None:
        rEl = self.stack.pop()
        minVal = self.getMin()
        if minVal == rEl:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min:
            return None
        return self.min[-1]

class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.min_stack = MinStack()
    
    def test_push_and_top(self):
        self.min_stack.push(5)
        self.assertEqual(self.min_stack.top(), 5)
        self.min_stack.push(3)
        self.assertEqual(self.min_stack.top(), 3)
    
    def test_pop(self):
        self.min_stack.push(5)
        self.min_stack.push(3)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.top(), 5)
    
    def test_get_min(self):
        self.min_stack.push(5)
        self.assertEqual(self.min_stack.getMin(), 5)
        self.min_stack.push(3)
        self.assertEqual(self.min_stack.getMin(), 3)
        self.min_stack.push(7)
        self.assertEqual(self.min_stack.getMin(), 3)
    
    def test_empty_stack(self):
        self.assertIsNone(self.min_stack.getMin())
        self.min_stack.push(1)
        self.min_stack.pop()
        self.assertIsNone(self.min_stack.getMin())
    
    def test_duplicate_min_values(self):
        self.min_stack.push(3)
        self.min_stack.push(3)
        self.assertEqual(self.min_stack.getMin(), 3)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.getMin(), 3)
    
    def test_negative_numbers(self):
        self.min_stack.push(-2)
        self.assertEqual(self.min_stack.getMin(), -2)
        self.min_stack.push(0)
        self.assertEqual(self.min_stack.getMin(), -2)
        self.min_stack.push(-3)
        self.assertEqual(self.min_stack.getMin(), -3)

if __name__ == '__main__':
    unittest.main()