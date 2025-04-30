package main

import (
	"testing"
)

func TestUrlify(t *testing.T) {
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
			name:     "No spaces",
			input:    "HelloWorld",
			expected: "HelloWorld",
		},
		{
			name:     "Single space",
			input:    "Hello World",
			expected: "Hello%20World",
		},
		{
			name:     "Multiple spaces",
			input:    "Mr John Smith",
			expected: "Mr%20John%20Smith",
		},
		{
			name:     "Leading space",
			input:    " HelloWorld",
			expected: "%20HelloWorld",
		},
		{
			name:     "Trailing space",
			input:    "HelloWorld ",
			expected: "HelloWorld%20",
		},
		{
			name:     "Multiple consecutive spaces",
			input:    "Hello  World",
			expected: "Hello%20%20World",
		},
		{
			name:     "Only spaces",
			input:    "   ",
			expected: "%20%20%20",
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := Urlify(tc.input)
			if result != tc.expected {
				t.Errorf("Urlify(%q) = %q; want %q", tc.input, result, tc.expected)
			}
		})
	}
}
