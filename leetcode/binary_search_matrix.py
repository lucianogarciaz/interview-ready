from typing import List
import unittest
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int)-> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        bot =0
        top = m - 1
        row = 0
        while bot<=top:
            row = (bot+top)//2 
            if matrix[row][0]>target:
                top = row - 1
            elif matrix[row][-1] < target:
                bot = row +1
            else:
                break
        
        if bot > top:
            return False

        l,r = 0, n-1

        while l<=r:
            pivot = (r+l)//2
            if matrix[row][pivot]==target:
                return True
            if matrix[row][pivot]<target:
                l = pivot + 1
            else:
                r = pivot -1
        
        return False
    
class TestSearchMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 3
        expected = True
        result = self.solution.searchMatrix(matrix, target)
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 13
        expected = False
        result = self.solution.searchMatrix(matrix, target)
        self.assertEqual(result, expected)
    
    def test_empty_matrix(self):
        matrix = []
        target = 1
        expected = False
        result = self.solution.searchMatrix(matrix, target)
        self.assertEqual(result, expected)
    
    def test_single_element_found(self):
        matrix = [[1]]
        target = 1
        expected = True
        result = self.solution.searchMatrix(matrix, target)
        self.assertEqual(result, expected)
    
    def test_single_element_not_found(self):
        matrix = [[1]]
        target = 2
        expected = False
        result = self.solution.searchMatrix(matrix, target)
        self.assertEqual(result, expected)
    
    def test_target_at_start(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        target = 1
        expected = True
        result = self.solution.searchMatrix(matrix, target)
        self.assertEqual(result, expected)
    
    def test_target_at_end(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        target = 9
        expected = True
        result = self.solution.searchMatrix(matrix, target)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
