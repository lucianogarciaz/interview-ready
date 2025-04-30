package main

import (
	"testing"
)

func TestSumLists(t *testing.T) {
	tests := []struct {
		name     string
		list1    []int
		list2    []int
		expected []int
	}{
		{
			name:     "Example case: 617 + 295 = 912",
			list1:    []int{7, 1, 6},
			list2:    []int{5, 9, 2},
			expected: []int{2, 1, 9},
		},
		{
			name:     "Different length lists: 65 + 954 = 1019",
			list1:    []int{5, 6},
			list2:    []int{4, 5, 9},
			expected: []int{9, 1, 0, 1},
		},
		{
			name:     "Empty first list",
			list1:    []int{},
			list2:    []int{5, 9, 2},
			expected: []int{5, 9, 2},
		},
		{
			name:     "Empty second list",
			list1:    []int{7, 1, 6},
			list2:    []int{},
			expected: []int{7, 1, 6},
		},
		{
			name:     "Both empty lists",
			list1:    []int{},
			list2:    []int{},
			expected: []int{},
		},
		{
			name:     "With carry: 999 + 1 = 1000",
			list1:    []int{9, 9, 9},
			list2:    []int{1},
			expected: []int{0, 0, 0, 1},
		},
		{
			name:     "Single digit lists: 5 + 7 = 12",
			list1:    []int{5},
			list2:    []int{7},
			expected: []int{2, 1},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Create linked lists from the input arrays
			var list1, list2 *ListNode

			if len(tt.list1) > 0 {
				list1 = &ListNode{Val: tt.list1[0]}
				current := list1
				for i := 1; i < len(tt.list1); i++ {
					current.Next = &ListNode{Val: tt.list1[i]}
					current = current.Next
				}
			}

			if len(tt.list2) > 0 {
				list2 = &ListNode{Val: tt.list2[0]}
				current := list2
				for i := 1; i < len(tt.list2); i++ {
					current.Next = &ListNode{Val: tt.list2[i]}
					current = current.Next
				}
			}

			// Call the function being tested
			result := sumLists(list1, list2)

			// Convert expected array to linked list for comparison
			var expected *ListNode
			if len(tt.expected) > 0 {
				expected = &ListNode{Val: tt.expected[0]}
				current := expected
				for i := 1; i < len(tt.expected); i++ {
					current.Next = &ListNode{Val: tt.expected[i]}
					current = current.Next
				}
			}

			// Compare result with expected
			resultNode := result
			expectedNode := expected

			for resultNode != nil && expectedNode != nil {
				if resultNode.Val != expectedNode.Val {
					t.Errorf("sumLists() = %d at position, want %d", resultNode.Val, expectedNode.Val)
					return
				}
				resultNode = resultNode.Next
				expectedNode = expectedNode.Next
			}

			// Check if one list is longer than the other
			if resultNode != nil {
				t.Errorf("sumLists() result is longer than expected")
			}
			if expectedNode != nil {
				t.Errorf("sumLists() result is shorter than expected")
			}
		})
	}
}

func TestSumListForeward(t *testing.T) {
	tests := []struct {
		name     string
		list1    []int
		list2    []int
		expected []int
	}{
		{
			name:     "Example case: 617 + 295 = 912",
			list1:    []int{6, 1, 7},
			list2:    []int{2, 9, 5},
			expected: []int{9, 1, 2},
		},
		{
			name:     "Empty lists",
			list1:    []int{},
			list2:    []int{},
			expected: []int{},
		},
		{
			name:     "One empty list",
			list1:    []int{4, 2, 1},
			list2:    []int{},
			expected: []int{4, 2, 1},
		},
		{
			name:     "Different length lists: 123 + 45 = 168",
			list1:    []int{1, 2, 3},
			list2:    []int{4, 5},
			expected: []int{1, 6, 8},
		},
		{
			name:     "With carry: 999 + 1 = 1000",
			list1:    []int{9, 9, 9},
			list2:    []int{1},
			expected: []int{1, 0, 0, 0},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Convert arrays to linked lists
			var list1 *ListNode
			var list2 *ListNode

			// Create first linked list
			if len(tt.list1) > 0 {
				list1 = &ListNode{Val: tt.list1[0]}
				current := list1
				for i := 1; i < len(tt.list1); i++ {
					current.Next = &ListNode{Val: tt.list1[i]}
					current = current.Next
				}
			}

			// Create second linked list
			if len(tt.list2) > 0 {
				list2 = &ListNode{Val: tt.list2[0]}
				current := list2
				for i := 1; i < len(tt.list2); i++ {
					current.Next = &ListNode{Val: tt.list2[i]}
					current = current.Next
				}
			}

			// Call the function being tested
			result := sumListForeward(list1, list2)

			// Convert expected array to linked list for comparison
			var expected *ListNode
			if len(tt.expected) > 0 {
				expected = &ListNode{Val: tt.expected[0]}
				current := expected
				for i := 1; i < len(tt.expected); i++ {
					current.Next = &ListNode{Val: tt.expected[i]}
					current = current.Next
				}
			}

			// Compare result with expected
			resultNode := result
			expectedNode := expected

			for resultNode != nil && expectedNode != nil {
				if resultNode.Val != expectedNode.Val {
					t.Errorf("sumListForeward() = %d at position, want %d", resultNode.Val, expectedNode.Val)
					return
				}
				resultNode = resultNode.Next
				expectedNode = expectedNode.Next
			}

			// Check if one list is longer than the other
			if resultNode != nil {
				t.Errorf("sumListForeward() result is longer than expected")
			}
			if expectedNode != nil {
				t.Errorf("sumListForeward() result is shorter than expected")
			}
		})
	}
}
