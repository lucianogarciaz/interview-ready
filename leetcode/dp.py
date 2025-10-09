import unittest
from typing import List

class Solution:
    def __init__(self):
        self.cachefib = {}
        self.cclimb = {0:0, 1:1, 2:2 }

    def coinChange2(self, arr:List[int], amount:int)->int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        arr.sort()
        for c in arr:
            for i in range(c, amount + 1):
                dp[i] += dp[i-c]
        return dp[amount]

    def coinChange(self, arr:List[int], amount:int)->int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        arr.sort()
        for i in range(1, amount+1):
            for c in arr:
                if c>i:
                    break
                dp[i] = min(dp[i], 1+dp[i-c])
        return dp[amount] if dp[amount]!=float('inf') else -1

    def coinChangeTopDown(self, arr:List[int], amount:int)->int:
        memo = {}
        def backtrack(rem:int):
            if rem in memo:
                return memo[rem]
            if rem == 0:
                return rem
            if rem < 0:
                return float('inf')
            best = float('inf')
            for c in arr:
                best = min(best, 1 + backtrack(rem-c))
            memo[rem] = best
            return best
        ans = backtrack(amount)
        return ans if ans!=float('inf') else -1 

    def houseRob(self, arr: List[int])->int:
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return arr[0]
        dp = [0] * len(arr)
        dp[0], dp[1] = arr[0], max(arr[0],arr[1])
        for i in range(2, len(arr)):
            dp[i] = max(dp[i-1], dp[i-2] + arr[i])
        return dp[-1]
        

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
class TestCoinChange2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_coin_change2_zero_amount(self):
        self.assertEqual(self.solution.coinChange2([1, 2, 5], 0), 1)
    
    def test_coin_change2_single_coin_exact(self):
        self.assertEqual(self.solution.coinChange2([1], 1), 1)
        self.assertEqual(self.solution.coinChange2([5], 5), 1)
        self.assertEqual(self.solution.coinChange2([10], 10), 1)
    
    def test_coin_change2_single_coin_multiple_ways(self):
        self.assertEqual(self.solution.coinChange2([1], 5), 1)
        self.assertEqual(self.solution.coinChange2([2], 6), 1)
    
    def test_coin_change2_impossible(self):
        self.assertEqual(self.solution.coinChange2([2], 3), 0)
        self.assertEqual(self.solution.coinChange2([5, 10], 3), 0)
    
    def test_coin_change2_leetcode_example_1(self):
        self.assertEqual(self.solution.coinChange2([1, 2, 5], 5), 4)
    
    def test_coin_change2_leetcode_example_2(self):
        self.assertEqual(self.solution.coinChange2([2], 3), 0)
    
    def test_coin_change2_leetcode_example_3(self):
        self.assertEqual(self.solution.coinChange2([10], 10), 1)
    
    def test_coin_change2_small_amounts(self):
        self.assertEqual(self.solution.coinChange2([1, 2, 5], 4), 3)
        self.assertEqual(self.solution.coinChange2([1, 2, 5], 3), 2)
    
    def test_coin_change2_multiple_combinations(self):
        self.assertEqual(self.solution.coinChange2([1, 2, 3], 4), 4)
        self.assertEqual(self.solution.coinChange2([1, 2, 5], 7), 6)
    
    def test_coin_change2_large_amount(self):
        self.assertEqual(self.solution.coinChange2([1, 2, 5], 10), 10)
        self.assertEqual(self.solution.coinChange2([1, 2, 5], 11), 11)
    
    def test_coin_change2_empty_coins(self):
        self.assertEqual(self.solution.coinChange2([], 5), 0)
        self.assertEqual(self.solution.coinChange2([], 0), 1)
        
    def test_coin_change2_all_ones(self):
        self.assertEqual(self.solution.coinChange2([1], 10), 1)
        self.assertEqual(self.solution.coinChange2([1], 100), 1)
        
    def test_coin_change2_edge_cases(self):
        self.assertEqual(self.solution.coinChange2([1, 5, 10, 25], 25), 13)
        self.assertEqual(self.solution.coinChange2([3, 5], 9), 1)
