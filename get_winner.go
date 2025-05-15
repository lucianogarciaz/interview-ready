package main

// Type: Array / Simulation / Greedy
// Difficulty: Medium
// Companies: This is LeetCode problem #1535 "Find the Winner of an Array Game".
// Asked at companies like Amazon, Microsoft, and Google.
// Tests understanding of array traversal and game simulation logic.

func getWinner(arr []int, k int) int {
	pivot := arr[0]
	winCount := 0

	for i := 1; i < len(arr); i++ {
		if winCount >= k {
			return pivot
		}
		if pivot > arr[i] {
			winCount++
			continue
		}
		winCount = 1
		pivot = arr[i]
	}

	return pivot
}
