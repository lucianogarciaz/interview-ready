package main

import "math"

// Type: Dynamic Programming / Memoization
// Difficulty: Easy
// Companies: This is LeetCode problem #746 "Min Cost Climbing Stairs".
// Commonly asked at companies like Amazon, Microsoft, and Google.
// Tests understanding of dynamic programming and memoization techniques.

// [1,100,1,2,100,1,1,100,1]
func minCostClimbingStairs(cost []int) int {
	// [10, 15, 20]
	memo := make([]int, len(cost))
	for i := 0; i < len(memo); i++ {
		memo[i] = -1
	}

	var dfs func(i int) int
	dfs = func(i int) int {
		if len(cost) <= i {
			return 0
		}

		if memo[i] != -1 {
			return memo[i]
		}

		min := int(math.Min(float64(dfs(i+1)), float64(dfs(i+2))))
		memo[i] = cost[i] + min
		return memo[i]
	}

	return int(math.Min(float64(dfs(0)), float64(dfs(1))))
}
