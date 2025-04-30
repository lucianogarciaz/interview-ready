package main

import (
	"testing"
)

func TestLongestCommonPrefix(t *testing.T) {
	testCases := []struct {
		name     string
		input    []string
		expected string
	}{
		{
			name:     "Common prefix 'fl'",
			input:    []string{"flower", "flow", "flight"},
			expected: "fl",
		},
		{
			name:     "No common prefix",
			input:    []string{"dog", "racecar", "car"},
			expected: "",
		},
		{
			name:     "Single string",
			input:    []string{"hello"},
			expected: "hello",
		},
		{
			name:     "Empty array",
			input:    []string{},
			expected: "",
		},
		{
			name:     "Array with empty string",
			input:    []string{"", "abc", "def"},
			expected: "",
		},
		{
			name:     "All identical strings",
			input:    []string{"abc", "abc", "abc"},
			expected: "abc",
		},
		{
			name:     "First letter different",
			input:    []string{"a", "b"},
			expected: "",
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := longestCommonPrefix(tc.input)
			if result != tc.expected {
				t.Errorf("longestCommonPrefix(%v) = %s; want %s", tc.input, result, tc.expected)
			}
		})
	}
}
