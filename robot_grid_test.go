package main

import "testing"

func TestFindPath(t *testing.T) {
	testCases := []struct {
		name     string
		grid     [][]bool
		expected [][]int
	}{
		{
			name: "Simple 2x2 grid with no obstacles",
			grid: [][]bool{
				{true, true},
				{true, true},
			},
			expected: [][]int{
				{0, 0},
				{0, 1},
				{1, 1},
			},
		},
		{
			name: "2x2 grid with obstacle",
			grid: [][]bool{
				{true, true},
				{false, true},
			},
			expected: [][]int{
				{0, 0},
				{0, 1},
				{1, 1},
			},
		},
		{
			name: "3x3 grid with obstacles",
			grid: [][]bool{
				{true, true, true},
				{false, false, true},
				{true, true, true},
			},
			expected: [][]int{
				{0, 0},
				{0, 1},
				{0, 2},
				{1, 2},
				{2, 2},
			},
		},
		{
			name: "No valid path",
			grid: [][]bool{
				{true, true},
				{false, false},
			},
			expected: nil,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := findPath(tc.grid)
			if !comparePaths(result, tc.expected) {
				t.Errorf("findPath() = %v; want %v", result, tc.expected)
			}
		})
	}
}

func comparePaths(path1, path2 [][]int) bool {
	if len(path1) != len(path2) {
		return false
	}
	for i := range path1 {
		if len(path1[i]) != len(path2[i]) {
			return false
		}
		for j := range path1[i] {
			if path1[i][j] != path2[i][j] {
				return false
			}
		}
	}
	return true
}
