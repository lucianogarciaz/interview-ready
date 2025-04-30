package main

import (
	"testing"
)

func TestAddBinary(t *testing.T) {
	testCases := []struct {
		name     string
		a        string
		b        string
		expected string
	}{
		// {
		// 	name:     "Example 1",
		// 	a:        "11",
		// 	b:        "1",
		// 	expected: "100",
		// },
		{
			name:     "Example 2",
			a:        "1010",
			b:        "1011",
			expected: "10101",
		},
		{
			name:     "Both zeros",
			a:        "0",
			b:        "0",
			expected: "0",
		},
		{
			name:     "One zero",
			a:        "0",
			b:        "1",
			expected: "1",
		},
		{
			name:     "Equal length strings",
			a:        "1111",
			b:        "1111",
			expected: "11110",
		},
		{
			name:     "Different length strings",
			a:        "11111",
			b:        "1",
			expected: "100000",
		},
		{
			name:     "Long carry propagation",
			a:        "1111",
			b:        "1",
			expected: "10000",
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := addBinary(tc.a, tc.b)
			if result != tc.expected {
				t.Errorf("addBinary(%q, %q) = %q; want %q", tc.a, tc.b, result, tc.expected)
			}
		})
	}
}
