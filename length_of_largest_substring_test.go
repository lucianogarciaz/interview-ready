package main

import "testing"

func TestLengthOfLongestSubstring(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "Example 1: abcabcbb",
			input:    "abcabcbb",
			expected: 3,
		},
		{
			name:     "Example 2: bbbbb",
			input:    "bbbbb",
			expected: 1,
		},
		{
			name:     "Example 3: pwwkew",
			input:    "pwwkew",
			expected: 3,
		},
		{
			name:     "Additional case: dvdf",
			input:    "dvdf",
			expected: 3,
		},
		{
			name:     "Additional case: tmmzuxt",
			input:    "tmmzuxt",
			expected: 5,
		},
		{
			name:     "Empty string",
			input:    "",
			expected: 0,
		},
		{
			name:     "Single character",
			input:    "a",
			expected: 1,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := lengthOfLongestSubstring(tc.input)
			if result != tc.expected {
				t.Errorf("lengthOfLongestSubstring(%q) = %d; want %d", tc.input, result, tc.expected)
			}
		})
	}
}
