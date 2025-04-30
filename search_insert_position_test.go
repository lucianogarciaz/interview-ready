package main

import (
	"testing"
)

func TestSearchInsert(t *testing.T) {
	testCases := []struct {
		name     string
		nums     []int
		target   int
		expected int
	}{
		{
			name:     "Example 1: Target found in array",
			nums:     []int{1, 3, 5, 6},
			target:   2,
			expected: 1,
		},
		{
			name:     "Example 2: Target not found, should be inserted in middle",
			nums:     []int{1, 3, 5, 6},
			target:   0,
			expected: 0,
		},
		{
			name:     "Example 3: Target not found, should be inserted at end",
			nums:     []int{1, 3, 5, 6},
			target:   7,
			expected: 4,
		},
		{
			name:     "Target not found, should be inserted at beginning",
			nums:     []int{1, 3, 5, 6},
			target:   0,
			expected: 0,
		},
		{
			name:     "Empty array",
			nums:     []int{},
			target:   5,
			expected: 0,
		},
		{
			name:     "Single element array, target found",
			nums:     []int{5},
			target:   5,
			expected: 0,
		},
		{
			name:     "Single element array, target smaller",
			nums:     []int{5},
			target:   3,
			expected: 0,
		},
		{
			name:     "Single element array, target larger",
			nums:     []int{5},
			target:   7,
			expected: 1,
		},
		{
			name:     "Target equal to last element",
			nums:     []int{1, 3, 5, 6},
			target:   6,
			expected: 3,
		},
		{
			name:     "Target equal to first element",
			nums:     []int{1, 3, 5, 6},
			target:   1,
			expected: 0,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := searchInsert(tc.nums, tc.target)
			if result != tc.expected {
				t.Errorf("searchInsert(%v, %d) = %d, want %d", tc.nums, tc.target, result, tc.expected)
			}
		})
	}
}
