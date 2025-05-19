package main

import "testing"

func TestLongestPalindrome(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		expected string
	}{
		{
			name:     "Example 1",
			input:    "babad",
			expected: "bab",
		},
		{
			name:     "Example 2",
			input:    "cbbd",
			expected: "bb",
		},
		{
			name:     "Single character",
			input:    "a",
			expected: "a",
		},
		{
			name:     "Empty string",
			input:    "",
			expected: "",
		},
		{
			name:     "All same characters",
			input:    "aaaa",
			expected: "aaaa",
		},
		{
			name:     "No palindrome",
			input:    "abc",
			expected: "a",
		},
		{
			name:     "Long palindrome in middle",
			input:    "racecar",
			expected: "racecar",
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := longestPalindrome(tc.input)
			if result != tc.expected {
				t.Errorf("Expected %s, but got %s", tc.expected, result)
			}
		})
	}
}
