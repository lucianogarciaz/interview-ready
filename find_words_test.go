package main

// [ hu  un  ng ga ar ry]
// [h:u:  u:n:  n:g:  g:a: a:r: r:y]
// find the first letter.
// create the hash set
// loop from the beginning until the end.

import "testing"

func TestFindWords(t *testing.T) {
	testCases := []struct {
		name     string
		input    []string
		expected string
	}{
		{
			name:     "Example 1: [h>u, u>n, n>g, g>a, a>r, r>y]",
			input:    []string{"h>u", "u>n", "n>g", "g>a", "a>r", "r>y"},
			expected: "hungary",
		},
		{
			name:     "Example 2: [a>b, b>c, c>d]",
			input:    []string{"a>b", "b>c", "c>d"},
			expected: "abcd",
		},
		{
			name:     "Single pair",
			input:    []string{"x>y"},
			expected: "xy",
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := findWords(tc.input)
			if result != tc.expected {
				t.Errorf("Expected %s, but got %s for input %v", tc.expected, result, tc.input)
			}
		})
	}
}
