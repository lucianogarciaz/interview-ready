package main

import (
	"testing"
)

func TestKthToLastNode(t *testing.T) {
	tests := []struct {
		name     string
		list     []int
		k        int
		expected *ListNode
	}{
		{
			name:     "Empty list",
			list:     []int{},
			k:        1,
			expected: nil,
		},
		{
			name:     "Single element list, k=1",
			list:     []int{5},
			k:        1,
			expected: &ListNode{Val: 5},
		},
		{
			name:     "List with multiple elements, k=1 (last element)",
			list:     []int{1, 2, 3, 4, 5},
			k:        1,
			expected: &ListNode{Val: 5},
		},
		{
			name:     "List with multiple elements, k=3",
			list:     []int{1, 2, 3, 4, 5},
			k:        2,
			expected: &ListNode{Val: 4},
		},
		{
			name:     "k greater than list length",
			list:     []int{1, 2, 3},
			k:        4,
			expected: nil,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Create linked list from the input array
			var head *ListNode
			if len(tt.list) > 0 {
				head = &ListNode{Val: tt.list[0]}
				current := head
				for i := 1; i < len(tt.list); i++ {
					current.Next = &ListNode{Val: tt.list[i]}
					current = current.Next
				}
			}

			// Call the function being tested
			result := kthToLastNode(head, tt.k)

			// Check if result is nil when expected is nil
			if tt.expected == nil {
				if result != nil {
					t.Errorf("kthToLastNode() = %v, want nil", result.Val)
				}
				return
			}

			// Check if result is nil when it shouldn't be
			if result == nil {
				t.Errorf("kthToLastNode() = nil, want %v", tt.expected.Val)
				return
			}

			// Check the value
			if result.Val != tt.expected.Val {
				t.Errorf("kthToLastNode() = %v, want %v", result.Val, tt.expected.Val)
			}
		})
	}
}
