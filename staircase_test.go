package main

import (
	"testing"
)

func TestClimbStairs(t *testing.T) {
	testCases := []struct {
		name     string
		input    int
		expected int
	}{
		{
			name:     "Example 1",
			input:    2,
			expected: 2,
		},
		{
			name:     "Example 2",
			input:    3,
			expected: 3,
		},
		{
			name:     "One Step",
			input:    1,
			expected: 1,
		},
		{
			name:     "Four Steps",
			input:    4,
			expected: 5,
		},
		{
			name:     "Five Steps",
			input:    5,
			expected: 8,
		},
		{
			name:     "Six Steps",
			input:    6,
			expected: 13,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := climbStairs(tc.input)
			result2 := climbStairs2(tc.input)
			if result != tc.expected {
				t.Errorf("climbStairs(%d) = %d; want %d", tc.input, result, tc.expected)
			}

			if result2 != tc.expected {
				t.Errorf("climbStairs(%d) = %d; want %d", tc.input, result2, tc.expected)
			}
		})
	}
}
