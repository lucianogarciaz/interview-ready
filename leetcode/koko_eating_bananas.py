from typing import List
import math
import unittest

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int)-> int:
        topK = max(piles)
        l = 1
        r = topK
        res = topK
        while l<=r:
            pivot = (r+l)//2
            k = 0
            for p in piles:
                k += math.ceil(p/pivot)
            if k <= h:
                res = min(res, pivot)
                r = pivot -1 
            else:
                l = pivot + 1
        return res
    

class TestKokoEatingBananas(unittest.TestCase):
    def test_example1(self):
        piles = [3, 6, 7, 11]
        h = 8
        expected = 4
        solution = Solution()
        result = solution.minEatingSpeed(piles, h)
        self.assertEqual(result, expected)

    def test_example2(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        expected = 30
        solution = Solution()
        result = solution.minEatingSpeed(piles, h)
        self.assertEqual(result, expected)

    def test_example3(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        expected = 23
        solution = Solution()
        result = solution.minEatingSpeed(piles, h)
        self.assertEqual(result, expected)

    def test_single_pile(self):
        piles = [10]
        h = 2
        expected = 5
        solution = Solution()
        result = solution.minEatingSpeed(piles, h)
        self.assertEqual(result, expected)

    def test_equal_piles(self):
        piles = [5, 5, 5, 5]
        h = 4
        expected = 5
        solution = Solution()
        result = solution.minEatingSpeed(piles, h)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
    