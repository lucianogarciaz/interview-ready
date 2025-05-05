package main

import "testing"

func TestTripleStep(t *testing.T) {
	testCases := []struct {
		name     string
		n        int
		expected int
	}{
		{
			name:     "Base case: 0 steps",
			n:        0,
			expected: 0,
		},
		{
			name:     "Base case: 1 step",
			n:        1,
			expected: 1,
		},
		{
			name:     "Base case: 2 steps",
			n:        2,
			expected: 2,
		},
		{
			name:     "Base case: 3 steps",
			n:        3,
			expected: 4,
		},
		{
			name:     "Example: 4 steps",
			n:        4,
			expected: 7,
		},
		{
			name:     "Example: 5 steps",
			n:        5,
			expected: 13,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := tripleStep(tc.n)
			if result != tc.expected {
				t.Errorf("tripleStep(%d) = %d; want %d", tc.n, result, tc.expected)
			}
		})
	}
}
