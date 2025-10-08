import unittest
from typing import List


class Solution:
    def combination_sum(self, arr:List[int], target:int)->List[List[int]]:
        res:List[List[int]]=[]
        path:List[int]=[]
        arr.sort()
        def backtrack(index:int, total:int):
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return
            
            for i in range(index, len(arr)):
                path.append(arr[i])
                backtrack(i, total + arr[i])
                path.pop()

        
        backtrack(0,0)
        return res

    def combination_sum_ii(self, arr:List[int], target:int)->List[List[int]]:
        res:List[List[int]] = []
        path:List[List[int]] = []
        arr.sort()

        def backtrack(index:int, total:int):
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return
            for i in range(index, len(arr)):
                if i>index and arr[i]==arr[i-1]:
                    continue
                path.append(arr[i])
                backtrack(i+1, arr[i]+total)
                path.pop()

        backtrack(0,0)
        return res
    
    def subset_with_dup(self, arr:List[int])->List[List[int]]:
        res:List[List[int]] = []
        path:List[int] = []
        arr.sort()
        # [1,2,2,3]
        # [1] [1,2] [1,3] [2,2] [2,3]
        def backtrack(index:int)->None:
            res.append(path.copy())
            for i in range(index,len(arr)):
                if i>index and arr[i]==arr[i-1]:
                    continue
                path.append(arr[i])
                backtrack(i+1)
                path.pop()
        
        backtrack(0)
        return res

    def generateCombinations(self, arr:List[int], k:int)->List[List[int]]:
        res:List[List[int]] = []
        path:List[int] = []
        def backtrack(index:int)->None:
            if len(path)==k:
                res.append(path.copy())
                return
            
            for i in range(index,len(arr)):
                path.append(arr[i])
                backtrack(i+1)
                path.pop()
            
        backtrack(0)
        return res


class TestCombinationSumII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_basic_case(self):
        result = self.solution.combination_sum_ii([10, 1, 2, 7, 6, 1, 5], 8)
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        self.assertEqual(len(result), len(expected))
        for combo in expected:
            self.assertIn(combo, result)
    
    def test_with_duplicates(self):
        result = self.solution.combination_sum_ii([2, 5, 2, 1, 2], 5)
        expected = [[1, 2, 2], [5]]
        self.assertEqual(len(result), len(expected))
        for combo in expected:
            self.assertIn(combo, result)
    
    def test_no_solution(self):
        result = self.solution.combination_sum_ii([2, 3, 5], 1)
        expected = []
        self.assertEqual(result, expected)
    
    def test_single_element_matches_target(self):
        result = self.solution.combination_sum_ii([1, 2, 3], 3)
        expected = [[1,2],[3]]
        self.assertEqual(result, expected)
    
    def test_all_same_numbers(self):
        result = self.solution.combination_sum_ii([1, 1, 1, 1], 2)
        expected = [[1, 1]]
        self.assertEqual(result, expected)
    
    def test_multiple_duplicates(self):
        result = self.solution.combination_sum_ii([1, 1, 1, 1, 1], 3)
        expected = [[1, 1, 1]]
        self.assertEqual(result, expected)
    
    def test_no_duplicate_combinations(self):
        result = self.solution.combination_sum_ii([10, 1, 2, 7, 6, 1, 5], 8)
        result_tuples = [tuple(combo) for combo in result]
        self.assertEqual(len(result), len(set(result_tuples)))
    
    def test_all_combinations_sum_to_target(self):
        result = self.solution.combination_sum_ii([10, 1, 2, 7, 6, 1, 5], 8)
        for combo in result:
            self.assertEqual(sum(combo), 8)
    
    def test_elements_in_sorted_order(self):
        result = self.solution.combination_sum_ii([10, 1, 2, 7, 6, 1, 5], 8)
        for combo in result:
            self.assertEqual(combo, sorted(combo))
    
    def test_each_element_used_once(self):
        result = self.solution.combination_sum_ii([1, 2], 3)
        expected = [[1, 2]]
        self.assertEqual(result, expected)
        # Should NOT have [1, 1] since only one '1' is available
        self.assertNotIn([1, 1], result)
    
    def test_empty_array(self):
        result = self.solution.combination_sum_ii([], 5)
        expected = []
        self.assertEqual(result, expected)
    
    def test_target_zero(self):
        result = self.solution.combination_sum_ii([1, 2, 3], 0)
        expected = [[]]
        self.assertEqual(result, expected)
    
    def test_larger_array_with_duplicates(self):
        result = self.solution.combination_sum_ii([1, 1, 2, 2, 3], 5)
        expected = [[1, 1, 3], [1, 2, 2], [2, 3]]
        self.assertEqual(len(result), len(expected))
        for combo in expected:
            self.assertIn(combo, result)
    
    def test_uses_all_elements(self):
        result = self.solution.combination_sum_ii([1, 2, 3], 6)
        expected = [[1, 2, 3]]
        self.assertEqual(result, expected)
    
    def test_many_duplicates_different_sums(self):
        result = self.solution.combination_sum_ii([1, 1, 1, 2, 2], 4)
        expected = [[1, 1, 2], [2, 2]]
        self.assertEqual(len(result), len(expected))
        for combo in expected:
            self.assertIn(combo, result)

