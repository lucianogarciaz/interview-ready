package main

import (
	"testing"
)

func TestLengthOfLastWord(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		expected int
	}{
		{
			name:     "Simple two words",
			input:    "Hello World",
			expected: 5,
		},
		{
			name:     "Multiple spaces between words",
			input:    "   fly me   to   the moon  ",
			expected: 4,
		},
		{
			name:     "No trailing spaces",
			input:    "luffy is still joyboy",
			expected: 6,
		},
		{
			name:     "Single word",
			input:    "Hello",
			expected: 5,
		},
		{
			name:     "Single word with spaces",
			input:    "   Hello   ",
			expected: 5,
		},
		{
			name:     "Minimum length input",
			input:    "a",
			expected: 1,
		},
		{
			name:     "Words with numbers",
			input:    "abc123 def456",
			expected: 6,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := lengthOfLastWord(tc.input)
			result2 := lengthOfLastWord2(tc.input)
			if result != tc.expected {
				t.Errorf("lengthOfLastWord(%q) = %d; want %d", tc.input, result, tc.expected)
			}
			if result2 != tc.expected {
				t.Errorf("lengthOfLastWord(%q) = %d; want %d", tc.input, result2, tc.expected)
			}
		})
	}
}
