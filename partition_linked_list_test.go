package main

import (
	"testing"
)

func TestPartitionLinkedList(t *testing.T) {
	tests := []struct {
		name      string
		list      []int
		partition int
		expected  []int
	}{
		{
			name:      "Empty list",
			list:      []int{},
			partition: 5,
			expected:  []int{},
		},
		{
			name:      "Single element list",
			list:      []int{5},
			partition: 5,
			expected:  []int{5},
		},
		{
			name:      "Example from problem statement",
			list:      []int{3, 5, 8, 5, 10, 2, 1},
			partition: 5,
			expected:  []int{3, 2, 1, 5, 8, 5, 10}, // All elements < 5 come before elements >= 5
		},
		{
			name:      "All elements less than partition",
			list:      []int{1, 2, 3, 4},
			partition: 5,
			expected:  []int{1, 2, 3, 4},
		},
		{
			name:      "All elements greater than or equal to partition",
			list:      []int{5, 6, 7, 8},
			partition: 5,
			expected:  []int{5, 6, 7, 8},
		},
		{
			name:      "Partition value not in list",
			list:      []int{3, 8, 10, 2, 1},
			partition: 5,
			expected:  []int{3, 2, 1, 8, 10},
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
			result := partitionLinkedList(head, tt.partition)

			// Convert result linked list back to array for comparison
			var resultArray []int
			for result != nil {
				resultArray = append(resultArray, result.Val)
				result = result.Next
			}

			// Check if result matches expected
			if len(resultArray) != len(tt.expected) {
				t.Errorf("partitionLinkedList() returned list of length %v, want %v", len(resultArray), len(tt.expected))
				return
			}

			// Compare each element
			for i := 0; i < len(resultArray); i++ {
				if resultArray[i] != tt.expected[i] {
					t.Errorf("partitionLinkedList() = %v, want %v", resultArray, tt.expected)
					return
				}
			}
		})
	}
}
