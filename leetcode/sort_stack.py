import unittest
from typing import List, Optional
from collections import deque



class Solution:
    def __init__(self, stack:List[int]=[]):
        self.stack = stack
        # [5  4 3 1]  val = 3
        # newVal = 4 tmp = 1 
    def push(self, val:int)->None:
        if self.isEmpty():
            self.stack.append(val)
            return
        tmp:List[int]= []
        
        while self.stack:
            newVal = self.peek()

            if newVal >= val:
                break
            tmp.append(self.pop())
        
        self.stack.append(val)
        while tmp:
            self.stack.append(tmp.pop())

        

    def pop(self)->Optional[int]:
        if self.isEmpty():
            return
        
        return self.stack.pop()

    def peek(self)->Optional[int]:
        if self.isEmpty():
            return None
        return self.stack[-1]

    def isEmpty(self)-> bool:
        return not self.stack
    

class TestSortStack(unittest.TestCase):
    def test_empty_stack_behavior(self):
        s = Solution(stack=[])
        self.assertTrue(s.isEmpty())
        self.assertIsNone(s.peek())
        self.assertIsNone(s.pop())

    def test_push_maintains_smallest_on_top(self):
        s = Solution(stack=[])
        s.push(3)
        s.push(1)
        s.push(2)
        s.push(4)
        # Smallest on top (end of list), largest at bottom (index 0)
        self.assertEqual(s.stack, [4, 3, 2, 1])
        self.assertEqual(s.peek(), 1)

    def test_pop_returns_increasing_order(self):
        s = Solution(stack=[])
        for v in [5, 3, 4, 1, 2]:
            s.push(v)
        popped = []
        while not s.isEmpty():
            popped.append(s.pop())
        self.assertEqual(popped, [1, 2, 3, 4, 5])

    def test_duplicates_are_supported(self):
        s = Solution(stack=[])
        for v in [3, 1, 2, 2, 1]:
            s.push(v)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.stack, [3, 2, 2, 1, 1])
        popped = []
        while not s.isEmpty():
            popped.append(s.pop())
        self.assertEqual(popped, [1, 1, 2, 2, 3])

    def test_push_greater_than_all_values(self):
        s = Solution()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        # 4 should be inserted and end up at the bottom
        self.assertEqual(s.stack, [4, 3, 2, 1])
        self.assertEqual(s.peek(), 1)


if __name__ == '__main__':
    unittest.main()