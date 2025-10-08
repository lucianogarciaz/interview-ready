import unittest
from typing import List


class Solution:
    def generateCombinations(self, arr:List[int], k:int)->List[List[int]]:
        res:List[List[int]] = []
        path:List[int] = []
        def backtrack(index:int):
            if len(path)==k:
                res.append(path.copy())
                return
            
            for i in range(index,len(arr)):
                path.append(arr[i])
                backtrack(i+1)
                path.pop()
            
        backtrack(0)
        return res

class TestGenerateCombinations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_basic_case_k_equals_2(self):
        result = self.solution.generateCombinations([1, 2, 3, 4], 2)
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_basic_case_k_equals_3(self):
        result = self.solution.generateCombinations([1, 2, 3, 4], 3)
        expected = [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_k_equals_1(self):
        result = self.solution.generateCombinations([1, 2, 3], 1)
        expected = [[1], [2], [3]]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_k_equals_array_length(self):
        result = self.solution.generateCombinations([1, 2, 3], 3)
        expected = [[1, 2, 3]]
        self.assertEqual(result, expected)
    
    def test_k_equals_zero(self):
        result = self.solution.generateCombinations([1, 2, 3], 0)
        expected = [[]]
        self.assertEqual(result, expected)
    
    def test_empty_array(self):
        result = self.solution.generateCombinations([], 2)
        expected = []
        self.assertEqual(result, expected)
    
    def test_k_greater_than_array_length(self):
        result = self.solution.generateCombinations([1, 2], 5)
        expected = []
        self.assertEqual(result, expected)
    
    def test_single_element_array(self):
        result = self.solution.generateCombinations([5], 1)
        expected = [[5]]
        self.assertEqual(result, expected)
    
    def test_correct_count(self):
        from math import comb
        arr = [1, 2, 3, 4, 5]
        k = 3
        result = self.solution.generateCombinations(arr, k)
        self.assertEqual(len(result), comb(len(arr), k))
    
    def test_no_duplicates(self):
        result = self.solution.generateCombinations([1, 2, 3, 4], 2)
        result_tuples = [tuple(combo) for combo in result]
        self.assertEqual(len(result), len(set(result_tuples)))
    
    def test_combinations_with_larger_numbers(self):
        result = self.solution.generateCombinations([10, 20, 30, 40], 2)
        expected = [[10, 20], [10, 30], [10, 40], [20, 30], [20, 40], [30, 40]]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_all_elements_correct_length(self):
        k = 3
        result = self.solution.generateCombinations([1, 2, 3, 4, 5], k)
        for combo in result:
            self.assertEqual(len(combo), k)


if __name__ == "__main__":
    unittest.main()