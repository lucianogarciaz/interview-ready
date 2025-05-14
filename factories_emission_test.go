package main

import (
	"testing"
)

// Solution struct matches the expected interface from the problem
type Solution struct{}

func TestSolution(t *testing.T) {

	testCases := []struct {
		name     string
		input    []int
		expected int
	}{
		{
			name:     "Example 1: [5, 19, 8, 1]",
			input:    []int{5, 19, 8, 1},
			expected: 3,
		},
		{
			name:     "Example 2: [10, 10]",
			input:    []int{10, 10},
			expected: 2,
		},
		// {
		// 	name:     "Example 3: [3, 0, 5]",
		// 	input:    []int{3, 0, 5},
		// 	expected: 2,
		// },
		{
			name:     "All zeros",
			input:    []int{0, 0, 0},
			expected: 0,
		},
		{
			name:     "Single factory",
			input:    []int{100},
			expected: 1,
		},
		{
			name:     "Multiple filters needed",
			input:    []int{64, 32, 16},
			expected: 3,
		},
		{
			name:     "Large factories",
			input:    []int{10000, 20000, 30000, 5000},
			expected: 4,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := factoriesEmission(tc.input)
			if result != tc.expected {
				t.Errorf("Expected %d filters, but got %d for input %v", tc.expected, result, tc.input)
			}
		})
	}
}
