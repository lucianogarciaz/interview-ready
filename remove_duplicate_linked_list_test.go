package main

import (
	"reflect"
	"testing"
)

func TestDeleteDuplicatesLinkedList(t *testing.T) {
	testCases := []struct {
		name     string
		input    []int
		expected []int
	}{
		{
			name:     "Example 1: [1,1,2]",
			input:    []int{1, 1, 2},
			expected: []int{1, 2},
		},
		{
			name:     "Example 2: [1,1,2,3,3]",
			input:    []int{1, 1, 2, 3, 3},
			expected: []int{1, 2, 3},
		},
		{
			name:  "Empty list",
			input: []int{},
		},
		{
			name:     "Single element",
			input:    []int{5},
			expected: []int{5},
		},
		{
			name:     "All duplicates",
			input:    []int{1, 1, 1, 1, 1},
			expected: []int{1},
		},
		{
			name:     "No duplicates",
			input:    []int{1, 2, 3, 4, 5},
			expected: []int{1, 2, 3, 4, 5},
		},
		{
			name:     "Duplicates at beginning",
			input:    []int{1, 1, 1, 2, 3, 4},
			expected: []int{1, 2, 3, 4},
		},
		{
			name:     "Duplicates at end",
			input:    []int{1, 2, 3, 4, 4, 4},
			expected: []int{1, 2, 3, 4},
		},
		{
			name:     "Duplicates in middle",
			input:    []int{1, 2, 2, 2, 3, 4},
			expected: []int{1, 2, 3, 4},
		},
		{
			name:     "Multiple duplicates throughout",
			input:    []int{1, 1, 2, 2, 3, 3, 4, 4},
			expected: []int{1, 2, 3, 4},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// Create a linked list from the input slice
			head := createLinkedList(tc.input)

			// Call the function to test
			result := deleteDuplicatesLinkedList(head)

			// Convert the result back to a slice for comparison
			resultSlice := linkedListToSlice(result)

			// Check if the result matches the expected output
			if !reflect.DeepEqual(resultSlice, tc.expected) {
				t.Errorf("deleteDuplicatesLinkedList() = %v, want %v", resultSlice, tc.expected)
			}
		})
	}
}
