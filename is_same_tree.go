package main

// Type: Binary Tree / Depth-First Search / Recursion
// Difficulty: Easy
// Companies: This is LeetCode problem #100 "Same Tree".
// Commonly asked at companies like Amazon, Microsoft, Facebook, and Google.
// Tests fundamental understanding of binary tree traversal and structural comparison.

func isSameTree(p *BinaryTreeNode, q *BinaryTreeNode) bool {
	if p == nil && q == nil {
		return true
	}

	if p == nil || q == nil || p.Val != q.Val {
		return false
	}

	if !isSameTree(p.Left, q.Left) {
		return false
	}

	if !isSameTree(p.Right, q.Right) {
		return false
	}

	return true
}
