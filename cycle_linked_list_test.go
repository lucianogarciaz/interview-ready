package main

import (
	"testing"
)

func TestDetectCycle(t *testing.T) {
	tests := []struct {
		name      string
		list      []int
		cycleAt   int // index where the cycle starts, -1 if no cycle
		expectNil bool
	}{
		{
			name:      "no cycle",
			list:      []int{1, 2, 3, 4, 5},
			cycleAt:   -1,
			expectNil: true,
		},
		{
			name:      "cycle at beginning",
			list:      []int{1, 2, 3, 4, 5},
			cycleAt:   0,
			expectNil: false,
		},
		{
			name:      "cycle in middle",
			list:      []int{1, 2, 3, 4, 5},
			cycleAt:   2,
			expectNil: false,
		},
		{
			name:      "cycle at end",
			list:      []int{1, 2, 3, 4, 5},
			cycleAt:   4,
			expectNil: false,
		},
		{
			name:      "empty list",
			list:      []int{},
			cycleAt:   -1,
			expectNil: true,
		},
		{
			name:      "single node with self-loop",
			list:      []int{1},
			cycleAt:   0,
			expectNil: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Create the linked list
			head := createLinkedList(tt.list)

			// Create cycle if needed
			if tt.cycleAt >= 0 {
				// Find the node where cycle should start
				cycleStartNode := head
				for i := 0; i < tt.cycleAt && cycleStartNode != nil; i++ {
					cycleStartNode = cycleStartNode.Next
				}

				// Find the last node
				lastNode := head
				for lastNode != nil && lastNode.Next != nil {
					lastNode = lastNode.Next
				}

				// Create the cycle by connecting last node to cycle start node
				if lastNode != nil {
					lastNode.Next = cycleStartNode
				}

				// Detect the cycle
				result := detectCycle(head)

				if result != cycleStartNode {
					t.Errorf("Expected cycle starting at node %p, got %p", cycleStartNode, result)
				}
			} else {
				// No cycle case
				result := detectCycle(head)

				if result != nil {
					t.Errorf("Expected no cycle, but got cycle at node with value %v", result.Val)
				}
			}
		})
	}
}
