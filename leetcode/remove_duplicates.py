from typing import List
import unittest

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        k = 0

        for i, num in enumerate(nums):
            nums[i]=nums[pointer]  # 1 2 1
            
            while pointer < len(nums) and nums[i]==nums[pointer]: # 0 2 0
                pointer+=1
            
            k+=1
            if pointer > len(nums)-1:
                break
        
        return k
    def removeDuplicatesEfficient(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1,1,2]
        expected_nums = [1,2]
        k = self.solution.removeDuplicatesEfficient(nums)
        self.assertEqual(k, len(expected_nums))
        self.assertEqual(nums[:k], expected_nums)

    def test_example2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        expected_nums = [0,1,2,3,4]
        k = self.solution.removeDuplicatesEfficient(nums)
        self.assertEqual(k, len(expected_nums))
        self.assertEqual(nums[:k], expected_nums)
    def test_empty_list(self):
        nums = []
        expected_nums = []
        k = self.solution.removeDuplicatesEfficient(nums)
        self.assertEqual(k, len(expected_nums))
        self.assertEqual(nums[:k], expected_nums)

    def test_single_element(self):
        nums = [5]
        expected_nums = [5]
        k = self.solution.removeDuplicatesEfficient(nums)
        self.assertEqual(k, len(expected_nums))
        self.assertEqual(nums[:k], expected_nums)

    def test_all_duplicates(self):
        nums = [2,2,2,2,2]
        expected_nums = [2]
        k = self.solution.removeDuplicatesEfficient(nums)
        self.assertEqual(k, len(expected_nums))
        self.assertEqual(nums[:k], expected_nums)

    def test_no_duplicates(self):
        nums = [1,2,3,4,5]
        expected_nums = [1,2,3,4,5]
        k = self.solution.removeDuplicatesEfficient(nums)
        self.assertEqual(k, len(expected_nums))
        self.assertEqual(nums[:k], expected_nums)

    def test_large_input(self):
        nums = [1]*100 + [2]*100 + [3]*100
        expected_nums = [1,2,3]
        k = self.solution.removeDuplicatesEfficient(nums)
        self.assertEqual(k, len(expected_nums))
        self.assertEqual(nums[:k], expected_nums)

if __name__ == "__main__":
    unittest.main()

