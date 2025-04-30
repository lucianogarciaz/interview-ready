package main

import (
	"testing"
)

func TestStrStr(t *testing.T) {
	testCases := []struct {
		name     string
		haystack string
		needle   string
		expected int
	}{
		{
			name:     "Example 1: First occurrence at beginning",
			haystack: "sadbutsad",
			needle:   "sad",
			expected: 0,
		},
		{
			name:     "Example 2: Needle not in haystack",
			haystack: "leetcode",
			needle:   "leeto",
			expected: -1,
		},
		{
			name:     "Empty needle",
			haystack: "hello",
			needle:   "",
			expected: -1,
		},
		{
			name:     "Empty haystack",
			haystack: "",
			needle:   "a",
			expected: -1,
		},
		{
			name:     "Needle longer than haystack",
			haystack: "abc",
			needle:   "abcdef",
			expected: -1,
		},
		{
			name:     "Occurrence in the middle",
			haystack: "hello world",
			needle:   "o w",
			expected: 4,
		},
		{
			name:     "Occurrence at the end",
			haystack: "hello",
			needle:   "lo",
			expected: 3,
		},
		{
			name:     "Multiple occurrences",
			haystack: "mississippi",
			needle:   "issi",
			expected: 1,
		},
		{
			name:     "Single character match",
			haystack: "aaaaa",
			needle:   "a",
			expected: 0,
		},
		{
			name:     "Case sensitivity",
			haystack: "Hello",
			needle:   "hello",
			expected: -1,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := strStr(tc.haystack, tc.needle)
			if result != tc.expected {
				t.Errorf("strStr(%q, %q) = %d, want %d", tc.haystack, tc.needle, result, tc.expected)
			}
		})
	}
}
