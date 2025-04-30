package main

import (
	"reflect"
	"testing"
)

func TestPlusOne(t *testing.T) {
	testCases := []struct {
		name     string
		digits   []int
		expected []int
	}{
		{
			name:     "Example 1",
			digits:   []int{1, 2, 3},
			expected: []int{1, 2, 4},
		},
		{
			name:     "Example 2",
			digits:   []int{4, 3, 2, 1},
			expected: []int{4, 3, 2, 2},
		},
		{
			name:     "Example with 9",
			digits:   []int{9},
			expected: []int{1, 0},
		},
		{
			name:     "Example with multiple 9s",
			digits:   []int{9, 9},
			expected: []int{1, 0, 0},
		},
		{
			name:     "Example with 9 in the middle",
			digits:   []int{1, 9, 9},
			expected: []int{2, 0, 0},
		},
		{
			name:     "Example with 9 at the end",
			digits:   []int{1, 2, 9},
			expected: []int{1, 3, 0},
		},
		{
			name:     "Zero",
			digits:   []int{0},
			expected: []int{1},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// Create a copy of the input to avoid modifying the test case
			input := make([]int, len(tc.digits))
			copy(input, tc.digits)

			result := plusOne(input)
			if !reflect.DeepEqual(result, tc.expected) {
				t.Errorf("plusOne(%v) = %v; want %v", tc.digits, result, tc.expected)
			}
		})
	}
}
