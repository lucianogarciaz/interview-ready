import unittest
from typing import List


class Solution:
    def generateBinaries(self, n:int)->List[str]:
        res = []
        def backtrack(path:List[str]):
            if len(path)==n:
                # res.append(''.join(str(bit)for bit in path))
                res.append(''.join(path))
                return
            for bit in ['0','1']:
                path.append(bit)
                backtrack(path)
                path.pop()
                
        backtrack([])
        return res


class TestGenerateBinaries(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_n_equals_zero(self):
        result = self.solution.generateBinaries(0)
        self.assertEqual(result, [""])
        self.assertEqual(len(result), 1)
    
    def test_n_equals_one(self):
        result = self.solution.generateBinaries(1)
        self.assertEqual(sorted(result), ["0", "1"])
        self.assertEqual(len(result), 2)
    
    def test_n_equals_two(self):
        result = self.solution.generateBinaries(2)
        expected = ["00", "01", "10", "11"]
        self.assertEqual(sorted(result), sorted(expected))
        self.assertEqual(len(result), 4)
    
    def test_n_equals_three(self):
        result = self.solution.generateBinaries(3)
        expected = ["000", "001", "010", "011", "100", "101", "110", "111"]
        self.assertEqual(sorted(result), sorted(expected))
        self.assertEqual(len(result), 8)
    
    def test_n_equals_four(self):
        result = self.solution.generateBinaries(4)
        self.assertEqual(len(result), 16)
        for binary_str in result:
            self.assertEqual(len(binary_str), 4)
            self.assertTrue(all(c in ['0', '1'] for c in binary_str))
    
    def test_all_unique(self):
        for n in range(1, 5):
            result = self.solution.generateBinaries(n)
            self.assertEqual(len(result), len(set(result)))
    
    def test_correct_count(self):
        for n in range(0, 6):
            result = self.solution.generateBinaries(n)
            self.assertEqual(len(result), 2**n)
    
    def test_all_strings_have_correct_length(self):
        for n in range(1, 5):
            result = self.solution.generateBinaries(n)
            for binary_str in result:
                self.assertEqual(len(binary_str), n)
    
    def test_only_binary_characters(self):
        for n in range(1, 5):
            result = self.solution.generateBinaries(n)
            for binary_str in result:
                self.assertTrue(all(c in ['0', '1'] for c in binary_str))
    
    def test_n_equals_five(self):
        result = self.solution.generateBinaries(5)
        self.assertEqual(len(result), 32)
        self.assertEqual(len(set(result)), 32)
        for binary_str in result:
            self.assertEqual(len(binary_str), 5)


if __name__ == "__main__":
    unittest.main()