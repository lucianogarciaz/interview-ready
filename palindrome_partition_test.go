package main

import (
	"slices"
	"testing"
)

func TestPartitionPalindrome(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected [][]string
	}{
		{
			name:     "empty string",
			input:    "",
			expected: [][]string{},
		},
		{
			name:     "single character",
			input:    "a",
			expected: [][]string{{"a"}},
		},
		{
			name:  "palindrome string",
			input: "aab",
			expected: [][]string{
				{"a", "a", "b"},
				{"aa", "b"},
			},
		},
		{
			name:  "longer palindrome string",
			input: "aabb",
			expected: [][]string{
				{"a", "a", "b", "b"},
				{"a", "a", "bb"},
				{"aa", "b", "b"},
				{"aa", "bb"},
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := partitionPalindrome(tt.input)
			if !areStringSlicesEqual(result, tt.expected) {
				t.Errorf("partitionPalindrome(%q) = %v; want %v",
					tt.input, result, tt.expected)
			}
		})
	}
}

func areStringSlicesEqual(a, b [][]string) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if !slices.Equal(a[i], b[i]) {
			return false
		}
	}
	return true
}
