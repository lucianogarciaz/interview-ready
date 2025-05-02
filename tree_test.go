package main

import (
	"testing"
)

func TestDfs(t *testing.T) {
	// Test cases for DFS
	testCases := []struct {
		name string
		tree *TreeNode
	}{
		{
			name: "Empty tree",
			tree: nil,
		},
		{
			name: "Single node tree",
			tree: &TreeNode{Val: 1},
		},
		{
			name: "Complete binary tree",
			tree: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 4,
					},
					Right: &TreeNode{
						Val: 5,
					},
				},
				Right: &TreeNode{
					Val: 3,
					Left: &TreeNode{
						Val: 6,
					},
					Right: &TreeNode{
						Val: 7,
					},
				},
			},
		},
		{
			name: "Unbalanced tree",
			tree: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 4,
						Left: &TreeNode{
							Val: 8,
						},
					},
				},
				Right: &TreeNode{
					Val: 3,
				},
			},
		},
	}

	// Run tests - since Dfs doesn't return anything, we're just testing that it doesn't panic
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// This test just verifies that Dfs doesn't panic
			Dfs(tc.tree)
		})
	}
}

func TestBfs(t *testing.T) {
	// Test cases for BFS
	testCases := []struct {
		name string
		tree *TreeNode
	}{
		{
			name: "Empty tree",
			tree: nil,
		},
		{
			name: "Single node tree",
			tree: &TreeNode{Val: 1},
		},
		{
			name: "Complete binary tree",
			tree: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 4,
					},
					Right: &TreeNode{
						Val: 5,
					},
				},
				Right: &TreeNode{
					Val: 3,
					Left: &TreeNode{
						Val: 6,
					},
					Right: &TreeNode{
						Val: 7,
					},
				},
			},
		},
		{
			name: "Unbalanced tree",
			tree: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 4,
						Left: &TreeNode{
							Val: 8,
						},
					},
				},
				Right: &TreeNode{
					Val: 3,
				},
			},
		},
	}

	// Run tests - since Bfs doesn't return anything, we're just testing that it doesn't panic
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// This test just verifies that Bfs doesn't panic
			Bfs(tc.tree)
		})
	}
}
