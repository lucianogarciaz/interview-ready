import unittest

class Solution:
    def __init__(self):
        self.memo = {0:0, 1:1,2:2}
    def climbStairs(self, n:int)->int:
        if n in self.memo:
            return self.memo[n]
        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n]=res
        return res

class TestClimbStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_base_cases(self):
        self.assertEqual(self.solution.climbStairs(0), 0)
        self.assertEqual(self.solution.climbStairs(1), 1)
        self.assertEqual(self.solution.climbStairs(2), 2)

    def test_small_numbers(self):
        self.assertEqual(self.solution.climbStairs(3), 3)
        self.assertEqual(self.solution.climbStairs(4), 5)
        self.assertEqual(self.solution.climbStairs(5), 8)
        self.assertEqual(self.solution.climbStairs(6), 13)

    def test_medium_numbers(self):
        self.assertEqual(self.solution.climbStairs(10), 89)
        self.assertEqual(self.solution.climbStairs(15), 987)

    def test_large_number(self):
        self.assertEqual(self.solution.climbStairs(30), 1346269)

    def test_monotonicity(self):
        # climbStairs(n) should be strictly increasing for n >= 1
        prev = self.solution.climbStairs(1)
        for n in range(2, 20):
            curr = self.solution.climbStairs(n)
            self.assertGreater(curr, prev)
            prev = curr

if __name__ == "__main__":
    unittest.main()
