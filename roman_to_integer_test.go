package main

import (
	"testing"
)

func TestRomanToInt(t *testing.T) {
	testCases := []struct {
		input    string
		expected int
	}{
		{"III", 3},
		{"LVIII", 58},
		{"MCMXCIV", 1994},
		{"I", 1},
		{"IV", 4},
		{"IX", 9},
		{"XL", 40},
		{"XC", 90},
		{"CD", 400},
		{"CM", 900},
		{"MMMDCCCLXXXVIII", 3888},
	}

	for _, tc := range testCases {
		t.Run(tc.input, func(t *testing.T) {
			result := romanToInt(tc.input)
			result2 := romanToInt2(tc.input)
			if result != tc.expected {
				t.Errorf("romanToInt(%s) = %d; want %d", tc.input, result, tc.expected)
			}
			if result2 != tc.expected {
				t.Errorf("romanToInt(%s) = %d; want %d", tc.input, result2, tc.expected)
			}
		})
	}
}
