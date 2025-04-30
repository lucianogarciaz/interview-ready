package main

import (
	"reflect"
	"testing"
)

func TestInorderTraversal(t *testing.T) {
	testCases := []struct {
		name     string
		root     *TreeNode
		expected []int
	}{
		{
			name: "Example 1: [1,null,2,3]",
			root: &TreeNode{
				Val: 1,
				Right: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 3,
					},
				},
			},
			expected: []int{1, 3, 2},
		},
		{
			name: "Example 2: [1,2,3,4,5,null,8,null,null,6,7,9]",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 4,
					},
					Right: &TreeNode{
						Val: 5,
						Left: &TreeNode{
							Val: 6,
						},
						Right: &TreeNode{
							Val: 7,
						},
					},
				},
				Right: &TreeNode{
					Val: 3,
					Right: &TreeNode{
						Val: 8,
						Left: &TreeNode{
							Val: 9,
						},
					},
				},
			},
			expected: []int{4, 2, 6, 5, 7, 1, 3, 9, 8},
		},
		{
			name:     "Example 3: Empty tree",
			root:     nil,
			expected: []int{},
		},
		{
			name: "Example 4: Single node",
			root: &TreeNode{
				Val: 1,
			},
			expected: []int{1},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := inorderTraversal(tc.root)
			if !reflect.DeepEqual(result, tc.expected) {
				t.Errorf("inorderTraversal(%v) = %v; want %v", tc.root, result, tc.expected)
			}
		})
	}
}
