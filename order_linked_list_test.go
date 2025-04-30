package main

import (
	"reflect"
	"testing"
)

// Helper function to create a linked list from a slice
func createLinkedList(values []int) *ListNode {
	if len(values) == 0 {
		return nil
	}

	head := &ListNode{Val: values[0]}
	current := head
	for i := 1; i < len(values); i++ {
		current.Next = &ListNode{Val: values[i]}
		current = current.Next
	}
	return head
}

// Helper function to convert a linked list to a slice for easier comparison
func linkedListToSlice(head *ListNode) []int {
	var result []int
	current := head
	for current != nil {
		result = append(result, current.Val)
		current = current.Next
	}
	return result
}

func TestMergeTwoLists(t *testing.T) {
	testCases := []struct {
		name     string
		list1    []int
		list2    []int
		expected []int
	}{
		{
			name:     "Both lists have values",
			list1:    []int{1, 2, 4},
			list2:    []int{1, 3, 4},
			expected: []int{1, 1, 2, 3, 4, 4},
		},
		{
			name:  "Both lists are empty",
			list1: []int{},
			list2: []int{},
		},
		{
			name:     "First list is empty",
			list1:    []int{},
			list2:    []int{0},
			expected: []int{0},
		},
		{
			name:     "Second list is empty",
			list1:    []int{1, 2, 3},
			list2:    []int{},
			expected: []int{1, 2, 3},
		},
		{
			name:     "Lists with different lengths",
			list1:    []int{1, 3, 5},
			list2:    []int{2, 4, 6, 8, 10},
			expected: []int{1, 2, 3, 4, 5, 6, 8, 10},
		},
		{
			name:     "First list with all smaller values",
			list1:    []int{1, 2, 3},
			list2:    []int{4, 5, 6},
			expected: []int{1, 2, 3, 4, 5, 6},
		},
		{
			name:     "Second list with all smaller values",
			list1:    []int{4, 5, 6},
			list2:    []int{1, 2, 3},
			expected: []int{1, 2, 3, 4, 5, 6},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			list1 := createLinkedList(tc.list1)
			list2 := createLinkedList(tc.list2)
			list21 := createLinkedList(tc.list1)
			list22 := createLinkedList(tc.list2)

			result := mergeTwoLists(list1, list2)
			result2 := mergeTwoLists2(list21, list22)
			resultSlice := linkedListToSlice(result)
			resultSlice2 := linkedListToSlice(result2)

			if !reflect.DeepEqual(resultSlice, tc.expected) {
				t.Errorf("mergeTwoLists() = %v, want %v", resultSlice, tc.expected)
			}
			if !reflect.DeepEqual(resultSlice2, tc.expected) {
				t.Errorf("mergeTwoLists() = %v, want %v", resultSlice2, tc.expected)
			}
		})
	}
}
