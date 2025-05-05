package main

import "testing"

func TestCreateMinimalBST(t *testing.T) {
	testCases := []struct {
		name     string
		input    []int
		expected *TreeNode
	}{
		{
			name:     "Empty array",
			input:    []int{},
			expected: nil,
		},
		{
			name:  "Single element",
			input: []int{1},
			expected: &TreeNode{
				Val: 1,
			},
		},
		{
			name:  "Even number of elements",
			input: []int{1, 2, 3, 4, 5, 6, 7, 8},
			expected: &TreeNode{
				Val: 4,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 1,
					},
					Right: &TreeNode{
						Val: 3,
					},
				},
				Right: &TreeNode{
					Val: 6,
					Left: &TreeNode{
						Val: 5,
					},
					Right: &TreeNode{
						Val: 7,
						Right: &TreeNode{
							Val: 8,
						},
					},
				},
			},
		},
		{
			name:  "Odd number of elements",
			input: []int{1, 2, 3, 4, 5},
			expected: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val: 1,
					Right: &TreeNode{
						Val: 2,
					},
				},
				Right: &TreeNode{
					Val: 4,
					Right: &TreeNode{
						Val: 5,
					},
				},
			},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := createMinimalBST(tc.input)
			if !compareTrees(result, tc.expected) {
				t.Errorf("Expected tree %v, got %v", tc.expected, result)
			}
		})
	}
}

func compareTrees(a, b *TreeNode) bool {
	if a == nil && b == nil {
		return true
	}
	if a == nil || b == nil {
		return false
	}
	if a.Val != b.Val {
		return false
	}
	return compareTrees(a.Left, b.Left) && compareTrees(a.Right, b.Right)
}
