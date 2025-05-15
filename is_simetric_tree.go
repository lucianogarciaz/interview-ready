package main

// Type: Binary Tree / Depth-First Search / Recursion
// Difficulty: Easy
// Companies: This is LeetCode problem #101 "Symmetric Tree".
// Commonly asked at companies like Amazon, Microsoft, Facebook, and Google.
// Tests understanding of tree traversal and mirror image comparison in trees.

func isSymmetric(root *BinaryTreeNode) bool {
	if root == nil {
		return true
	}

	return areTheSame(root.Left, root.Right)
}

func areTheSame(left *BinaryTreeNode, right *BinaryTreeNode) bool {
	if left == nil && right == nil {
		return true
	}

	if left == nil || right == nil || left.Val != right.Val {
		return false
	}

	if !areTheSame(left.Left, right.Right) {
		return false
	}

	if !areTheSame(left.Right, right.Left) {
		return false
	}
	return true
}
