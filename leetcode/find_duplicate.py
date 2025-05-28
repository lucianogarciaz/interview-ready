import unittest
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        newSlow = 0
        while True:
            slow = nums[slow]
            newSlow= nums[newSlow]
            if newSlow==slow:
                return slow

class TestFindDuplicate(unittest.TestCase):
    def test_example1(self):
        nums = [1, 3, 4, 2, 2]
        expected = 2
        solution = Solution()
        result = solution.findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [3, 1, 3, 4, 2]
        expected = 3
        solution = Solution()
        result = solution.findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_single_duplicate(self):
        nums = [1, 1]
        expected = 1
        solution = Solution()
        result = solution.findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_duplicate_at_end(self):
        nums = [1, 2, 3, 4, 5, 5]
        expected = 5
        solution = Solution()
        result = solution.findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_duplicate_at_start(self):
        nums = [1, 1, 2, 3, 4]
        expected = 1
        solution = Solution()
        result = solution.findDuplicate(nums)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
