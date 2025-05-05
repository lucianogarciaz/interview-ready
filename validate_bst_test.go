package main

import "testing"

func TestValidateBST(t *testing.T) {
	// Test case 1: Empty tree
	t.Run("empty tree", func(t *testing.T) {
		result := validateBST(nil)
		if !result {
			t.Error("Expected empty tree to be a valid BST")
		}
	})

	// Test case 2: Single node tree
	t.Run("single node", func(t *testing.T) {
		root := &TreeNode{Val: 1}
		result := validateBST(root)
		if !result {
			t.Error("Expected single node tree to be a valid BST")
		}
	})

	// Test case 3: Valid BST
	t.Run("valid BST", func(t *testing.T) {
		// Create a valid BST:
		//       5
		//      / \
		//     3   7
		//    / \ / \
		//   2  4 6  8
		root := &TreeNode{Val: 5}
		root.Left = &TreeNode{Val: 3}
		root.Right = &TreeNode{Val: 7}
		root.Left.Left = &TreeNode{Val: 2}
		root.Left.Right = &TreeNode{Val: 4}
		root.Right.Left = &TreeNode{Val: 6}
		root.Right.Right = &TreeNode{Val: 8}

		result := validateBST(root)
		if !result {
			t.Error("Expected valid BST to return true")
		}
	})

	// Test case 4: Invalid BST (right child smaller than root)
	t.Run("invalid BST - right child smaller", func(t *testing.T) {
		// Create an invalid BST:
		//     5
		//    / \
		//   3   4
		root := &TreeNode{Val: 5}
		root.Left = &TreeNode{Val: 3}
		root.Right = &TreeNode{Val: 4}

		result := validateBST(root)
		if result {
			t.Error("Expected invalid BST to return false")
		}
	})

	// Test case 5: Invalid BST (left child larger than root)
	t.Run("invalid BST - left child larger", func(t *testing.T) {
		// Create an invalid BST:
		//     5
		//    / \
		//   6   7
		root := &TreeNode{Val: 5}
		root.Left = &TreeNode{Val: 6}
		root.Right = &TreeNode{Val: 7}

		result := validateBST(root)
		if result {
			t.Error("Expected invalid BST to return false")
		}
	})

	// Test case 6: Invalid BST (grandchild violation)
	t.Run("invalid BST - grandchild violation", func(t *testing.T) {
		// Create an invalid BST:
		//       5
		//      / \
		//     3   7
		//    / \
		//   2   6
		root := &TreeNode{Val: 5}
		root.Left = &TreeNode{Val: 3}
		root.Right = &TreeNode{Val: 7}
		root.Left.Left = &TreeNode{Val: 2}
		root.Left.Right = &TreeNode{Val: 6}

		result := validateBST(root)
		if result {
			t.Error("Expected invalid BST to return false")
		}
	})
}
