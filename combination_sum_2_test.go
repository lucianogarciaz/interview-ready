package main

import (
	"testing"
)

func TestCombinationSum2(t *testing.T) {
	tests := []struct {
		name       string
		candidates []int
		target     int
		expected   [][]int
	}{
		{
			name:       "empty array",
			candidates: []int{},
			target:     0,
			expected:   [][]int{},
		},
		{
			name:       "single element matching target",
			candidates: []int{1},
			target:     1,
			expected:   [][]int{{1}},
		},
		{
			name:       "single element not matching target",
			candidates: []int{2},
			target:     1,
			expected:   [][]int{},
		},
		{
			name:       "multiple elements with duplicates",
			candidates: []int{10, 1, 2, 7, 6, 1, 5},
			target:     8,
			expected: [][]int{
				{1, 1, 6},
				{1, 2, 5},
				{1, 7},
				{2, 6},
			},
		},
		{
			name:       "all elements sum to target",
			candidates: []int{2, 5, 2, 1, 2},
			target:     5,
			expected: [][]int{
				{1, 2, 2},
				{5},
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := combinationSum2(tt.candidates, tt.target)
			if !areSlicesEqual(result, tt.expected) {
				t.Errorf("combinationSum2(%v, %d) = %v; want %v",
					tt.candidates, tt.target, result, tt.expected)
			}
		})
	}
}
