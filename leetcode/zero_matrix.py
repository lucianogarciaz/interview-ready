import unittest
from typing import List
# 1 2 3
# 4 0 5
# 6 7 8
# coordinate = [[1,1]]
# 1 0 3
# 0 0 0
# 6 0 8

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        coordinates: List[Tuple[int,int]] = []
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    coordinates.append((row,col))
        for i,j in coordinates:
            # set 0 all row
            for col in range(m):
                matrix[i][col] = 0
            # set 0 to all column
            for row in range(n):
                matrix[row][j] = 0

class TestSetZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_3x3_with_one_zero(self):
        matrix = [
            [1, 2, 3],
            [4, 0, 6],
            [7, 8, 9]
        ]
        expected = [
            [1, 0, 3],
            [0, 0, 0],
            [7, 0, 9]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_3x3_no_zeros(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_3x3_all_zeros(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        expected = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_1x1_zero(self):
        matrix = [
            [0]
        ]
        expected = [
            [0]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_1x1_nonzero(self):
        matrix = [
            [5]
        ]
        expected = [
            [5]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_2x2_with_zero(self):
        matrix = [
            [1, 0],
            [3, 4]
        ]
        expected = [
            [0, 0],
            [3, 0]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_2x2_all_zeros(self):
        matrix = [
            [0, 0],
            [0, 0]
        ]
        expected = [
            [0, 0],
            [0, 0]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_2x3_with_multiple_zeros(self):
        matrix = [
            [1, 0, 3],
            [4, 5, 6]
        ]
        expected = [
            [0, 0, 0],
            [4, 0, 6]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_3x2_with_multiple_zeros(self):
        matrix = [
            [1, 2],
            [0, 4],
            [5, 6]
        ]
        expected = [
            [0, 2],
            [0, 0],
            [0, 6]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

if __name__ == "__main__":
    unittest.main()
