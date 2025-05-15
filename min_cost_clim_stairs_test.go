package main

import "testing"

func TestMinCostClimbingStairs(t *testing.T) {
	testCases := []struct {
		name     string
		cost     []int
		expected int
	}{
		{
			name:     "Example 1",
			cost:     []int{10, 15, 20},
			expected: 15,
		},
		{
			name:     "Example 2",
			cost:     []int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1},
			expected: 6,
		},
		{
			name:     "Empty array",
			cost:     []int{},
			expected: 0,
		},
		{
			name:     "Single element",
			cost:     []int{5},
			expected: 5,
		},
		{
			name:     "Two elements",
			cost:     []int{5, 10},
			expected: 5,
		},
		{
			name:     "All same cost",
			cost:     []int{2, 2, 2, 2},
			expected: 4,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := minCostClimbingStairs(tc.cost)
			if result != tc.expected {
				t.Errorf("Expected %d, but got %d", tc.expected, result)
			}
		})
	}
}
