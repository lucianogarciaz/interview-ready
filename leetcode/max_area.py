import unittest
from typing import List
class Solution:
    def maxArea(self, height: List[int])->bool:
        l=0
        r=len(height)-1
        maxArea=0
        while l<r:
            area = (r-l)*min(height[r], height[l])
            maxArea = max(area, maxArea)
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return maxArea

class TestMaxArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        result = self.solution.maxArea(height)
        self.assertEqual(result, expected)
    
    def test_example2(self):
        height = [1, 1]
        expected = 1
        result = self.solution.maxArea(height)
        self.assertEqual(result, expected)
    
    def test_single_element(self):
        height = [1]
        expected = 0
        result = self.solution.maxArea(height)
        self.assertEqual(result, expected)
    
    def test_decreasing_heights(self):
        height = [5, 4, 3, 2, 1]
        expected = 6
        result = self.solution.maxArea(height)
        self.assertEqual(result, expected)
    
    def test_increasing_heights(self):
        height = [1, 2, 3, 4, 5]
        expected = 6
        result = self.solution.maxArea(height)
        self.assertEqual(result, expected)
    
    def test_equal_heights(self):
        height = [4, 4, 4, 4]
        expected = 12
        result = self.solution.maxArea(height)
        self.assertEqual(result, expected)
    
    def test_zero_heights(self):
        height = [0, 0, 0, 0]
        expected = 0
        result = self.solution.maxArea(height)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
