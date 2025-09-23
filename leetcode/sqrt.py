from typing import List
import unittest
class Solution:
    def sqrt(self, x:int)->int:
        r = x//2 +1
        l = 1
        res = 0
        while l<=r:
            pivot = (l+r)//2
            p = pivot*pivot
            if p == x:
                return pivot
            if p>x:
                r = pivot -1
            if p<x:
                res = pivot
                l = pivot +1

        return res


class TestSqrt(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_zero(self):
        self.assertEqual(self.solution.sqrt(0), 0)

    def test_one(self):
        self.assertEqual(self.solution.sqrt(1), 1)

    def test_perfect_square(self):
        self.assertEqual(self.solution.sqrt(4), 2)
        self.assertEqual(self.solution.sqrt(9), 3)
        self.assertEqual(self.solution.sqrt(16), 4)
        self.assertEqual(self.solution.sqrt(25), 5)
        self.assertEqual(self.solution.sqrt(100), 10)
        self.assertEqual(self.solution.sqrt(121), 11)
        self.assertEqual(self.solution.sqrt(10000), 100)

    def test_non_perfect_square(self):
        self.assertEqual(self.solution.sqrt(2), 1)
        self.assertEqual(self.solution.sqrt(3), 1)
        self.assertEqual(self.solution.sqrt(5), 2)
        self.assertEqual(self.solution.sqrt(8), 2)
        self.assertEqual(self.solution.sqrt(10), 3)
        self.assertEqual(self.solution.sqrt(15), 3)
        self.assertEqual(self.solution.sqrt(26), 5)
        self.assertEqual(self.solution.sqrt(99), 9)
        self.assertEqual(self.solution.sqrt(120), 10)

    def test_large_numbers(self):
        self.assertEqual(self.solution.sqrt(2147395599), 46339)
        self.assertEqual(self.solution.sqrt(2147483647), 46340)
        self.assertEqual(self.solution.sqrt(999999999), 31622)

if __name__ == "__main__":
    unittest.main()
