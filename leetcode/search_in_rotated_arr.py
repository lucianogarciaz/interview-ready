from typing import List
import unittest

class Solution:
    def search(self, nums: List[int],target: int)->int:
        l = 0
        r = len(nums)-1
        while l<=r:
            pivot = (r+l)//2
            if nums[pivot-1]>nums[pivot]:
                break
            if nums[pivot]>=nums[0]:
                l = pivot + 1
            else:
                r = pivot - 1
        
        l, r = 0, len(nums)-1
        if nums[pivot]<=target<= nums[len(nums)-1]:
            l = pivot
        else:
            r = pivot
        
        while l<=r:
            pivot = (l+r)//2
            if nums[pivot]==target:
                return pivot
            if nums[pivot]<target:
                l = pivot + 1
            else: 
                r = pivot - 1
        
        return -1


class TestSearchInRotatedArray(unittest.TestCase):
    def test_example1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        expected = 4
        solution = Solution()
        result = solution.search(nums, target)
        self.assertEqual(result, expected)

    def test_example2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        expected = -1
        solution = Solution()
        result = solution.search(nums, target)
        self.assertEqual(result, expected)

    def test_example3(self):
        nums = [1]
        target = 0
        expected = -1
        solution = Solution()
        result = solution.search(nums, target)
        self.assertEqual(result, expected)

    def test_single_element_found(self):
        nums = [1]
        target = 1
        expected = 0
        solution = Solution()
        result = solution.search(nums, target)
        self.assertEqual(result, expected)

    def test_not_rotated(self):
        nums = [1, 2, 3, 4, 5]
        target = 3
        expected = 2
        solution = Solution()
        result = solution.search(nums, target)
        self.assertEqual(result, expected)

    def test_target_at_pivot(self):
        nums = [3, 4, 5, 1, 2]
        target = 5
        expected = 2
        solution = Solution()
        result = solution.search(nums, target)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
