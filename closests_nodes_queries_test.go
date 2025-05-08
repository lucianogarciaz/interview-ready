package main

import (
	"reflect"
	"testing"
)

// Helper function to create a binary tree from a slice
// nil values in the slice represent null nodes
func createTree(values []interface{}) *TreeNode {
	if len(values) == 0 || values[0] == nil {
		return nil
	}

	root := &TreeNode{Val: values[0].(int)}
	queue := []*TreeNode{root}
	i := 1

	for len(queue) > 0 && i < len(values) {
		node := queue[0]
		queue = queue[1:]

		// Left child
		if i < len(values) && values[i] != nil {
			node.Left = &TreeNode{Val: values[i].(int)}
			queue = append(queue, node.Left)
		}
		i++

		// Right child
		if i < len(values) && values[i] != nil {
			node.Right = &TreeNode{Val: values[i].(int)}
			queue = append(queue, node.Right)
		}
		i++
	}

	return root
}

func TestClosestNodes(t *testing.T) {
	tests := []struct {
		name     string
		root     []interface{}
		queries  []int
		expected [][]int
	}{
		{
			name:     "Example 1",
			root:     []interface{}{6, 2, 13, 1, 4, 9, 15, nil, nil, nil, nil, nil, nil, 14},
			queries:  []int{2, 5, 16},
			expected: [][]int{{2, 2}, {4, 6}, {15, -1}},
		},
		{
			name:     "Empty Tree",
			root:     []interface{}{},
			queries:  []int{1, 2, 3},
			expected: [][]int{{-1, -1}, {-1, -1}, {-1, -1}},
		},
		{
			name:     "Single Node",
			root:     []interface{}{1},
			queries:  []int{0, 1, 2},
			expected: [][]int{{-1, 1}, {1, 1}, {1, -1}},
		},
		{
			name:     "Left Skewed Tree",
			root:     []interface{}{3, 2, nil, 1},
			queries:  []int{0, 1, 2, 3, 4},
			expected: [][]int{{-1, 1}, {1, 1}, {2, 2}, {3, 3}, {3, -1}},
		},
		{
			name:     "Perfect Tree",
			root:     []interface{}{4, 2, 6, 1, 3, 5, 7},
			queries:  []int{0, 1, 2, 3, 4, 5, 6, 7, 8},
			expected: [][]int{{-1, 1}, {1, 1}, {2, 2}, {3, 3}, {4, 4}, {5, 5}, {6, 6}, {7, 7}, {7, -1}},
		},
		{
			name:     "Duplicate Values",
			root:     []interface{}{2, 2, 2},
			queries:  []int{1, 2, 3},
			expected: [][]int{{-1, 2}, {2, 2}, {2, -1}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			root := createTree(tt.root)
			got := closestNodes(root, tt.queries)
			if !reflect.DeepEqual(got, tt.expected) {
				t.Errorf("closestNodes() for the queries %v = %v, want %v", tt.queries, got, tt.expected)
			}
		})
	}
}
