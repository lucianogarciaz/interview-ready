package main

import (
	"slices"
	"testing"
)

func TestLetterCombinations(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected []string
	}{
		{
			name:     "empty string",
			input:    "",
			expected: []string{},
		},
		{
			name:     "single digit",
			input:    "2",
			expected: []string{"a", "b", "c"},
		},
		{
			name:     "two digits",
			input:    "23",
			expected: []string{"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"},
		},
		{
			name:     "digit with four letters",
			input:    "7",
			expected: []string{"p", "q", "r", "s"},
		},
		{
			name:     "multiple digits including 7 and 9",
			input:    "79",
			expected: []string{"pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := letterCombinations(tt.input)
			if !slices.Equal(result, tt.expected) {
				t.Errorf("letterCombinations(%q) = %v; want %v",
					tt.input, result, tt.expected)
			}
		})
	}
}
