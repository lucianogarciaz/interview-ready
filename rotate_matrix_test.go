package main

import "testing"

func TestRotateMatrix(t *testing.T) {
	testCases := []struct {
		name     string
		input    [][]int
		expected [][]int
	}{
		{
			name: "1x1 matrix",
			input: [][]int{
				{1},
			},
			expected: [][]int{
				{1},
			},
		},
		{
			name: "2x2 matrix",
			input: [][]int{
				{1, 2},
				{3, 4},
			},
			expected: [][]int{
				{3, 1},
				{4, 2},
			},
		},
		{
			name: "3x3 matrix",
			input: [][]int{
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
			},
			expected: [][]int{
				{7, 4, 1},
				{8, 5, 2},
				{9, 6, 3},
			},
		},
		{
			name: "4x4 matrix",
			input: [][]int{
				{1, 2, 3, 4},
				{5, 6, 7, 8},
				{9, 10, 11, 12},
				{13, 14, 15, 16},
			},
			expected: [][]int{
				{13, 9, 5, 1},
				{14, 10, 6, 2},
				{15, 11, 7, 3},
				{16, 12, 8, 4},
			},
		},
		{
			name: "Empty matrix",
			input: [][]int{
				{},
			},
			expected: [][]int{
				{},
			},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := rotateMatrix(tc.input)

			// Check dimensions
			if len(result) != len(tc.expected) {
				t.Fatalf("rotateMatrix() returned matrix with wrong number of rows: got %d, want %d",
					len(result), len(tc.expected))
			}

			// Check each element
			for i := 0; i < len(tc.expected); i++ {
				if len(result[i]) != len(tc.expected[i]) {
					t.Fatalf("rotateMatrix() returned matrix with wrong number of columns in row %d: got %d, want %d",
						i, len(result[i]), len(tc.expected[i]))
				}

				for j := 0; j < len(tc.expected[i]); j++ {
					if result[i][j] != tc.expected[i][j] {
						t.Errorf("rotateMatrix() at position [%d][%d]: got %d, want %d",
							i, j, result[i][j], tc.expected[i][j])
					}
				}
			}
		})
	}
}
func TestRotateMatrixInPlace(t *testing.T) {
	testCases := []struct {
		name     string
		input    [][]int
		expected [][]int
	}{
		{
			name: "1x1 matrix",
			input: [][]int{
				{1},
			},
			expected: [][]int{
				{1},
			},
		},
		{
			name: "2x2 matrix",
			input: [][]int{
				{1, 2},
				{3, 4},
			},
			expected: [][]int{
				{3, 1},
				{4, 2},
			},
		},
		{
			name: "3x3 matrix",
			input: [][]int{
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
			},
			expected: [][]int{
				{7, 4, 1},
				{8, 5, 2},
				{9, 6, 3},
			},
		},
		{
			name: "4x4 matrix",
			input: [][]int{
				{1, 2, 3, 4},
				{5, 6, 7, 8},
				{9, 10, 11, 12},
				{13, 14, 15, 16},
			},
			expected: [][]int{
				{13, 9, 5, 1},
				{14, 10, 6, 2},
				{15, 11, 7, 3},
				{16, 12, 8, 4},
			},
		},
		{
			name: "Empty matrix",
			input: [][]int{
				{},
			},
			expected: [][]int{
				{},
			},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := rotateMatrixInPlace(tc.input)

			// Check dimensions
			if len(result) != len(tc.expected) {
				t.Fatalf("rotateMatrix() returned matrix with wrong number of rows: got %d, want %d",
					len(result), len(tc.expected))
			}

			// Check each element
			for i := 0; i < len(tc.expected); i++ {
				if len(result[i]) != len(tc.expected[i]) {
					t.Fatalf("rotateMatrix() returned matrix with wrong number of columns in row %d: got %d, want %d",
						i, len(result[i]), len(tc.expected[i]))
				}

				for j := 0; j < len(tc.expected[i]); j++ {
					if result[i][j] != tc.expected[i][j] {
						t.Errorf("rotateMatrix() at position [%d][%d]: got %d, want %d",
							i, j, result[i][j], tc.expected[i][j])
					}
				}
			}
		})
	}
}
