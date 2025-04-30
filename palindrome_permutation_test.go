package main

import (
	"testing"
)

func TestIsPalindromePermutation(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		expected bool
	}{
		{
			name:     "Example: Tact Coa",
			input:    "Tact Coa",
			expected: true,
		},
		{
			name:     "Empty string",
			input:    "",
			expected: true,
		},
		{
			name:     "Single character",
			input:    "a",
			expected: true,
		},
		{
			name:     "Palindrome - even length",
			input:    "abba",
			expected: true,
		},
		{
			name:     "Palindrome - odd length",
			input:    "racecar",
			expected: true,
		},
		{
			name:     "Not a palindrome permutation",
			input:    "hello",
			expected: false,
		},
		{
			name:     "Permutation of palindrome - even length",
			input:    "aabb",
			expected: true,
		},
		{
			name:     "Permutation of palindrome - odd length",
			input:    "aabc",
			expected: false,
		},
		{
			name:     "Case insensitive palindrome permutation",
			input:    "Able was I ere I saw Elba",
			expected: true,
		},
		{
			name:     "With special characters and spaces",
			input:    "A man, a plan, a canal: Panama",
			expected: false,
		},
		{
			name:     "Not a palindrome permutation with special chars",
			input:    "Hello, World!",
			expected: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := palindromPermutation2(tc.input)
			// result := isPalindromePermutation(tc.input)
			if result != tc.expected {
				t.Errorf("isPalindromePermutation(%q) = %v; want %v", tc.input, result, tc.expected)
			}
		})
	}
}
