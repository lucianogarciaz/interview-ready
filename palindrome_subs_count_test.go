package main

import "testing"

func TestCountSubstrings(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "Example 1",
			input:    "abc",
			expected: 3, // "a", "b", "c"
		},
		{
			name:     "Example 2",
			input:    "aaa",
			expected: 6, // "a", "a", "a", "aa", "aa", "aaa"
		},
		{
			name:     "Single character",
			input:    "a",
			expected: 1, // "a"
		},
		{
			name:     "Empty string",
			input:    "",
			expected: 0,
		},
		{
			name:     "All same characters",
			input:    "aaaa",
			expected: 10, // "a", "a", "a", "a", "aa", "aa", "aa", "aaa", "aaa", "aaaa"
		},
		{
			name:     "Complex palindrome",
			input:    "racecar",
			expected: 10, // "r", "a", "c", "e", "c", "a", "r", "cec", "aceca", "racecar"
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := countSubstrings(tc.input)
			if result != tc.expected {
				t.Errorf("Expected %d palindromic substrings, but got %d", tc.expected, result)
			}
		})
	}
}