class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_coin_change_zero_amount(self):
        self.assertEqual(self.solution.coinChange([1, 2, 5], 0), 0)
    
    def test_coin_change_impossible(self):
        self.assertEqual(self.solution.coinChange([2], 3), -1)
        self.assertEqual(self.solution.coinChange([5, 10], 3), -1)
    
    def test_coin_change_single_coin_exact(self):
        self.assertEqual(self.solution.coinChange([1], 1), 1)
        self.assertEqual(self.solution.coinChange([5], 5), 1)
        self.assertEqual(self.solution.coinChange([10], 10), 1)
    
    def test_coin_change_single_coin_multiple(self):
        self.assertEqual(self.solution.coinChange([1], 5), 5)
        self.assertEqual(self.solution.coinChange([2], 6), 3)
    
    def test_coin_change_leetcode_example_1(self):
        self.assertEqual(self.solution.coinChange([1, 2, 5], 11), 3)
    
    def test_coin_change_leetcode_example_2(self):
        self.assertEqual(self.solution.coinChange([2], 3), -1)
    
    def test_coin_change_leetcode_example_3(self):
        self.assertEqual(self.solution.coinChange([1], 0), 0)
    
    def test_coin_change_small_amounts(self):
        self.assertEqual(self.solution.coinChange([1, 2, 5], 4), 2)
        self.assertEqual(self.solution.coinChange([1, 3, 4], 6), 2)
        self.assertEqual(self.solution.coinChange([1, 5, 10], 12), 3)
    
    def test_coin_change_greedy_fails(self):
        self.assertEqual(self.solution.coinChange([1, 3, 4], 6), 2)
        self.assertEqual(self.solution.coinChange([1, 5, 6, 9], 11), 2)
    
    def test_coin_change_multiple_options(self):
        self.assertEqual(self.solution.coinChange([1, 2, 5], 7), 2)
        self.assertEqual(self.solution.coinChange([1, 2, 5], 8), 3)
        self.assertEqual(self.solution.coinChange([1, 2, 5], 10), 2)
    
    def test_coin_change_large_coins_only(self):
        self.assertEqual(self.solution.coinChange([5, 10, 25], 30), 2)
        self.assertEqual(self.solution.coinChange([5, 10, 25], 40), 3)
    
    def test_coin_change_all_ones(self):
        self.assertEqual(self.solution.coinChange([1], 10), 10)
    
    def test_coin_change_optimal_selection(self):
        self.assertEqual(self.solution.coinChange([1, 5, 6, 8], 11), 2)
        self.assertEqual(self.solution.coinChange([2, 5, 10, 1], 27), 4)
    
    def test_coin_change_empty_coins(self):
        self.assertEqual(self.solution.coinChange([], 5), -1)
    
    def test_coin_change_medium_amount(self):
        self.assertEqual(self.solution.coinChange([1, 5, 10, 25], 63), 6)
        self.assertEqual(self.solution.coinChange([1, 2, 5, 10], 18), 4)

class TestHouseRob(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_house_rob_empty_array(self):
        self.assertEqual(self.solution.houseRob([]), 0)
    
    def test_house_rob_single_house(self):
        self.assertEqual(self.solution.houseRob([5]), 5)
        self.assertEqual(self.solution.houseRob([100]), 100)
    
    def test_house_rob_two_houses(self):
        self.assertEqual(self.solution.houseRob([1, 2]), 2)
        self.assertEqual(self.solution.houseRob([5, 1]), 5)
        self.assertEqual(self.solution.houseRob([2, 7]), 7)
    
    def test_house_rob_small_arrays(self):
        self.assertEqual(self.solution.houseRob([1, 2, 3]), 4)
        self.assertEqual(self.solution.houseRob([2, 7, 9, 3]), 11)
        self.assertEqual(self.solution.houseRob([5, 3, 4, 11, 2]), 16)
    
    def test_house_rob_classic_example(self):
        self.assertEqual(self.solution.houseRob([2, 7, 9, 3, 1]), 12)
    
    def test_house_rob_alternating_pattern(self):
        self.assertEqual(self.solution.houseRob([1, 3, 1, 3, 1]), 6)
    
    def test_house_rob_increasing_values(self):
        self.assertEqual(self.solution.houseRob([1, 2, 3, 4, 5]), 9)
    
    def test_house_rob_decreasing_values(self):
        self.assertEqual(self.solution.houseRob([5, 4, 3, 2, 1]), 9)
    
    def test_house_rob_all_same_values(self):
        self.assertEqual(self.solution.houseRob([5, 5, 5, 5, 5]), 15)
        self.assertEqual(self.solution.houseRob([3, 3, 3, 3]), 6)
    
    def test_house_rob_large_value_at_start(self):
        self.assertEqual(self.solution.houseRob([10, 1, 1, 1, 1]), 12)
    
    def test_house_rob_large_value_at_end(self):
        self.assertEqual(self.solution.houseRob([1, 1, 1, 1, 10]), 12)
    
    def test_house_rob_large_value_in_middle(self):
        self.assertEqual(self.solution.houseRob([1, 1, 10, 1, 1]), 12)
    
    def test_house_rob_with_zeros(self):
        self.assertEqual(self.solution.houseRob([0, 0, 0, 0]), 0)
        self.assertEqual(self.solution.houseRob([5, 0, 0, 5]), 10)
    
    def test_house_rob_leetcode_example_1(self):
        self.assertEqual(self.solution.houseRob([1, 2, 3, 1]), 4)
    
    def test_house_rob_leetcode_example_2(self):
        self.assertEqual(self.solution.houseRob([2, 1, 1, 2]), 4)
    
    def test_house_rob_longer_array(self):
        self.assertEqual(self.solution.houseRob([5, 3, 4, 11, 2, 8, 6, 1]), 25)
        self.assertEqual(self.solution.houseRob([9, 1, 1, 9, 1, 1, 9]), 27)

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