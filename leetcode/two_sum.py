from typing import List
import unittest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myDict = {}
        for i, val in enumerate(nums) :
            myDict[target-val] = i
        
        
        for i, val in enumerate(nums):
            if val in myDict and myDict[val]!=i :
                return [i, myDict[val]]

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_example_3(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))

if __name__ == '__main__':
    unittest.main() 