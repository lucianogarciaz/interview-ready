package main

import (
	"reflect"
	"testing"
)

func TestInorderTraversal(t *testing.T) {
	testCases := []struct {
		name     string
		root     *BinaryTreeNode
		expected []int
	}{
		{
			name: "Example 1: [1,null,2,3]",
			root: &BinaryTreeNode{
				Val: 1,
				Right: &BinaryTreeNode{
					Val: 2,
					Left: &BinaryTreeNode{
						Val: 3,
					},
				},
			},
			expected: []int{1, 3, 2},
		},
		{
			name: "Example 2: [1,2,3,4,5,null,8,null,null,6,7,9]",
			root: &BinaryTreeNode{
				Val: 1,
				Left: &BinaryTreeNode{
					Val: 2,
					Left: &BinaryTreeNode{
						Val: 4,
					},
					Right: &BinaryTreeNode{
						Val: 5,
						Left: &BinaryTreeNode{
							Val: 6,
						},
						Right: &BinaryTreeNode{
							Val: 7,
						},
					},
				},
				Right: &BinaryTreeNode{
					Val: 3,
					Right: &BinaryTreeNode{
						Val: 8,
						Left: &BinaryTreeNode{
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
			root: &BinaryTreeNode{
				Val: 1,
			},
			expected: []int{1},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := inorder(tc.root)
			// result := inorderTraversal(tc.root)
			if !reflect.DeepEqual(result, tc.expected) {
				t.Errorf("inorderTraversal(%v) = %v; want %v", tc.root, result, tc.expected)
			}
		})
	}
}
func TestPreOrderTraversal(t *testing.T) {
	testCases := []struct {
		name     string
		root     *BinaryTreeNode
		expected []int
	}{
		{
			name: "Example 1: Simple tree",
			root: &BinaryTreeNode{
				Val: 1,
				Left: &BinaryTreeNode{
					Val: 2,
				},
				Right: &BinaryTreeNode{
					Val: 3,
				},
			},
			expected: []int{1, 2, 3},
		},
		{
			name: "Example 2: Complex tree",
			root: &BinaryTreeNode{
				Val: 1,
				Left: &BinaryTreeNode{
					Val: 2,
					Left: &BinaryTreeNode{
						Val: 4,
					},
					Right: &BinaryTreeNode{
						Val: 5,
						Left: &BinaryTreeNode{
							Val: 6,
						},
						Right: &BinaryTreeNode{
							Val: 7,
						},
					},
				},
				Right: &BinaryTreeNode{
					Val: 3,
					Right: &BinaryTreeNode{
						Val: 8,
						Left: &BinaryTreeNode{
							Val: 9,
						},
					},
				},
			},
			expected: []int{1, 2, 4, 5, 6, 7, 3, 8, 9},
		},
		{
			name:     "Example 3: Empty tree",
			root:     nil,
			expected: []int{},
		},
		{
			name: "Example 4: Single node",
			root: &BinaryTreeNode{
				Val: 1,
			},
			expected: []int{1},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := preOrderTraversal(tc.root)
			if !reflect.DeepEqual(result, tc.expected) {
				t.Errorf("preOrderTraversal(%v) = %v; want %v", tc.root, result, tc.expected)
			}
		})
	}
}

func TestPostOrderTraversal(t *testing.T) {
	testCases := []struct {
		name     string
		root     *BinaryTreeNode
		expected []int
	}{
		{
			name: "Example 1: Simple tree",
			root: &BinaryTreeNode{
				Val: 1,
				Left: &BinaryTreeNode{
					Val: 2,
				},
				Right: &BinaryTreeNode{
					Val: 3,
				},
			},
			expected: []int{2, 3, 1},
		},
		{
			name: "Example 2: Complex tree",
			root: &BinaryTreeNode{
				Val: 1,
				Left: &BinaryTreeNode{
					Val: 2,
					Left: &BinaryTreeNode{
						Val: 4,
					},
					Right: &BinaryTreeNode{
						Val: 5,
						Left: &BinaryTreeNode{
							Val: 6,
						},
						Right: &BinaryTreeNode{
							Val: 7,
						},
					},
				},
				Right: &BinaryTreeNode{
					Val: 3,
					Right: &BinaryTreeNode{
						Val: 8,
						Left: &BinaryTreeNode{
							Val: 9,
						},
					},
				},
			},
			expected: []int{4, 6, 7, 5, 2, 9, 8, 3, 1},
		},
		{
			name:     "Example 3: Empty tree",
			root:     nil,
			expected: []int{},
		},
		{
			name: "Example 4: Single node",
			root: &BinaryTreeNode{
				Val: 1,
			},
			expected: []int{1},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := postOrderTraversal(tc.root)
			if !reflect.DeepEqual(result, tc.expected) {
				t.Errorf("postOrderTraversal(%v) = %v; want %v", tc.root, result, tc.expected)
			}
		})
	}
}
