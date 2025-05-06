package main

import "testing"

func TestListOfDepths(t *testing.T) {
	t.Skip()
	// Test case 1: Empty tree
	t.Run("empty tree", func(t *testing.T) {
		result := listOfDepths(nil)
		if len(result) != 0 {
			t.Error("Expected empty list for nil tree")
		}
	})

	// Test case 2: Single node tree
	t.Run("single node", func(t *testing.T) {
		root := &TreeNode{Val: 1}
		result := listOfDepths(root)
		if len(result) != 1 {
			t.Error("Expected one level for single node")
		}
		if result[0].Val != 1 {
			t.Error("Expected root value in first level")
		}
	})

	// Test case 3: Complete binary tree
	t.Run("complete binary tree", func(t *testing.T) {
		// Create a complete binary tree:
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

		result := listOfDepths(root)
		if len(result) != 3 {
			t.Error("Expected 3 levels for complete binary tree")
		}

		// Check first level (root)
		if result[0].Val != 1 {
			t.Error("Expected root value in first level")
		}

		// Check second level
		if result[1].Val != 2 || result[1].Next.Val != 3 {
			t.Error("Expected 2 and 3 in second level")
		}

		// Check third level
		if result[2].Val != 4 || result[2].Next.Val != 5 ||
			result[2].Next.Next.Val != 6 || result[2].Next.Next.Next.Val != 7 {
			t.Error("Expected 4, 5, 6, 7 in third level")
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

		result := listOfDepths(root)
		if len(result) != 3 {
			t.Error("Expected 3 levels for unbalanced tree")
		}

		// Check first level (root)
		if result[0].Val != 1 {
			t.Error("Expected root value in first level")
		}

		// Check second level
		if result[1].Val != 2 || result[1].Next.Val != 3 {
			t.Error("Expected 2 and 3 in second level")
		}

		// Check third level
		if result[2].Val != 4 {
			t.Error("Expected 4 in third level")
		}
	})
}
