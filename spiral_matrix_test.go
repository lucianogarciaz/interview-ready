package main

import (
	"reflect"
	"testing"
)

func TestGenerateMatrix(t *testing.T) {
	tests := []struct {
		name     string
		input    int
		expected [][]int
	}{
		{
			name:  "2x2 matrix",
			input: 2,
			expected: [][]int{
				{1, 2},
				{4, 3},
			},
		},
		{
			name:  "3x3 matrix",
			input: 3,
			expected: [][]int{
				{1, 2, 3},
				{8, 9, 4},
				{7, 6, 5},
			},
		},
		{
			name:  "4x4 matrix",
			input: 4,
			expected: [][]int{
				{1, 2, 3, 4},
				{12, 13, 14, 5},
				{11, 16, 15, 6},
				{10, 9, 8, 7},
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := generateMatrix(tt.input)
			if !reflect.DeepEqual(result, tt.expected) {
				t.Errorf("generateMatrix(%d) = %v, want %v", tt.input, result, tt.expected)
			}
		})
	}
}
