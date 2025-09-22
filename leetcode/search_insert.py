from typing import List
import unittest

class Solution:
    def searchInsert(self, nums:List[int], target:int)->int:
        r=len(nums)-1
        l=0

        while l<=r:
            pivot = (l+r)//2
            if nums[pivot]== target:
                return pivot
            if nums[pivot]<target:
                l= pivot + 1

            if nums[pivot]>target:
                r=pivot - 1
            

        return l


class TestSearchInsert(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_target_found(self):
        nums = [1,3,5,6]
        target = 5
        expected = 2
        self.assertEqual(self.solution.searchInsert(nums, target), expected)

    def test_target_not_found_insert_middle(self):
        nums = [1,3,5,6]
        target = 2
        expected = 1
        self.assertEqual(self.solution.searchInsert(nums, target), expected)

    def test_target_not_found_insert_end(self):
        nums = [1,3,5,6]
        target = 7
        expected = 4
        self.assertEqual(self.solution.searchInsert(nums, target), expected)

    def test_target_not_found_insert_start(self):
        nums = [1,3,5,6]
        target = 0
        expected = 0
        self.assertEqual(self.solution.searchInsert(nums, target), expected)

    def test_single_element_found(self):
        nums = [1]
        target = 1
        expected = 0
        self.assertEqual(self.solution.searchInsert(nums, target), expected)

    def test_single_element_insert_before(self):
        nums = [1]
        target = 0
        expected = 0
        self.assertEqual(self.solution.searchInsert(nums, target), expected)

    def test_single_element_insert_after(self):
        nums = [1]
        target = 2
        expected = 1
        self.assertEqual(self.solution.searchInsert(nums, target), expected)

    def test_empty_list(self):
        nums = []
        target = 3
        expected = 0
        self.assertEqual(self.solution.searchInsert(nums, target), expected)

    def test_large_input(self):
        nums = list(range(0, 10000, 2))  # [0,2,4,...,9998]
        target = 1234
        expected = 617
        self.assertEqual(self.solution.searchInsert(nums, target), expected)
        target = 1235
        expected = 618
        self.assertEqual(self.solution.searchInsert(nums, target), expected)

if __name__ == "__main__":
    unittest.main()
