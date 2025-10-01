from typing import List, Optional
import unittest

# min
class Solution:
    def __init__(self):
        self.min: List[int]=[]
        self.stack: List[int] = []
    
    def push(self, el:int)->None:
        # we add an element. if it's less than or equal to the current minimum, then add it to the min stack
        self.stack.append(el)
        minVal = self.getMin()
        if minVal is None or el <= minVal:
            self.min.append(el)

    def pop(self)->None:
        if not self.stack:
            return None
        peak = self.stack.pop()
        getMin = self.getMin()
        if peak is not None and getMin is not None and peak == getMin:
            self.min.pop()

        # return last element
        # we check if it's the same as the minimum, if its not we don't do nothing, if its we pop as well
    def peak(self)->Optional[int]:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self)->Optional[int]:
        if not self.min:
            return None
        return self.min[-1]


class TestSolution(unittest.TestCase):
    def test_empty_stack(self):
        """Test behavior when stack is empty"""
        stack = Solution()
        
        # Test that peak and getMin return None for empty stack
        self.assertIsNone(stack.peak())
        self.assertIsNone(stack.getMin())
        
        # Test that we can check if values are None
        peak_val = stack.peak()
        min_val = stack.getMin()
        
        self.assertTrue(peak_val is None)
        self.assertTrue(min_val is None)
        
        # Test the conditional check from your code
        if peak_val and min_val and peak_val == min_val:
            self.fail("This should not execute for empty stack")
    
    def test_single_element(self):
        """Test behavior with single element"""
        stack = Solution()
        stack.push(5)
        
        self.assertEqual(stack.peak(), 5)
        self.assertEqual(stack.getMin(), 5)
        
        # Test the conditional check
        peak_val = stack.peak()
        min_val = stack.getMin()
        if peak_val and min_val and peak_val == min_val:
            # This should execute for single element
            self.assertEqual(peak_val, 5)
            self.assertEqual(min_val, 5)
    
    def test_multiple_elements(self):
        """Test behavior with multiple elements"""
        stack = Solution()
        
        # Push elements in descending order
        stack.push(5)
        stack.push(3)
        stack.push(1)
        
        self.assertEqual(stack.getMin(), 1)
        self.assertEqual(stack.peak(), 1)
        
        # Test the conditional check - peak should equal min
        peak_val = stack.peak()
        min_val = stack.getMin()
        if peak_val and min_val and peak_val == min_val:
            self.assertEqual(peak_val, 1)
            self.assertEqual(min_val, 1)
    
    def test_pop_behavior(self):
        """Test pop behavior and minimum tracking"""
        stack = Solution()
        
        # Push elements
        stack.push(5)
        stack.push(3)
        stack.push(1)
        stack.push(2)  # This won't be added to min stack
        
        self.assertEqual(stack.getMin(), 1)
        self.assertEqual(stack.peak(), 2)
        
        # Test the conditional check - peak != min
        peak_val = stack.peak()
        min_val = stack.getMin()
        if peak_val and min_val and peak_val == min_val:
            self.fail("This should not execute since 2 != 1")
        
        # Pop the 2 (should not affect min stack)
        stack.pop()
        self.assertEqual(stack.peak(), 1)
        self.assertEqual(stack.getMin(), 1)
        
        # Now peak == min, test the conditional
        peak_val = stack.peak()
        min_val = stack.getMin()
        if peak_val and min_val and peak_val == min_val:
            self.assertEqual(peak_val, 1)
            self.assertEqual(min_val, 1)
        
        # Pop the 1 (should remove from min stack too)
        stack.pop()
        self.assertEqual(stack.peak(), 3)
        self.assertEqual(stack.getMin(), 3)
    
    def test_duplicate_minimums(self):
        """Test behavior with duplicate minimum values"""
        stack = Solution()
        
        stack.push(3)
        stack.push(1)
        stack.push(1)  # Duplicate minimum
        stack.push(2)
        
        self.assertEqual(stack.getMin(), 1)
        self.assertEqual(stack.peak(), 2)
        
        # Pop 2
        stack.pop()
        self.assertEqual(stack.peak(), 1)
        self.assertEqual(stack.getMin(), 1)
        
        # Pop first 1
        stack.pop()
        self.assertEqual(stack.peak(), 1)
        self.assertEqual(stack.getMin(), 1)
        
        # Pop second 1
        stack.pop()
        self.assertEqual(stack.peak(), 3)
        self.assertEqual(stack.getMin(), 3)
    
    def test_optional_return_checks(self):
        """Test different ways to check optional returns"""
        stack = Solution()
        
        # Empty stack
        peak = stack.peak()
        getMin = stack.getMin()
        
        # Method 1: Direct None comparison
        self.assertTrue(peak is None)
        self.assertTrue(getMin is None)
        
        # Method 2: Truthiness check
        self.assertFalse(peak)
        self.assertFalse(getMin)
        
        # Method 3: Using 'not'
        self.assertTrue(not peak)
        self.assertTrue(not getMin)
        
        # Add element and test again
        stack.push(42)
        peak = stack.peak()
        getMin = stack.getMin()
        
        # Now they should have values
        self.assertIsNotNone(peak)
        self.assertIsNotNone(getMin)
        self.assertTrue(peak)
        self.assertTrue(getMin)
        self.assertFalse(not peak)
        self.assertFalse(not getMin)
    
    def test_pop_empty_stack(self):
        """Test pop behavior on empty stack"""
        stack = Solution()
        
        # Should not raise an error when popping from empty stack
        stack.pop()
        stack.pop()
        stack.pop()
        
        # Stack should still be empty
        self.assertIsNone(stack.peak())
        self.assertIsNone(stack.getMin())
    
    def test_pop_minimum_tracking(self):
        """Test that pop correctly maintains minimum tracking"""
        stack = Solution()
        
        # Build stack: [5, 3, 1, 2]
        stack.push(5)  # min stack: [5]
        stack.push(3)  # min stack: [5, 3]
        stack.push(1)  # min stack: [5, 3, 1]
        stack.push(2)  # min stack: [5, 3, 1] (2 is not added)
        
        self.assertEqual(stack.peak(), 2)
        self.assertEqual(stack.getMin(), 1)
        
        # Pop 2 (not minimum, min stack unchanged)
        stack.pop()
        self.assertEqual(stack.peak(), 1)
        self.assertEqual(stack.getMin(), 1)
        
        # Pop 1 (is minimum, should remove from min stack)
        stack.pop()
        self.assertEqual(stack.peak(), 3)
        self.assertEqual(stack.getMin(), 3)
        
        # Pop 3 (is minimum, should remove from min stack)
        stack.pop()
        self.assertEqual(stack.peak(), 5)
        self.assertEqual(stack.getMin(), 5)
        
        # Pop 5 (is minimum, should remove from min stack)
        stack.pop()
        self.assertIsNone(stack.peak())
        self.assertIsNone(stack.getMin())
    
    def test_pop_duplicate_minimums(self):
        """Test pop behavior with duplicate minimum values"""
        stack = Solution()
        
        # Build stack: [5, 1, 1, 2]
        stack.push(5)  # min stack: [5]
        stack.push(1)  # min stack: [5, 1]
        stack.push(1)  # min stack: [5, 1, 1] (duplicate added)
        stack.push(2)  # min stack: [5, 1, 1] (2 not added)
        
        self.assertEqual(stack.peak(), 2)
        self.assertEqual(stack.getMin(), 1)
        
        # Pop 2 (not minimum)
        stack.pop()
        self.assertEqual(stack.peak(), 1)
        self.assertEqual(stack.getMin(), 1)
        
        # Pop first 1 (is minimum, removes one instance)
        stack.pop()
        self.assertEqual(stack.peak(), 1)
        self.assertEqual(stack.getMin(), 1)  # Still 1 (duplicate exists)
        
        # Pop second 1 (is minimum, removes last instance)
        stack.pop()
        self.assertEqual(stack.peak(), 5)
        self.assertEqual(stack.getMin(), 5)
    
    def test_pop_edge_cases(self):
        """Test edge cases for pop method"""
        stack = Solution()
        
        # Single element
        stack.push(42)
        self.assertEqual(stack.peak(), 42)
        self.assertEqual(stack.getMin(), 42)
        
        stack.pop()
        self.assertIsNone(stack.peak())
        self.assertIsNone(stack.getMin())
        
        # Multiple same elements
        stack.push(7)
        stack.push(7)
        stack.push(7)
        
        self.assertEqual(stack.peak(), 7)
        self.assertEqual(stack.getMin(), 7)
        
        # Pop all 7s
        stack.pop()  # min stack: [7, 7]
        self.assertEqual(stack.peak(), 7)
        self.assertEqual(stack.getMin(), 7)
        
        stack.pop()  # min stack: [7]
        self.assertEqual(stack.peak(), 7)
        self.assertEqual(stack.getMin(), 7)
        
        stack.pop()  # min stack: []
        self.assertIsNone(stack.peak())
        self.assertIsNone(stack.getMin())
    
    def test_user_approach_issues(self):
        """Test that demonstrates issues with the user's approach"""
        stack = Solution()
        
        # Test 1: Empty stack pop (should return None gracefully)
        result = stack.pop()
        self.assertIsNone(result)  # Should return None for empty stack
        
        # Test 2: The main issue - order of operations
        # Build stack: [5, 3, 1, 2]
        stack.push(5)  # min stack: [5]
        stack.push(3)  # min stack: [5, 3]
        stack.push(1)  # min stack: [5, 3, 1]
        stack.push(2)  # min stack: [5, 3, 1] (2 not added)
        
        # Pop 2 (not minimum)
        stack.pop()
        self.assertEqual(stack.peak(), 1)
        self.assertEqual(stack.getMin(), 1)
        self.assertEqual(len(stack.min), 3)  # Should still have 3 elements
        
        # Pop 1 (the minimum)
        stack.pop()
        self.assertEqual(stack.peak(), 3)
        self.assertEqual(stack.getMin(), 3)
        self.assertEqual(len(stack.min), 2)  # Should have 2 elements now
    
    def test_order_of_operations_issue(self):
        """Test that exposes the real issue with user's approach"""
        stack = Solution()
        
        # Build a specific scenario: [5, 3, 1, 1, 2]
        stack.push(5)  # min stack: [5]
        stack.push(3)  # min stack: [5, 3]
        stack.push(1)  # min stack: [5, 3, 1]
        stack.push(1)  # min stack: [5, 3, 1, 1] (duplicate)
        stack.push(2)  # min stack: [5, 3, 1, 1] (2 not added)
        
        # Pop 2 (not minimum)
        stack.pop()
        
        # Pop the first 1
        stack.pop()
        self.assertEqual(stack.stack, [5, 3, 1])
        self.assertEqual(stack.min, [5, 3, 1])
        self.assertEqual(stack.peak(), 1)
        self.assertEqual(stack.getMin(), 1)
        
        # Pop the second 1
        stack.pop()
        self.assertEqual(stack.stack, [5, 3])
        self.assertEqual(stack.min, [5, 3])
        self.assertEqual(stack.peak(), 3)
        self.assertEqual(stack.getMin(), 3)
    
    def test_comprehensive_comparison(self):
        """Comprehensive test comparing both approaches"""
        stack = Solution()
        stack.push(5)  # min: [5]
        stack.push(3)  # min: [5, 3]
        stack.push(1)  # min: [5, 3, 1]
        stack.push(1)  # min: [5, 3, 1, 1]
        stack.push(2)  # min: [5, 3, 1, 1]
        stack.push(0)  # min: [5, 3, 1, 1, 0]
        
        # Pop sequence: 0, 2, 1, 1, 3, 5
        stack.pop()  # Pop 0 (min)
        stack.pop()  # Pop 2 (not min)
        stack.pop()  # Pop 1 (min)
        stack.pop()  # Pop 1 (min)
        
        # Expected result: main=[5, 3], min=[5, 3]
        expected_main = [5, 3]
        expected_min = [5, 3]
        
        self.assertEqual(stack.stack, expected_main)
        self.assertEqual(stack.min, expected_min)
    
    def test_edge_case_zero_values(self):
        """Test edge case with zero values"""
        stack = Solution()
        
        # Test with zeros (which are falsy in Python)
        stack.push(0)
        stack.push(-1)
        
        # Check the conditional logic with zero values
        peak = stack.peak()
        getMin = stack.getMin()
        
        # This should work correctly because 0 and -1 are both truthy when compared as values
        self.assertEqual(peak, -1)
        self.assertEqual(getMin, -1)
        self.assertTrue(peak and getMin and peak == getMin)
        
        # Pop -1 (should remove from both stacks)
        stack.pop()
        self.assertEqual(stack.peak(), 0)
        self.assertEqual(stack.getMin(), 0)
        
        # Pop 0 (should remove from both stacks)
        stack.pop()
        self.assertIsNone(stack.peak())
        self.assertIsNone(stack.getMin())
    
    def test_zero_values_debug(self):
        """Debug test for zero values issue"""
        stack = Solution()
        
        stack.push(0)
        stack.push(2)
        
        stack.pop()  # Should pop 2, but min stack stays unchanged
        self.assertEqual(stack.stack, [0])
        self.assertEqual(stack.min, [0])
        self.assertEqual(stack.peak(), 0)
        self.assertEqual(stack.getMin(), 0)
        
        # Test the real zero issue
        stack = Solution()
        stack.push(5)
        stack.push(0)  # This becomes the minimum
        
        stack.pop()  # Should pop 0 and remove from min stack
        
        self.assertEqual(stack.stack, [5])
        self.assertEqual(stack.min, [5])
        self.assertEqual(stack.peak(), 5)
        self.assertEqual(stack.getMin(), 5)


if __name__ == '__main__':
    unittest.main()
