package main

import (
	"testing"
)

func TestIsSameTree(t *testing.T) {
	testCases := []struct {
		name     string
		p        *TreeNode
		q        *TreeNode
		expected bool
	}{
		{
			name: "Example 1: Same trees [1,2,3]",
			p: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
				},
				Right: &TreeNode{
					Val: 3,
				},
			},
			q: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
				},
				Right: &TreeNode{
					Val: 3,
				},
			},
			expected: true,
		},
		{
			name: "Example 2: Different trees [1,2] and [1,null,2]",
			p: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
				},
			},
			q: &TreeNode{
				Val: 1,
				Right: &TreeNode{
					Val: 2,
				},
			},
			expected: false,
		},
		{
			name: "Example 3: Different trees [1,2,1] and [1,1,2]",
			p: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
				},
				Right: &TreeNode{
					Val: 1,
				},
			},
			q: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 1,
				},
				Right: &TreeNode{
					Val: 2,
				},
			},
			expected: false,
		},
		{
			name:     "Both trees are nil",
			p:        nil,
			q:        nil,
			expected: true,
		},
		{
			name: "One tree is nil",
			p: &TreeNode{
				Val: 1,
			},
			q:        nil,
			expected: false,
		},
		{
			name: "Different values at root",
			p: &TreeNode{
				Val: 1,
			},
			q: &TreeNode{
				Val: 2,
			},
			expected: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := isSameTree(tc.p, tc.q)
			if result != tc.expected {
				t.Errorf("isSameTree(%v, %v) = %v; want %v", tc.p, tc.q, result, tc.expected)
			}
		})
	}
}
