package main

import (
	"strconv"
	"testing"
)

func TestIsPalindrome(t *testing.T) {
	testCases := []struct {
		input    int
		expected bool
	}{
		{121, true},
		{-121, false},
		{10, false},
	}

	for _, tc := range testCases {
		t.Run(strconv.Itoa(tc.input), func(t *testing.T) {
			result := isPalindrome(tc.input)
			result2 := isPalindrome2(tc.input)
			if result != tc.expected {
				t.Errorf("isPalindrome(%d) = %v; want %v", tc.input, result, tc.expected)
			}
			if result2 != tc.expected {
				t.Errorf("isPalindrome(%d) = %v; want %v", tc.input, result2, tc.expected)
			}
		})
	}
}
