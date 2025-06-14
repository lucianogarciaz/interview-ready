package main

import "math"

// Type: Tree / Binary Search Tree / Recursion
// Difficulty: Medium
// Companies: This is similar to LeetCode problem #98 "Validate Binary Search Tree".
// Commonly asked at companies like Google, Facebook, Amazon, and Microsoft.
// It tests understanding of BST properties and recursive tree traversal.

// left < root < right
//	      5
//	   /    \
//	  3      8
//   / \    / \
//  1   4  6   9

func validateBST(root *TreeNode) bool {
	if root == nil {
		return true
	}

	ok, _ := bstWithVals(root)
	return ok
}

func bstWithVals(root *TreeNode) (bool, int) {
	if root.Left == nil && root.Right == nil {
		return true, root.Val.(int)
	}

	if root.Left != nil {
		ok, left := bstWithVals(root.Left)
		if !ok || left > root.Val.(int) {
			return false, left
		}
	}
	var right int
	var ok bool
	if root.Right != nil {
		ok, right = bstWithVals(root.Right)
		if !ok || right < root.Val.(int) {
			return false, right
		}
	}

	return true, int(math.Max(float64(root.Val.(int)), float64(right)))
}
