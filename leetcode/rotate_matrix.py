import unittest
from typing import List
# 1 2
# 3 4
# 3 1
# 4 2

# 1 2   3  4
# 5 6   7  8
# 9 10 11 12
#13 14 15 16
# 
# 13  9  5  1
# 14 10  6 2
# 15 11  7  3
# 16 12  8  4
# 
# 1: 0,0 -> 0,3
# 2: 0,1 -> 1,3
# 3: 0,2 -> 2,3
# 4: 0,3 -> 3,3
# 5: 1,0 -> 0,2
# 6: 1,1 -> 1,2
# 14: 3,1 -> 1,0

# 1 2 3
# 4 5 6
# 7 8 9
# ---
# 
# 
# 

# ---
# 7 4 1
# 8 5 2
# 9 6 3



class Solution:
    def rotateMatrix(self, matrix:List[List[int]])->List[List[int]]:
        n = len(matrix)
        # swat column with row
        for row in range(n):
            for col in range(row+1, n):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = tmp
        
        # mirror the row
        for row in range(n):
            for col in range(n//2):
                tmp = matrix[row][col]
                newCol = n - 1 - col
                matrix[row][col] = matrix[row][newCol]
                matrix[row][newCol] = tmp
        return matrix

    def rotateMatrixWithDataStructure(self, matrix: List[List[int]])->List[List[int]]:
        n = len(matrix)
        newMatrix:List[List[int]] = [[0] * n for _ in range(n)]
    
        for col in range(n):
            for row in range(n):
                newRow = col
                newCol = abs(n -1 - row)
                newMatrix[newRow][newCol] = matrix[row][col]
        
        return newMatrix

class TestRotateMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_2x2(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        expected = [
            [3, 1],
            [4, 2]
        ]
        result = self.solution.rotateMatrix([row[:] for row in matrix])
        self.assertEqual(result, expected)

    def test_3x3(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        result = self.solution.rotateMatrix([row[:] for row in matrix])
        self.assertEqual(result, expected)

    def test_4x4(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        expected = [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ]
        result = self.solution.rotateMatrix([row[:] for row in matrix])
        self.assertEqual(result, expected)

    def test_single_element(self):
        matrix = [[1]]
        expected = [[1]]
        result = self.solution.rotateMatrix([row[:] for row in matrix])
        self.assertEqual(result, expected)

    def test_empty_matrix(self):
        matrix = []
        expected = []
        result = self.solution.rotateMatrix([row[:] for row in matrix])
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
