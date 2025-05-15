package main

import "testing"

// Type: Dynamic Programming
// Difficulty: Medium
// Companies: This is LeetCode problem #198 "House Robber". Frequently asked at
// companies like Amazon, Microsoft, and Google. Tests understanding of dynamic
// programming and memoization techniques.

func TestRob(t *testing.T) {
	testCases := []struct {
		name     string
		nums     []int
		expected int
	}{
		{
			name:     "Example 1",
			nums:     []int{1, 2, 3, 1},
			expected: 4,
		},
		{
			name:     "Example 2",
			nums:     []int{2, 7, 9, 3, 1},
			expected: 12,
		},
		{
			name:     "Empty array",
			nums:     []int{},
			expected: 0,
		},
		{
			name:     "Single element",
			nums:     []int{5},
			expected: 5,
		},
		{
			name:     "Two elements",
			nums:     []int{2, 1},
			expected: 2,
		},
		{
			name:     "Adjacent houses with same value",
			nums:     []int{2, 2, 2, 2},
			expected: 4,
		},
		{
			name:     "Complex case",
			nums:     []int{2, 1, 1, 2},
			expected: 4,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := rob(tc.nums)
			if result != tc.expected {
				t.Errorf("Expected %d, but got %d", tc.expected, result)
			}
		})
	}
}

func TestRob2(t *testing.T) {
	testCases := []struct {
		name     string
		nums     []int
		expected int
	}{
		{
			name:     "Example 1",
			nums:     []int{1, 2, 3, 1},
			expected: 4,
		},
		{
			name:     "Example 2",
			nums:     []int{2, 7, 9, 3, 1},
			expected: 12,
		},
		{
			name:     "Empty array",
			nums:     []int{},
			expected: 0,
		},
		{
			name:     "Single element",
			nums:     []int{5},
			expected: 5,
		},
		{
			name:     "Two elements",
			nums:     []int{2, 1},
			expected: 2,
		},
		{
			name:     "Adjacent houses with same value",
			nums:     []int{2, 2, 2, 2},
			expected: 4,
		},
		{
			name:     "Complex case",
			nums:     []int{2, 1, 1, 2},
			expected: 4,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := rob2(tc.nums)
			if result != tc.expected {
				t.Errorf("Expected %d, but got %d", tc.expected, result)
			}
		})
	}
}
