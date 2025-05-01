package main

import (
	"testing"
)

func TestFindIntersection(t *testing.T) {
	tests := []struct {
		name              string
		list1             []int
		list2             []int
		hasIntersection   bool
		intersectionIndex int // index in list1 where intersection occurs, -1 if no intersection
	}{
		{
			name:              "no intersection",
			list1:             []int{1, 2, 3, 4, 5},
			list2:             []int{6, 7, 8},
			hasIntersection:   false,
			intersectionIndex: -1,
		},
		{
			name:              "intersection at middle of list1",
			list1:             []int{1, 2, 3, 4, 5},
			list2:             []int{6, 7},
			hasIntersection:   true,
			intersectionIndex: 2, // intersect at node with value 3
		},
		{
			name:              "intersection at start of list1",
			list1:             []int{1, 2, 3},
			list2:             []int{},
			hasIntersection:   true,
			intersectionIndex: 0, // intersect at head of list1
		},
		{
			name:              "both lists empty",
			list1:             []int{},
			list2:             []int{},
			hasIntersection:   false,
			intersectionIndex: -1,
		},
		{
			name:              "one list empty",
			list1:             []int{1, 2, 3},
			list2:             []int{},
			hasIntersection:   false,
			intersectionIndex: -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Create the first list
			list1 := createLinkedList(tt.list1)

			// For test cases with no intersection, create separate lists
			if !tt.hasIntersection {
				list2 := createLinkedList(tt.list2)
				result := findIntersection(list1, list2)
				if result != nil {
					t.Errorf("Expected no intersection, but got intersection at node with value %v", result.Val)
				}
			} else {
				// For test cases with intersection, we need to create the second list
				// that shares nodes with the first list
				var intersectionNode *ListNode
				if tt.intersectionIndex >= 0 {
					// Find the node at the intersection index
					intersectionNode = list1
					for i := 0; i < tt.intersectionIndex && intersectionNode != nil; i++ {
						intersectionNode = intersectionNode.Next
					}
				}

				// Create the second list up to the intersection point
				var list2 *ListNode
				if len(tt.list2) > 0 {
					list2 = createLinkedList(tt.list2)
					// Find the last node of list2
					lastNode := list2
					for lastNode.Next != nil {
						lastNode = lastNode.Next
					}
					// Connect the last node to the intersection point
					lastNode.Next = intersectionNode
				} else {
					// If list2 is empty but has intersection, it means list2 starts at the intersection
					list2 = intersectionNode
				}

				result := findIntersection(list1, list2)
				if result != intersectionNode {
					t.Errorf("Expected intersection at node %p, got %p", intersectionNode, result)
				}
			}
		})
	}
}

func TestFindIntersection2(t *testing.T) {
	tests := []struct {
		name              string
		list1             []int
		list2             []int
		hasIntersection   bool
		intersectionIndex int // index in list1 where intersection occurs, -1 if no intersection
	}{
		{
			name:              "no intersection",
			list1:             []int{1, 2, 3, 4, 5},
			list2:             []int{6, 7, 8},
			hasIntersection:   false,
			intersectionIndex: -1,
		},
		{
			name:              "intersection at middle of list1",
			list1:             []int{1, 2, 3, 4, 5},
			list2:             []int{6, 7},
			hasIntersection:   true,
			intersectionIndex: 2, // intersect at node with value 3
		},
		{
			name:              "intersection at start of list1",
			list1:             []int{1, 2, 3},
			list2:             []int{},
			hasIntersection:   true,
			intersectionIndex: 0, // intersect at head of list1
		},
		{
			name:              "both lists empty",
			list1:             []int{},
			list2:             []int{},
			hasIntersection:   false,
			intersectionIndex: -1,
		},
		{
			name:              "one list empty",
			list1:             []int{1, 2, 3},
			list2:             []int{},
			hasIntersection:   false,
			intersectionIndex: -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Create the first list
			list1 := createLinkedList(tt.list1)

			// For test cases with no intersection, create separate lists
			if !tt.hasIntersection {
				list2 := createLinkedList(tt.list2)
				result := findIntersection2(list1, list2)
				if result != nil {
					t.Errorf("Expected no intersection, but got intersection at node with value %v", result.Val)
				}
			} else {
				// For test cases with intersection, we need to create the second list
				// that shares nodes with the first list
				var intersectionNode *ListNode
				if tt.intersectionIndex >= 0 {
					// Find the node at the intersection index
					intersectionNode = list1
					for i := 0; i < tt.intersectionIndex && intersectionNode != nil; i++ {
						intersectionNode = intersectionNode.Next
					}
				}

				// Create the second list up to the intersection point
				var list2 *ListNode
				if len(tt.list2) > 0 {
					list2 = createLinkedList(tt.list2)
					// Find the last node of list2
					lastNode := list2
					for lastNode.Next != nil {
						lastNode = lastNode.Next
					}
					// Connect the last node to the intersection point
					lastNode.Next = intersectionNode
				} else {
					// If list2 is empty but has intersection, it means list2 starts at the intersection
					list2 = intersectionNode
				}

				result := findIntersection2(list1, list2)
				if result != intersectionNode {
					t.Errorf("Expected intersection at node %p, got %p", intersectionNode, result)
				}
			}
		})
	}
}
