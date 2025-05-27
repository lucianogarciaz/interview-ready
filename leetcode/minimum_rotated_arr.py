from typing import List
import unittest

class Solution:
    def findMin(self, nums: List[int])->int:
        l = 0
        r = len(nums)-1
        while l<=r:
            pivot = (r+l)//2
            if nums[pivot-1]>nums[pivot]:
                return nums[pivot]
            if nums[pivot]>=nums[0]:
                l = pivot + 1
            else:
                r = pivot - 1
        
        return nums[0]

class TestFindMin(unittest.TestCase):
    def test_example1(self):
        nums = [3, 4, 5, 1, 2]
        expected = 1
        solution = Solution()
        result = solution.findMin(nums)
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        expected = 0
        solution = Solution()
        result = solution.findMin(nums)
        self.assertEqual(result, expected)

    def test_example3(self):
        nums = [11, 13, 15, 17]
        expected = 11
        solution = Solution()
        result = solution.findMin(nums)
        self.assertEqual(result, expected)

    def test_single_element(self):
        nums = [1]
        expected = 1
        solution = Solution()
        result = solution.findMin(nums)
        self.assertEqual(result, expected)

    def test_two_elements(self):
        nums = [2, 1]
        expected = 1
        solution = Solution()
        result = solution.findMin(nums)
        self.assertEqual(result, expected)

    def test_duplicate_elements(self):
        nums = [2, 2, 2, 0, 1]
        expected = 0
        solution = Solution()
        result = solution.findMin(nums)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
