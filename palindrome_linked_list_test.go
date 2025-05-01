package main

import (
	"testing"
)

func TestIsPalindromeLinkedList(t *testing.T) {
	tests := []struct {
		name     string
		input    []int
		expected bool
	}{
		{
			name:     "empty list",
			input:    []int{},
			expected: true,
		},
		{
			name:     "single element",
			input:    []int{1},
			expected: true,
		},
		{
			name:     "even length palindrome",
			input:    []int{1, 2, 2, 1},
			expected: true,
		},
		{
			name:     "odd length palindrome",
			input:    []int{1, 2, 3, 2, 1},
			expected: true,
		},
		{
			name:     "not a palindrome",
			input:    []int{1, 2, 3, 4},
			expected: false,
		},
		{
			name:     "long palindrome",
			input:    []int{1, 2, 3, 4, 5, 4, 3, 2, 1},
			expected: true,
		},
		{
			name:     "almost palindrome",
			input:    []int{1, 2, 3, 4, 5, 4, 3, 2, 2},
			expected: false,
		},
		{
			name:     "almost palindrome 2",
			input:    []int{2, 2, 3, 4, 5, 4, 3, 2, 2, 2},
			expected: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			head := createLinkedList(tt.input)
			result := isPalindromeLinkedList(head)
			if result != tt.expected {
				t.Errorf("IsPalindrome() = %v, want %v", result, tt.expected)
			}
		})
	}
}
