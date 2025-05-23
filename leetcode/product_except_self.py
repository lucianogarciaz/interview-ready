
from typing import List
import unittest
class Solution:
    def productExceptSelf(self, nums: List[int])-> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        prefix = [nums[0]]
        postfix = [i for i in range(n)]
        postfix[n-1] = nums[n-1]

        for i in range(1, n):
            prefix.append(prefix[i-1]*nums[i])
        for i in range(n-2, -1,-1):
            postfix[i] = postfix[i+1]*nums[i]
        res = [postfix[1]]
        for i in range(1, n-1):
            res.append(prefix[i-1]*postfix[i+1])
        
        res.append(prefix[n-2])
        return res

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, expected)
    
    def test_single_element(self):
        nums = [1]
        expected = [1]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, expected)
    
    def test_two_elements(self):
        nums = [2, 3]
        expected = [3, 2]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, expected)
    
    def test_with_zeros(self):
        nums = [0, 0]
        expected = [0, 0]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 