package main

import "testing"

func TestStringConversion(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		expected string
	}{
		{
			name:     "Empty string",
			input:    "",
			expected: "",
		},
		{
			name:     "Single character",
			input:    "a",
			expected: "a",
		},
		{
			name:     "No repeating characters",
			input:    "abcdef",
			expected: "abcdef",
		},
		{
			name:     "Basic compression",
			input:    "aabcccccaaa",
			expected: "a2b1c5a3",
		},
		{
			name:     "Compression not smaller than original",
			input:    "abc",
			expected: "abc",
		},
		{
			name:     "All same characters",
			input:    "aaaaa",
			expected: "a5",
		},
		{
			name:     "Alternating characters",
			input:    "ababab",
			expected: "ababab",
		},
		{
			name:     "Mixed case letters",
			input:    "aAaAaA",
			expected: "aAaAaA",
		},
		{
			name:     "Long repeating sequence",
			input:    "aaaaaaaaaaaabbbbbbbbbbbbcccccccccccc",
			expected: "a12b12c12",
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := stringConversion(tc.input)
			if result != tc.expected {
				t.Errorf("stringConversion(%q) = %q; want %q", tc.input, result, tc.expected)
			}
		})
	}
}
