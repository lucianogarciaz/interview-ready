package main

import "testing"

func TestCharacterReplacement(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		k        int
		expected int
	}{
		{
			name:     "Example 1: ABAB with k=2",
			input:    "ABAB",
			k:        2,
			expected: 4,
		},
		{
			name:     "Example 2: AABABBA with k=1",
			input:    "AABABBA",
			k:        1,
			expected: 4,
		},
		{
			name:     "Empty string",
			input:    "",
			k:        1,
			expected: 0,
		},
		{
			name:     "Single character",
			input:    "A",
			k:        1,
			expected: 1,
		},
		{
			name:     "All same characters",
			input:    "AAAA",
			k:        2,
			expected: 4,
		},
		{
			name:     "No replacements needed",
			input:    "ABCD",
			k:        0,
			expected: 1,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := characterReplacement(tc.input, tc.k)
			if result != tc.expected {
				t.Errorf("characterReplacement(%q, %d) = %d; want %d", tc.input, tc.k, result, tc.expected)
			}
		})
	}
}
