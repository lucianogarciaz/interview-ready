package main

import "testing"

func TestIsBalanced(t *testing.T) {
	// Test case 1: Empty tree
	t.Run("empty tree", func(t *testing.T) {
		result := isBalanced(nil)
		if !result {
			t.Error("Expected empty tree to be balanced")
		}
	})

	// Test case 2: Single node tree
	t.Run("single node", func(t *testing.T) {
		root := &TreeNode{Val: 1}
		result := isBalanced(root)
		if !result {
			t.Error("Expected single node tree to be balanced")
		}
	})

	// Test case 3: Balanced tree
	t.Run("balanced tree", func(t *testing.T) {
		// Create a balanced tree:
		//       1
		//      / \
		//     2   3
		//    / \ / \
		//   4  5 6  7
		root := &TreeNode{Val: 1}
		root.Left = &TreeNode{Val: 2}
		root.Right = &TreeNode{Val: 3}
		root.Left.Left = &TreeNode{Val: 4}
		root.Left.Right = &TreeNode{Val: 5}
		root.Right.Left = &TreeNode{Val: 6}
		root.Right.Right = &TreeNode{Val: 7}

		result := isBalanced(root)
		if !result {
			t.Error("Expected balanced tree to return true")
		}
	})

	// Test case 4: Unbalanced tree
	t.Run("unbalanced tree", func(t *testing.T) {
		// Create an unbalanced tree:
		//     1
		//    / \
		//   2   3
		//  /
		// 4
		root := &TreeNode{Val: 1}
		root.Left = &TreeNode{Val: 2}
		root.Right = &TreeNode{Val: 3}
		root.Left.Left = &TreeNode{Val: 4}

		result := isBalanced(root)
		if result {
			t.Error("Expected unbalanced tree to return false")
		}
	})

	// Test case 5: Deeply unbalanced tree
	t.Run("deeply unbalanced tree", func(t *testing.T) {
		// Create a deeply unbalanced tree:
		//     1
		//    /
		//   2
		//  /
		// 3
		root := &TreeNode{Val: 1}
		root.Left = &TreeNode{Val: 2}
		root.Left.Left = &TreeNode{Val: 3}

		result := isBalanced(root)
		if result {
			t.Error("Expected deeply unbalanced tree to return false")
		}
	})
}

func TestIsBalanced2(t *testing.T) {
	// Test case 1: Empty tree
	t.Run("empty tree", func(t *testing.T) {
		result := checkBalanced(nil)
		if !result {
			t.Error("Expected empty tree to be balanced")
		}
	})

	// Test case 2: Single node tree
	t.Run("single node", func(t *testing.T) {
		root := &TreeNode{Val: 1}
		result := checkBalanced(root)
		if !result {
			t.Error("Expected single node tree to be balanced")
		}
	})

	// Test case 3: Balanced tree
	t.Run("balanced tree", func(t *testing.T) {
		// Create a balanced tree:
		//       1
		//      / \
		//     2   3
		//    / \ / \
		//   4  5 6  7
		root := &TreeNode{Val: 1}
		root.Left = &TreeNode{Val: 2}
		root.Right = &TreeNode{Val: 3}
		root.Left.Left = &TreeNode{Val: 4}
		root.Left.Right = &TreeNode{Val: 5}
		root.Right.Left = &TreeNode{Val: 6}
		root.Right.Right = &TreeNode{Val: 7}

		result := checkBalanced(root)
		if !result {
			t.Error("Expected balanced tree to return true")
		}
	})

	// Test case 4: Unbalanced tree
	t.Run("unbalanced tree", func(t *testing.T) {
		// Create an unbalanced tree:
		//     1
		//    / \
		//   2   3
		//  /
		// 4
		root := &TreeNode{Val: 1}
		root.Left = &TreeNode{Val: 2}
		root.Right = &TreeNode{Val: 3}
		root.Left.Left = &TreeNode{Val: 4}

		result := checkBalanced(root)
		if result {
			t.Error("Expected unbalanced tree to return false")
		}
	})

	// Test case 5: Deeply unbalanced tree
	t.Run("deeply unbalanced tree", func(t *testing.T) {
		// Create a deeply unbalanced tree:
		//     1
		//    /
		//   2
		//  /
		// 3
		root := &TreeNode{Val: 1}
		root.Left = &TreeNode{Val: 2}
		root.Left.Left = &TreeNode{Val: 3}

		result := checkBalanced(root)
		if result {
			t.Error("Expected deeply unbalanced tree to return false")
		}
	})
}
