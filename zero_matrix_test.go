package main

import "testing"

func TestZeroMatrix(t *testing.T) {
	testCases := []struct {
		name     string
		input    [][]int
		expected [][]int
	}{
		{
			name: "1x1 matrix with zero",
			input: [][]int{
				{0},
			},
			expected: [][]int{
				{0},
			},
		},
		{
			name: "1x1 matrix without zero",
			input: [][]int{
				{1},
			},
			expected: [][]int{
				{1},
			},
		},
		{
			name: "2x2 matrix with one zero",
			input: [][]int{
				{1, 2},
				{3, 0},
			},
			expected: [][]int{
				{1, 0},
				{0, 0},
			},
		},
		{
			name: "3x3 matrix with one zero",
			input: [][]int{
				{1, 2, 3},
				{4, 0, 6},
				{7, 8, 9},
			},
			expected: [][]int{
				{1, 0, 3},
				{0, 0, 0},
				{7, 0, 9},
			},
		},
		{
			name: "3x3 matrix with multiple zeros",
			input: [][]int{
				{1, 0, 3},
				{4, 5, 6},
				{0, 8, 9},
			},
			expected: [][]int{
				{0, 0, 0},
				{0, 0, 6},
				{0, 0, 0},
			},
		},
		{
			name: "3x4 matrix (non-square)",
			input: [][]int{
				{1, 2, 3, 4},
				{5, 0, 7, 8},
				{9, 10, 11, 0},
			},
			expected: [][]int{
				{1, 0, 3, 0},
				{0, 0, 0, 0},
				{0, 0, 0, 0},
			},
		},
		{
			name:     "Empty matrix",
			input:    [][]int{},
			expected: [][]int{},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// Create a copy of the input to avoid modifying the original
			inputCopy := make([][]int, len(tc.input))
			for i, row := range tc.input {
				inputCopy[i] = make([]int, len(row))
				copy(inputCopy[i], row)
			}

			result := zeroMatrix(inputCopy)

			// Check if the result matches the expected output
			if !matrixEqual(result, tc.expected) {
				t.Errorf("Expected %v, got %v", tc.expected, result)
			}
		})
	}
}

// Helper function to compare two matrices
func matrixEqual(a, b [][]int) bool {
	if len(a) != len(b) {
		return false
	}

	for i := range a {
		if len(a[i]) != len(b[i]) {
			return false
		}
		for j := range a[i] {
			if a[i][j] != b[i][j] {
				return false
			}
		}
	}

	return true
}
