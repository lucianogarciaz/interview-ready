from typing import List
import unittest

def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    
    Args:
        nums: List of integers
        
    Returns:
        List of lists containing triplets that sum to zero
    """
    nums = sorted(nums)
    res = []
    for i,v in enumerate(nums):
        if i>0 and nums[i-1]==v:
            continue
        l,r=i+1,len(nums)-1
        while l<r:
            cSum = v+nums[l]+nums[r]
            if cSum == 0:
                res.append([v,nums[l],nums[r]])
                l+=1
                r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
            if cSum < 0:
                l+=1
            if cSum >0:
                r-=1
            
    return res

class TestThreeSum(unittest.TestCase):
    def test_example1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        result = threeSum(nums)
        self.assertEqual(sorted([sorted(x) for x in result]), sorted([sorted(x) for x in expected]))

    def test_example2(self):
        nums = []
        expected = []
        result = threeSum(nums)
        self.assertEqual(result, expected)

    def test_example3(self):
        nums = [0]
        expected = []
        result = threeSum(nums)
        self.assertEqual(result, expected)

    def test_no_solution(self):
        nums = [1, 2, 3, 4, 5]
        expected = []
        result = threeSum(nums)
        self.assertEqual(result, expected)

    def test_multiple_solutions(self):
        nums = [-2, 0, 1, 1, 2]
        expected = [[-2, 0, 2], [-2, 1, 1]]
        result = threeSum(nums)
        self.assertEqual(sorted([sorted(x) for x in result]), sorted([sorted(x) for x in expected]))

    def test_duplicate_numbers(self):
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        result = threeSum(nums)
        self.assertEqual(sorted([sorted(x) for x in result]), sorted([sorted(x) for x in expected]))

if __name__ == '__main__':
    unittest.main()

