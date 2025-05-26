from typing import List
import unittest
class Solution:
    def search(self, nums: List[int], target: int)->int:
        l=0
        r=len(nums)-1
        while l<=r:
            pivot = int((l+r)/2)
            if nums[pivot]== target:
                return pivot
            if nums[pivot]< target:
                l = pivot+1
            else:
                r = pivot-1
        return -1
    

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        expected = 4
        result = self.solution.search(nums, target)
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        expected = -1
        result = self.solution.search(nums, target)
        self.assertEqual(result, expected)
    
    def test_empty_array(self):
        nums = []
        target = 1
        expected = -1
        result = self.solution.search(nums, target)
        self.assertEqual(result, expected)
    
    def test_single_element_found(self):
        nums = [1]
        target = 1
        expected = 0
        result = self.solution.search(nums, target)
        self.assertEqual(result, expected)
    
    def test_single_element_not_found(self):
        nums = [1]
        target = 2
        expected = -1
        result = self.solution.search(nums, target)
        self.assertEqual(result, expected)
    
    def test_target_at_start(self):
        nums = [1, 2, 3, 4, 5]
        target = 1
        expected = 0
        result = self.solution.search(nums, target)
        self.assertEqual(result, expected)
    
    def test_target_at_end(self):
        nums = [1, 2, 3, 4, 5]
        target = 5
        expected = 4
        result = self.solution.search(nums, target)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

