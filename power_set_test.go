package main

import (
	"fmt"
	"reflect"
	"testing"
)

func TestPowerSet(t *testing.T) {
	tests := []struct {
		name     string
		input    []int
		expected [][]int
	}{
		{
			name:     "empty array",
			input:    []int{},
			expected: [][]int{{}},
		},
		{
			name:     "single element",
			input:    []int{1},
			expected: [][]int{{}, {1}},
		},
		{
			name:     "two elements",
			input:    []int{1, 2},
			expected: [][]int{{}, {1}, {2}, {1, 2}},
		},
		{
			name:  "three elements",
			input: []int{1, 2, 3},
			expected: [][]int{
				{},
				{1},
				{2},
				{3},
				{1, 2},
				{1, 3},
				{2, 3},
				{1, 2, 3},
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := powerSet(tt.input)
			if !areSlicesEqual(result, tt.expected) {
				t.Errorf("powerSet(%v) = %v; want %v", tt.input, result, tt.expected)
			}
			result = powerSetBacktrack(tt.input)
			if !areSlicesEqual(result, tt.expected) {
				t.Errorf("powerSet(%v) = %v; want %v", tt.input, result, tt.expected)
			}
		})
	}
}

// Helper function to compare slices of slices
func areSlicesEqual(a, b [][]int) bool {
	if len(a) != len(b) {
		return false
	}

	// Create maps to count occurrences of each subset
	mapA := make(map[string]int)
	mapB := make(map[string]int)

	for _, subset := range a {
		key := fmt.Sprintf("%v", subset)
		mapA[key]++
	}

	for _, subset := range b {
		key := fmt.Sprintf("%v", subset)
		mapB[key]++
	}

	// Compare the maps
	return reflect.DeepEqual(mapA, mapB)
}

func TestPowerSetWithDuplicates(t *testing.T) {
	tests := []struct {
		name     string
		input    []int
		expected [][]int
	}{
		{
			name:  "empty array",
			input: []int{},
			expected: [][]int{
				{},
			},
		},
		{
			name:  "single element",
			input: []int{1},
			expected: [][]int{
				{},
				{1},
			},
		},
		{
			name:  "array with duplicates",
			input: []int{1, 2, 2},
			expected: [][]int{
				{},
				{1},
				{2},
				{1, 2},
				{2, 2},
				{1, 2, 2},
			},
		},
		{
			name:  "array with duplicates",
			input: []int{2, 1, 2},
			expected: [][]int{
				{},
				{1},
				{2},
				{1, 2},
				{2, 2},
				{1, 2, 2},
			},
		},
		{
			name:  "array with multiple duplicates",
			input: []int{1, 1, 2, 2},
			expected: [][]int{
				{},
				{1},
				{2},
				{1, 1},
				{1, 2},
				{2, 2},
				{1, 1, 2},
				{1, 2, 2},
				{1, 1, 2, 2},
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := powerSetWithDuplicates(tt.input)
			if !areSlicesEqual(result, tt.expected) {
				t.Errorf("powerSetWithDuplicates(%v) = %v; want %v", tt.input, result, tt.expected)
			}
		})
	}
}
