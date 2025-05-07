package main

import "testing"

func TestGetWinner(t *testing.T) {
	tests := []struct {
		name     string
		arr      []int
		k        int
		expected int
	}{
		{
			name:     "Example 1",
			arr:      []int{2, 1, 3, 5, 4, 6, 7},
			k:        2,
			expected: 5,
		},
		{
			name:     "Example 2",
			arr:      []int{3, 2, 1},
			k:        10,
			expected: 3,
		},
		{
			name:     "Single element array",
			arr:      []int{1},
			k:        1,
			expected: 1,
		},
		{
			name:     "K equals array length",
			arr:      []int{1, 2, 3, 4, 5},
			k:        5,
			expected: 5,
		},
		{
			name:     "K greater than array length",
			arr:      []int{1, 2, 3},
			k:        5,
			expected: 3,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := getWinner(tt.arr, tt.k)
			if result != tt.expected {
				t.Errorf("getWinner() = %v, want %v", result, tt.expected)
			}
		})
	}
}
