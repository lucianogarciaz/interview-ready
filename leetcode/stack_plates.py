import unittest
from typing import List, Optional

class Solution:
    def __init__(self, capacity:int = 0):
        self.stacks:List[List[int]] = []
        self.capacity:int = capacity

    def push(self, val:int)->None:
        if not self.stacks:
            self.stacks.append([val])
            return

        stack = self.stacks[-1]
        if len(stack) < self.capacity:
            stack.append(val)
            self.stacks[-1] = stack
            return
        
        self.stacks.append([val])
        return

    def pop(self)->None:
        if not self.stacks:
            return None
        stack = self.stacks[-1]
        stack.pop()
        if len(stack) == 0:
            self.stacks.pop()
            return
        self.stacks[-1] = stack
    
    def peak(self)->Optional[int]:
        if not self.stacks:
            return None
        return self.stacks[-1][-1]


    def popAt(self, index:int)->None:
        if not self.stacks or index >= len(self.stacks):
            return None
        stack = self.stacks[index]
        stack.pop()
        if len(stack) == 0:
            self.stacks = self.stacks[:index] + self.stacks[index+1:]
            return 
        self.stacks[index] = stack


class TestStackOfPlates(unittest.TestCase):
    def test_empty_stack(self):
        """Test behavior when stack is empty"""
        stack = Solution(capacity=3)
        
        self.assertIsNone(stack.peak())
        self.assertIsNone(stack.pop())
        self.assertEqual(len(stack.stacks), 0)
    
    def test_single_stack_basic_operations(self):
        """Test basic operations on a single stack"""
        stack = Solution(capacity=3)
        
        # Push elements
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        self.assertEqual(len(stack.stacks), 1)
        self.assertEqual(stack.stacks[0], [1, 2, 3])
        self.assertEqual(stack.peak(), 3)
        
        # Pop elements
        stack.pop()
        self.assertEqual(stack.stacks[0], [1, 2])
        self.assertEqual(stack.peak(), 2)
        
        stack.pop()
        self.assertEqual(stack.stacks[0], [1])
        self.assertEqual(stack.peak(), 1)
        
        stack.pop()
        self.assertEqual(len(stack.stacks), 0)
        self.assertIsNone(stack.peak())
    
    def test_multiple_stacks_creation(self):
        """Test that new stacks are created when capacity is exceeded"""
        stack = Solution(capacity=2)
        
        # Push elements that exceed capacity
        stack.push(1)
        stack.push(2)
        stack.push(3)  # Should create new stack
        stack.push(4)
        stack.push(5)  # Should create third stack
        
        self.assertEqual(len(stack.stacks), 3)
        self.assertEqual(stack.stacks[0], [1, 2])
        self.assertEqual(stack.stacks[1], [3, 4])
        self.assertEqual(stack.stacks[2], [5])
        self.assertEqual(stack.peak(), 5)
    
    def test_pop_from_multiple_stacks(self):
        """Test popping from multiple stacks"""
        stack = Solution(capacity=2)
        
        # Create multiple stacks
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        
        self.assertEqual(len(stack.stacks), 3)
        self.assertEqual(stack.peak(), 5)
        
        # Pop from last stack
        stack.pop()
        self.assertEqual(len(stack.stacks), 2)
        self.assertEqual(stack.peak(), 4)
        
        # Pop until empty
        stack.pop()
        self.assertEqual(len(stack.stacks), 2)
        self.assertEqual(stack.peak(), 3)
        
        stack.pop()
        self.assertEqual(len(stack.stacks), 1)
        self.assertEqual(stack.peak(), 2)
        
        stack.pop()
        self.assertEqual(len(stack.stacks), 1)
        self.assertEqual(stack.peak(), 1)
        
        stack.pop()
        self.assertEqual(len(stack.stacks), 0)
        self.assertIsNone(stack.peak())
    
    def test_capacity_one(self):
        """Test behavior with capacity of 1"""
        stack = Solution(capacity=1)
        
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        self.assertEqual(len(stack.stacks), 3)
        self.assertEqual(stack.stacks[0], [1])
        self.assertEqual(stack.stacks[1], [2])
        self.assertEqual(stack.stacks[2], [3])
        
        stack.pop()
        self.assertEqual(len(stack.stacks), 2)
        self.assertEqual(stack.peak(), 2)
    
    def test_zero_capacity(self):
        """Test behavior with capacity of 0"""
        stack = Solution(capacity=0)
        
        # With capacity 0, each push should create a new stack
        stack.push(1)
        stack.push(2)
        
        self.assertEqual(len(stack.stacks), 2)
        self.assertEqual(stack.stacks[0], [1])
        self.assertEqual(stack.stacks[1], [2])
    
    def test_large_capacity(self):
        """Test behavior with large capacity"""
        stack = Solution(capacity=5)
        
        # Push 7 elements - should fit in 2 stacks
        for i in range(1, 8):
            stack.push(i)
        
        self.assertEqual(len(stack.stacks), 2)
        self.assertEqual(stack.stacks[0], [1, 2, 3, 4, 5])
        self.assertEqual(stack.stacks[1], [6, 7])
        self.assertEqual(stack.peak(), 7)
    
    def test_alternating_push_pop(self):
        """Test alternating push and pop operations"""
        stack = Solution(capacity=3)
        
        # Push some elements
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)  # Creates new stack
        
        self.assertEqual(len(stack.stacks), 2)
        self.assertEqual(stack.peak(), 4)
        
        # Pop from new stack
        stack.pop()
        self.assertEqual(len(stack.stacks), 1)
        self.assertEqual(stack.peak(), 3)
        
        # Push more
        stack.push(5)
        stack.push(6)
        stack.push(7)  # Creates new stack again
        
        self.assertEqual(len(stack.stacks), 2)
        self.assertEqual(stack.peak(), 7)
    
    def test_peek_after_operations(self):
        """Test peek behavior after various operations"""
        stack = Solution(capacity=2)
        
        self.assertIsNone(stack.peak())
        
        stack.push(1)
        self.assertEqual(stack.peak(), 1)
        
        stack.push(2)
        self.assertEqual(stack.peak(), 2)
        
        stack.push(3)  # New stack
        self.assertEqual(stack.peak(), 3)
        
        stack.pop()
        self.assertEqual(stack.peak(), 2)
        
        stack.pop()
        self.assertEqual(stack.peak(), 1)
        
        stack.pop()
        self.assertIsNone(stack.peak())
    
    def test_popAt_empty_stack(self):
        """Test popAt on empty stack"""
        stack = Solution(capacity=3)
        
        self.assertIsNone(stack.popAt(0))
        self.assertIsNone(stack.popAt(1))
        self.assertIsNone(stack.popAt(-1))
    
    def test_popAt_invalid_index(self):
        """Test popAt with invalid indices"""
        stack = Solution(capacity=2)
        
        # Add some elements
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        # Test invalid indices
        self.assertIsNone(stack.popAt(2))  # Index out of range
        self.assertIsNone(stack.popAt(5))  # Index out of range
        self.assertIsNone(stack.popAt(-2)) # Negative index (if not supported)
    
    def test_popAt_valid_indices(self):
        """Test popAt with valid indices"""
        stack = Solution(capacity=2)
        
        # Create multiple stacks: [[1,2], [3,4], [5]]
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        
        self.assertEqual(len(stack.stacks), 3)
        self.assertEqual(stack.stacks[0], [1, 2])
        self.assertEqual(stack.stacks[1], [3, 4])
        self.assertEqual(stack.stacks[2], [5])
        
        # Pop from middle stack (index 1)
        stack.popAt(1)
        self.assertEqual(stack.stacks[1], [3])
        self.assertEqual(len(stack.stacks), 3)
        
        # Pop from first stack (index 0)
        stack.popAt(0)
        self.assertEqual(stack.stacks[0], [1])
        
        # Pop from last stack (index 2)
        stack.popAt(2)
        self.assertEqual(len(stack.stacks), 2)  # Empty stack removed
        self.assertEqual(stack.stacks[1], [3])
    
    def test_popAt_removes_empty_stacks(self):
        """Test that popAt removes empty stacks"""
        stack = Solution(capacity=2)
        
        # Create stacks: [[1,2], [3,4], [5]]
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        
        self.assertEqual(len(stack.stacks), 3)
        
        # Pop all elements from middle stack
        stack.popAt(1)  # Remove 4 from [3,4]
        self.assertEqual(stack.stacks[1], [3])
        
        stack.popAt(1)  # Remove 3 from [3], should remove entire stack
        self.assertEqual(len(stack.stacks), 2)
        self.assertEqual(stack.stacks[0], [1, 2])
        self.assertEqual(stack.stacks[1], [5])
        
        # Pop from first stack
        stack.popAt(0)  # Remove 2 from [1,2]
        stack.popAt(0)  # Remove 1 from [1], should remove entire stack
        self.assertEqual(len(stack.stacks), 1)
        self.assertEqual(stack.stacks[0], [5])
    
    def test_popAt_vs_regular_pop(self):
        """Test interaction between popAt and regular pop"""
        stack = Solution(capacity=2)
        
        # Create stacks: [[1,2], [3,4], [5]]
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        
        # Pop from specific stack
        stack.popAt(1)  # Remove 4 from middle stack
        self.assertEqual(stack.stacks[1], [3])
        self.assertEqual(stack.peak(), 5)  # Regular peek should still work
        
        # Regular pop should still work
        stack.pop()
        self.assertEqual(len(stack.stacks), 2)
        self.assertEqual(stack.peak(), 3)
    
    def test_popAt_single_stack(self):
        """Test popAt on single stack"""
        stack = Solution(capacity=3)
        
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        self.assertEqual(len(stack.stacks), 1)
        self.assertEqual(stack.stacks[0], [1, 2, 3])
        
        # Pop from single stack
        stack.popAt(0)
        self.assertEqual(stack.stacks[0], [1, 2])
        self.assertEqual(stack.peak(), 2)
        
        stack.popAt(0)
        self.assertEqual(stack.stacks[0], [1])
        self.assertEqual(stack.peak(), 1)
        
        stack.popAt(0)
        self.assertEqual(len(stack.stacks), 0)
        self.assertIsNone(stack.peak())
    
    def test_popAt_capacity_one(self):
        """Test popAt with capacity 1"""
        stack = Solution(capacity=1)
        
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        self.assertEqual(len(stack.stacks), 3)
        
        # Each popAt should remove entire stack
        stack.popAt(1)  # Remove stack [2]
        self.assertEqual(len(stack.stacks), 2)
        self.assertEqual(stack.stacks[0], [1])
        self.assertEqual(stack.stacks[1], [3])
        
        stack.popAt(0)  # Remove stack [1]
        self.assertEqual(len(stack.stacks), 1)
        self.assertEqual(stack.stacks[0], [3])
    
    def test_popAt_edge_cases(self):
        """Test popAt edge cases"""
        stack = Solution(capacity=2)
        
        # Test with single element
        stack.push(1)
        stack.popAt(0)
        self.assertEqual(len(stack.stacks), 0)
        
        # Test with two elements in one stack
        stack.push(1)
        stack.push(2)
        stack.popAt(0)  # Remove 2
        self.assertEqual(len(stack.stacks), 1)
        self.assertEqual(stack.stacks[0], [1])
        self.assertEqual(stack.peak(), 1)
        
        stack.popAt(0)  # Remove 1
        self.assertEqual(len(stack.stacks), 0)
        self.assertIsNone(stack.peak())


if __name__ == '__main__':
    unittest.main()