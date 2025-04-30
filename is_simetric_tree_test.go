package main

import (
	"testing"
)

func TestIsSymmetricTree(t *testing.T) {
	testCases := []struct {
		name     string
		root     *TreeNode
		expected bool
	}{
		{
			name: "Example 1: Symmetric tree [1,2,2,3,4,4,3]",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 3,
					},
					Right: &TreeNode{
						Val: 4,
					},
				},
				Right: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 4,
					},
					Right: &TreeNode{
						Val: 3,
					},
				},
			},
			expected: true,
		},
		{
			name: "Example 2: Non-symmetric tree [1,2,2,null,3,null,3]",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Right: &TreeNode{
						Val: 3,
					},
				},
				Right: &TreeNode{
					Val: 2,
					Right: &TreeNode{
						Val: 3,
					},
				},
			},
			expected: false,
		},
		{
			name:     "Empty tree is symmetric",
			root:     nil,
			expected: true,
		},
		{
			name: "Single node tree is symmetric",
			root: &TreeNode{
				Val: 1,
			},
			expected: true,
		},
		{
			name: "Different values at same position",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
				},
				Right: &TreeNode{
					Val: 3,
				},
			},
			expected: false,
		},
		{
			name: "Deeper symmetric tree",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 3,
					},
					Right: &TreeNode{
						Val: 4,
					},
				},
				Right: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 4,
					},
					Right: &TreeNode{
						Val: 3,
					},
				},
			},
			expected: true,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := isSymmetric(tc.root)
			if result != tc.expected {
				t.Errorf("isSymmetric(%v) = %v; want %v", tc.root, result, tc.expected)
			}
		})
	}
}
