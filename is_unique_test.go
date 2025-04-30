package main

import (
	"testing"
)

func TestIsUnique(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		expected bool
	}{
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
			name:     "All unique characters",
			input:    "abcdefg",
			expected: true,
		},
		{
			name:     "Duplicate characters",
			input:    "hello",
			expected: false,
		},
		{
			name:     "All unique with numbers and special chars",
			input:    "abcde123!@#",
			expected: true,
		},
		{
			name:     "Duplicate with numbers and special chars",
			input:    "abcde123!@#a",
			expected: false,
		},
		{
			name:     "Case sensitive - all unique",
			input:    "abcABC",
			expected: true,
		},
		{
			name:     "Case sensitive - duplicates",
			input:    "abcABCa",
			expected: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := isUnique(tc.input)
			if result != tc.expected {
				t.Errorf("isUnique(%q) = %v; want %v", tc.input, result, tc.expected)
			}

			result = isUnique2(tc.input)
			if result != tc.expected {
				t.Errorf("isUnique(%q) = %v; want %v", tc.input, result, tc.expected)
			}

			result = isUnique3(tc.input)
			if result != tc.expected {
				t.Errorf("isUnique(%q) = %v; want %v", tc.input, result, tc.expected)
			}
		})
	}
}
