package main

import "math"

// Type: Sliding Window / Greedy Algorithm
// Difficulty: Easy
// Companies: This is LeetCode problem #121 "Best Time to Buy and Sell Stock".
// One of the most frequently asked problems at major tech companies including
// Amazon, Facebook, Microsoft, Google, and Apple. It tests understanding of
// array traversal and optimization problems.

func maxProfit(prices []int) int {
	l, r := 0, 1
	maxP := 0
	if len(prices) <= 1 {
		return maxP
	}

	// [3, 4, 6, 5, 0, 3]
	for r < len(prices) {
		if prices[l] < prices[r] {
			profit := prices[r] - prices[l]
			maxP = int(math.Max(float64(profit), float64(maxP)))
		} else {
			l = r
		}

		r++
	}

	return maxP
}

func maxProfitWithoutSlidingWindow(prices []int) int {
	sell := 0
	sellIndex := 0
	if len(prices) <= 1 {
		return sellIndex
	}

	buy := prices[0]
	profit := 0

	for i := 1; i < len(prices); i++ {
		if buy > prices[i] {
			buy = prices[i]
			sell = prices[i]
		}
		if prices[i] > sell {
			sell = prices[i]
		}
		if (sell - buy) > profit {
			profit = sell - buy
		}
	}

	return profit
}
