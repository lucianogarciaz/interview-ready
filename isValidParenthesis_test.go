package main

import (
	"testing"
)

func TestIsValid(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		expected bool
	}{
		{
			name:     "Simple valid parentheses",
			input:    "()",
			expected: true,
		},
		{
			name:     "Multiple valid brackets",
			input:    "()[]{}",
			expected: true,
		},
		{
			name:     "Mismatched brackets",
			input:    "(]",
			expected: false,
		},
		{
			name:     "Nested valid brackets",
			input:    "([{}])",
			expected: true,
		},
		{
			name:     "Unbalanced opening brackets",
			input:    "([",
			expected: false,
		},
		{
			name:     "Unbalanced closing brackets",
			input:    ")]",
			expected: false,
		},
		{
			name:     "Complex valid nesting",
			input:    "{[()]}",
			expected: true,
		},
		{
			name:     "Incorrect closing order",
			input:    "([)]",
			expected: false,
		},
		{
			name:     "Empty string",
			input:    "",
			expected: true,
		},
		{
			name:     "Single opening bracket",
			input:    "[",
			expected: false,
		},
		{
			name:     "Single closing bracket",
			input:    "]",
			expected: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := isValid(tc.input)
			if result != tc.expected {
				t.Errorf("isValid(%s) = %v; want %v", tc.input, result, tc.expected)
			}
		})
	}
}
