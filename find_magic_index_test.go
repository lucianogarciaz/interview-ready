package main

import "testing"

func TestFindMagicIndex(t *testing.T) {
	tests := []struct {
		name     string
		input    []int
		expected int
	}{
		{
			name:     "empty array",
			input:    []int{},
			expected: -1,
		},
		{
			name:     "no magic index",
			input:    []int{1, 2, 3, 4, 5},
			expected: -1,
		},
		{
			name:     "magic index at start",
			input:    []int{0, 2, 3, 4, 5},
			expected: 0,
		},
		{
			name:     "magic index at end",
			input:    []int{-1, 0, 1, 2, 4},
			expected: 4,
		},
		{
			name:     "magic index in middle",
			input:    []int{-1, 0, 2, 4, 5},
			expected: 2,
		},
		{
			name:     "multiple magic indices",
			input:    []int{-1, 1, 2, 3, 4},
			expected: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := findMagicIndex(tt.input)
			if result != tt.expected {
				t.Errorf("findMagicIndex(%v) = %d; want %d", tt.input, result, tt.expected)
			}
		})
	}
}
