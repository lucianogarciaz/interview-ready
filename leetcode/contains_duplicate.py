from typing import List
import unittest

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = {}
        for val in nums:
            if val in hash:
                hash[val] += 1    
            else:
                hash[val] = 1
            
        for val in hash:
            if hash[val] > 1:
                return True
        
        return False

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        nums = [1, 2, 3, 1]
        expected = True
        result = self.solution.containsDuplicate(nums)
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        nums = [1, 2, 3, 4]
        expected = False
        result = self.solution.containsDuplicate(nums)
        self.assertEqual(result, expected)
    
    def test_example_3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        expected = True
        result = self.solution.containsDuplicate(nums)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 