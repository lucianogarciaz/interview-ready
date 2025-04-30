package main

// 4 -> 2
// 1, 2

// 8
// n  multiply
// 1  1
// 2  4
// 3  9
import (
	"testing"
)

func TestMySqrt(t *testing.T) {
	testCases := []struct {
		name     string
		input    int
		expected int
	}{
		{
			name:     "Example 1",
			input:    4,
			expected: 2,
		},
		{
			name:     "Example 2",
			input:    8,
			expected: 2,
		},
		{
			name:     "Zero",
			input:    0,
			expected: -1,
		},
		{
			name:     "One",
			input:    1,
			expected: 1,
		},
		{
			name:     "Perfect Square",
			input:    16,
			expected: 4,
		},
		{
			name:     "Perfect Square",
			input:    9,
			expected: 3,
		},
		{
			name:     "Large Number",
			input:    2147395599,
			expected: 46339,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := mySqrt(tc.input)
			if result != tc.expected {
				t.Errorf("mySqrt(%d) = %d; want %d", tc.input, result, tc.expected)
			}
		})
	}
}
