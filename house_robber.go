package main

import "math"

// Type: Dynamic Programming
// Difficulty: Medium
// Companies: This is LeetCode problem #198 "House Robber". Frequently asked at
// companies like Amazon, Microsoft, and Google. Tests understanding of dynamic
// programming and memoization techniques.

// Input: nums = [2, 1, 1, 2]
// botom up solution
func rob(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) <= 1 {
		return nums[0]
	}
	if len(nums) == 2 {
		return int(math.Max(float64(nums[0]), float64(nums[1])))
	}
	dp := make([]int, len(nums))
	dp[0] = nums[0]

	dp[1] = int(math.Max(float64(nums[0]), float64(nums[1]))) // this is done just because if we have something like [2 1 1 2], we need to return 4 instead of 3. For that we want just to know which part of the subarray was smaller.
	for i := 2; i < len(nums); i++ {
		dp[i] = int(math.Max(float64(dp[i-1]), float64(dp[i-2]+nums[i])))
	}

	return dp[len(nums)-1]
}

// top-down solution
func robTD(nums []int) int {
	cost := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		cost[i] = -1
	}

	var tds func(i int) int
	tds = func(i int) int {
		if len(nums) <= i {
			return 0
		}
		if cost[i] != -1 {
			return cost[i]
		}

		cost[i] = int(math.Max(float64(tds(i+1)), float64(tds(i+2)+nums[i])))
		return cost[i]
	}
	return tds(0)
}