class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_basic_case(self):
        result = self.solution.combination_sum([2, 3, 6, 7], 7)
        expected = [[2, 2, 3], [7]]
        self.assertEqual(len(result), len(expected))
        for combo in expected:
            self.assertIn(combo, result)
    
    def test_repeated_elements(self):
        result = self.solution.combination_sum([2, 3, 5], 8)
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertEqual(len(result), len(expected))
        for combo in expected:
            self.assertIn(combo, result)
    
    def test_single_element_repeated(self):
        result = self.solution.combination_sum([2], 8)
        expected = [[2, 2, 2, 2]]
        self.assertEqual(result, expected)
    
    def test_target_equals_element(self):
        result = self.solution.combination_sum([2, 3, 5], 5)
        expected = [[2, 3], [5]]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_no_solution(self):
        result = self.solution.combination_sum([2, 4, 6], 5)
        expected = []
        self.assertEqual(result, expected)
    
    def test_target_1(self):
        result = self.solution.combination_sum([1], 3)
        expected = [[1, 1, 1]]
        self.assertEqual(result, expected)
    
    def test_larger_numbers(self):
        result = self.solution.combination_sum([10, 20, 30], 50)
        expected = [[10,10,10,10,10],[10, 10, 10, 20], [10, 10, 30], [10, 20, 20], [20, 30]]
        self.assertEqual(len(result), len(expected))
        for combo in expected:
            self.assertIn(combo, result)
    
    def test_all_combinations_sum_to_target(self):
        result = self.solution.combination_sum([2, 3, 5], 8)
        for combo in result:
            self.assertEqual(sum(combo), 8)
    
    def test_no_duplicates_in_result(self):
        result = self.solution.combination_sum([2, 3, 6, 7], 7)
        result_tuples = [tuple(combo) for combo in result]
        self.assertEqual(len(result), len(set(result_tuples)))
    
    def test_elements_in_sorted_order(self):
        result = self.solution.combination_sum([3, 2, 7, 6], 7)
        for combo in result:
            self.assertEqual(combo, sorted(combo))
    
    def test_single_element_cant_reach_target(self):
        result = self.solution.combination_sum([3], 5)
        expected = []
        self.assertEqual(result, expected)
    
    def test_multiple_ways_to_reach_target(self):
        result = self.solution.combination_sum([1, 2], 4)
        expected = [[1, 1, 1, 1], [1, 1, 2], [2, 2]]
        self.assertEqual(len(result), len(expected))
        for combo in expected:
            self.assertIn(combo, result)
    
    def test_target_zero(self):
        result = self.solution.combination_sum([1, 2, 3], 0)
        expected = [[]]
        self.assertEqual(result, expected)
    
    def test_large_target_small_numbers(self):
        result = self.solution.combination_sum([2, 3], 12)
        self.assertGreater(len(result), 0)
        for combo in result:
            self.assertEqual(sum(combo), 12)
    
    def test_all_elements_use_only_from_candidates(self):
        candidates = [2, 3, 6, 7]
        result = self.solution.combination_sum(candidates, 7)
        for combo in result:
            for num in combo:
                self.assertIn(num, candidates)

class TestSubsetWithDup(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_basic_case_with_duplicates(self):
        result = self.solution.subset_with_dup([1, 2, 2])
        expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        self.assertEqual(len(result), len(expected))
        for subset in expected:
            self.assertIn(subset, result)
    
    def test_no_duplicates_in_input(self):
        result = self.solution.subset_with_dup([1, 2, 3])
        expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        self.assertEqual(len(result), len(expected))
        for subset in expected:
            self.assertIn(subset, result)
    
    def test_all_same_elements(self):
        result = self.solution.subset_with_dup([1, 1, 1])
        expected = [[], [1], [1, 1], [1, 1, 1]]
        self.assertEqual(len(result), len(expected))
        for subset in expected:
            self.assertIn(subset, result)
    
    def test_two_duplicates(self):
        result = self.solution.subset_with_dup([4, 4, 4, 1, 4])
        # Should handle duplicates properly
        self.assertGreater(len(result), 0)
        # No duplicate subsets
        result_tuples = [tuple(subset) for subset in result]
        self.assertEqual(len(result), len(set(result_tuples)))
    
    def test_empty_array(self):
        result = self.solution.subset_with_dup([])
        expected = [[]]
        self.assertEqual(result, expected)
    
    def test_single_element(self):
        result = self.solution.subset_with_dup([1])
        expected = [[], [1]]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_multiple_pairs_of_duplicates(self):
        result = self.solution.subset_with_dup([1, 2, 2, 3, 3])
        # Check no duplicate subsets exist
        result_tuples = [tuple(subset) for subset in result]
        self.assertEqual(len(result), len(set(result_tuples)))
        # Check some key subsets exist
        self.assertIn([1, 2, 2], result)
        self.assertIn([1, 3, 3], result)
        self.assertIn([2, 2, 3, 3], result)
    
    def test_no_duplicate_subsets_in_result(self):
        result = self.solution.subset_with_dup([1, 2, 2, 3])
        result_tuples = [tuple(subset) for subset in result]
        self.assertEqual(len(result), len(set(result_tuples)), 
                        "Result contains duplicate subsets")
    
    def test_sorting_preserved(self):
        result = self.solution.subset_with_dup([3, 1, 2, 2])
        # All subsets should be in sorted order (since arr.sort() is called)
        for subset in result:
            self.assertEqual(subset, sorted(subset))
    
    def test_larger_array_with_dups(self):
        result = self.solution.subset_with_dup([1, 2, 2, 3])
        expected = [
            [], [1], [1, 2], [1, 2, 2], [1, 2, 2, 3], [1, 2, 3], 
            [1, 3], [2], [2, 2], [2, 2, 3], [2, 3], [3]
        ]
        self.assertEqual(len(result), len(expected))
        for subset in expected:
            self.assertIn(subset, result)

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