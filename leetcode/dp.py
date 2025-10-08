import unittest

class Solution:
    def __init__(self):
        self.cachefib = {}
        self.cclimb = {0:0, 1:1, 2:2 }

    def climbStairsBU(self, n:int)->int:
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[0],dp[1],dp[2] = 0,1,2
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]

    def climbStairs(self, n:int)->int:
        if n in self.cclimb:
            return self.cclimb[n]
        a = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cclimb[n] = a
        return a

    def fib(self, n: int)->int:
        if n <=1:
            return n
        if n in self.cachefib:
            return self.cachefib[n]
        res = self.fib(n-1) + self.fib(n-2)
        self.cachefib[n] = res
        return res



class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fib_calculator = Solution()
    
    def test_fib_base_case_zero(self):
        self.assertEqual(self.fib_calculator.fib(0), 0)
    
    def test_fib_base_case_one(self):
        self.assertEqual(self.fib_calculator.fib(1), 1)
    
    def test_fib_small_numbers(self):
        self.assertEqual(self.fib_calculator.fib(2), 1)
        self.assertEqual(self.fib_calculator.fib(3), 2)
        self.assertEqual(self.fib_calculator.fib(4), 3)
        self.assertEqual(self.fib_calculator.fib(5), 5)
        self.assertEqual(self.fib_calculator.fib(6), 8)
    
    def test_fib_medium_numbers(self):
        self.assertEqual(self.fib_calculator.fib(10), 55)
        self.assertEqual(self.fib_calculator.fib(15), 610)
        self.assertEqual(self.fib_calculator.fib(20), 6765)
    
    def test_fib_large_numbers(self):
        self.assertEqual(self.fib_calculator.fib(30), 832040)
        self.assertEqual(self.fib_calculator.fib(35), 9227465)
    
    def test_fib_caching_works(self):
        fib_calc = Solution()
        result1 = fib_calc.fib(10)
        self.assertIn(10, fib_calc.cachefib)
        self.assertIn(9, fib_calc.cachefib)
        self.assertIn(8, fib_calc.cachefib)
        self.assertEqual(result1, 55)
        
        result2 = fib_calc.fib(10)
        self.assertEqual(result1, result2)
    
    def test_fib_sequence(self):
        expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, expected in enumerate(expected_sequence):
            with self.subTest(n=i):
                self.assertEqual(self.fib_calculator.fib(i), expected)
    
    def test_multiple_instances_independent_caches(self):
        fib1 = Solution()
        fib2 = Solution()
        
        fib1.fib(10)
        self.assertTrue(len(fib1.cachefib) > 0)
        self.assertEqual(len(fib2.cachefib), 0)
class TestClimbStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_climb_base_case_zero(self):
        self.assertEqual(self.solution.climbStairs(0), 0)
    
    def test_climb_base_case_one(self):
        self.assertEqual(self.solution.climbStairs(1), 1)
    
    def test_climb_base_case_two(self):
        self.assertEqual(self.solution.climbStairs(2), 2)
    
    def test_climb_small_numbers(self):
        self.assertEqual(self.solution.climbStairs(3), 3)
        self.assertEqual(self.solution.climbStairs(4), 5)
        self.assertEqual(self.solution.climbStairs(5), 8)
        self.assertEqual(self.solution.climbStairs(6), 13)
    
    def test_climb_medium_numbers(self):
        self.assertEqual(self.solution.climbStairs(10), 89)
        self.assertEqual(self.solution.climbStairs(15), 987)
        self.assertEqual(self.solution.climbStairs(20), 10946)
    
    def test_climb_large_numbers(self):
        self.assertEqual(self.solution.climbStairs(30), 1346269)
        self.assertEqual(self.solution.climbStairs(35), 14930352)
    
    def test_climb_caching_works(self):
        sol = Solution()
        result1 = sol.climbStairs(10)
        self.assertIn(10, sol.cclimb)
        self.assertIn(9, sol.cclimb)
        self.assertIn(8, sol.cclimb)
        self.assertEqual(result1, 89)
        
        result2 = sol.climbStairs(10)
        self.assertEqual(result1, result2)
    
    def test_climb_sequence(self):
        expected_sequence = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for i, expected in enumerate(expected_sequence):
            with self.subTest(n=i):
                self.assertEqual(self.solution.climbStairs(i), expected)
    
    def test_climb_multiple_instances_independent_caches(self):
        sol1 = Solution()
        sol2 = Solution()
        
        sol1.climbStairs(10)
        self.assertTrue(len(sol1.cclimb) > 3)
        self.assertEqual(len(sol2.cclimb), 3)
    
    def test_climb_efficiency_large_input(self):
        sol = Solution()
        result = sol.climbStairs(40)
        self.assertEqual(result, 165580141)
        self.assertIn(40, sol.cclimb)


class TestClimbStairsBU(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_climb_bu_base_case_zero(self):
        self.assertEqual(self.solution.climbStairsBU(0), 0)
    
    def test_climb_bu_base_case_one(self):
        self.assertEqual(self.solution.climbStairsBU(1), 1)
    
    def test_climb_bu_base_case_two(self):
        self.assertEqual(self.solution.climbStairsBU(2), 2)
    
    def test_climb_bu_small_numbers(self):
        self.assertEqual(self.solution.climbStairsBU(3), 3)
        self.assertEqual(self.solution.climbStairsBU(4), 5)
        self.assertEqual(self.solution.climbStairsBU(5), 8)
        self.assertEqual(self.solution.climbStairsBU(6), 13)
    
    def test_climb_bu_medium_numbers(self):
        self.assertEqual(self.solution.climbStairsBU(10), 89)
        self.assertEqual(self.solution.climbStairsBU(15), 987)
        self.assertEqual(self.solution.climbStairsBU(20), 10946)
    
    def test_climb_bu_large_numbers(self):
        self.assertEqual(self.solution.climbStairsBU(30), 1346269)
        self.assertEqual(self.solution.climbStairsBU(35), 14930352)
    
    def test_climb_bu_sequence(self):
        expected_sequence = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for i, expected in enumerate(expected_sequence):
            with self.subTest(n=i):
                self.assertEqual(self.solution.climbStairsBU(i), expected)
    
    def test_climb_bu_matches_recursive(self):
        for n in range(0, 20):
            with self.subTest(n=n):
                sol = Solution()
                bu_result = sol.climbStairsBU(n)
                recursive_result = sol.climbStairs(n)
                self.assertEqual(bu_result, recursive_result, 
                                f"Bottom-up and recursive methods differ at n={n}")
    
    def test_climb_bu_no_cache_pollution(self):
        sol = Solution()
        initial_cache_size = len(sol.cclimb)
        sol.climbStairsBU(10)
        final_cache_size = len(sol.cclimb)
        self.assertEqual(initial_cache_size, final_cache_size)
    
    def test_climb_bu_efficiency(self):
        sol = Solution()
        result = sol.climbStairsBU(40)
        self.assertEqual(result, 165580141)
if __name__ == '__main__':
    unittest.main()