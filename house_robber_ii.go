package main

import (
	"math"
	"slices"
)

// Type: Dynamic Programming
// Difficulty: Medium
// Companies: This is LeetCode problem #213 "House Robber II ". Frequently asked at
// companies like Amazon, Microsoft, and Google. Tests understanding of dynamic
// programming and memoization techniques.

// Input: nums = [1, 8, 1, 1,1000] 0

func robII(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}

	secondSlice := slices.Clone(nums)
	nums = nums[:len(nums)-1]
	one := robHelper(nums)
	secondSlice = secondSlice[1:]
	two := robHelper(secondSlice)

	return int(math.Max(float64(one), float64(two)))
}

func robHelper(nums []int) int {
	memo := make([]int, len(nums))
	for i := 0; i < len(memo); i++ {
		memo[i] = -1
	}
	var dp func(i int) int
	dp = func(i int) int {
		if len(nums) <= i {
			return 0
		}
		if memo[i] != -1 {
			return memo[i]
		}
		memo[i] = int(math.Max(float64(dp(i+1)), float64(dp(i+2)+nums[i])))
		return memo[i]
	}

	return dp(0)
}
