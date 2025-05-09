package main

import (
	"fmt"
	"reflect"
	"testing"
)

func TestReverseString(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected string
	}{
		{
			name:     "Basic test",
			input:    "hello",
			expected: "olleh",
		},
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
			name:     "Palindrome",
			input:    "racecar",
			expected: "racecar",
		},
		{
			name:     "Special characters",
			input:    "Hello, World!",
			expected: "!dlroW ,olleH",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := reverseString((tt.input))
			if string(result) != string(tt.expected) {
				t.Errorf("reverseString() = %v, want %v", string(result), string(tt.expected))
			}
		})
	}
}

func TestIsPalindromeRecursive(t *testing.T) {
	testCases := []struct {
		input    string
		expected bool
	}{
		{"hello", false},
		{"racecar", true},
		{"raccecar", false},
		{"", true},      // Empty string is considered palindrome
		{"a", true},     // Single character is palindrome
		{"aa", true},    // Two same characters
		{"ab", false},   // Two different characters
		{"madam", true}, // Common palindrome word
		{"A man, a plan, a canal: Panama", false}, // Complex string with spaces and punctuation
		{"12321", true},                         // Numeric palindrome
		{"12345", false},                        // Non-palindrome numbers
		{"Was it a car or a cat I saw?", false}, // Complex string with spaces and punctuation
		{"Never odd or even", false},            // Complex string with spaces
	}

	for _, tc := range testCases {
		t.Run(tc.input, func(t *testing.T) {
			result := isPalindromeRecusively(tc.input)
			if result != tc.expected {
				t.Errorf("isPalindrome(%s) = %v; want %v", tc.input, result, tc.expected)
			}
		})
	}
}

func TestPrintNumbersRecursive(t *testing.T) {
	testCases := []struct {
		input    int
		expected []int
	}{
		{5, []int{5, 4, 3, 2, 1}},
		{0, []int{}},
		{1, []int{1}},
		{3, []int{3, 2, 1}},
	}

	for _, tc := range testCases {
		t.Run(fmt.Sprintf("n=%d", tc.input), func(t *testing.T) {
			result := printNumbersRecursive(tc.input)
			if !reflect.DeepEqual(result, tc.expected) {
				t.Errorf("printNumbersRecursive(%d) = %v, want %v", tc.input, result, tc.expected)
			}
		})
	}
}

func TestSumArray(t *testing.T) {
	testCases := []struct {
		input    []int
		expected int
	}{
		{[]int{1, 2, 3}, 6},
		{[]int{0}, 0},
		{[]int{-1, -2, -3}, -6},
		{[]int{}, 0},
		{[]int{5}, 5},
		{[]int{1, 1, 1, 1, 1}, 5},
		{[]int{-1, 1, -1, 1}, 0},
	}

	for _, tc := range testCases {
		t.Run(fmt.Sprintf("array=%v", tc.input), func(t *testing.T) {
			result := sumArrayRecurs(tc.input)
			if result != tc.expected {
				t.Errorf("sumArray(%v) = %d; want %d", tc.input, result, tc.expected)
			}
		})
	}
}
