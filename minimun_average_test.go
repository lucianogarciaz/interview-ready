package main

import "testing"

func TestMinimumAverageDifference(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{
			name:     "Example 1",
			nums:     []int{2, 5, 3, 9, 5, 3},
			expected: 3,
		},
		{
			name:     "Example 2",
			nums:     []int{0},
			expected: 0,
		},
		{
			name:     "Empty array",
			nums:     []int{},
			expected: 0,
		},
		{
			name:     "Single element",
			nums:     []int{1},
			expected: 0,
		},
		{
			name:     "Two elements",
			nums:     []int{1, 2},
			expected: 0,
		},
		{
			name:     "Example 3",
			nums:     []int{4, 2, 0},
			expected: 2,
		},
		{
			name:     "Example 3",
			nums:     []int{0, 0, 0, 0},
			expected: 0,
		},
		{
			name:     "Example 5",
			nums:     []int{5, 0},
			expected: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := minimumAverageDifference(tt.nums)
			if result != tt.expected {
				t.Errorf("minimumAverageDifference(%v) = %v, want %v", tt.nums, result, tt.expected)
			}
		})
	}
}
