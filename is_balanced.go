package main

import "math"

// Type: Binary Tree / Depth-First Search / Recursion
// Difficulty: Easy
// Companies: This is LeetCode problem #110 "Balanced Binary Tree".
// Commonly asked at companies like Amazon, Microsoft, and Google.
// It's also Exercise 4.4 in "Cracking the Coding Interview" book.
// Tests understanding of tree traversal and recursive depth calculation.

func isBalanced(root *TreeNode) bool {
	isBalanced, _ := isBalancedWithHeight(root)
	return isBalanced
}

func isBalancedWithHeight(root *TreeNode) (bool, int) {
	if root == nil {
		return true, 0
	}
	//     1
	//    / \
	//   2   3
	//  /
	// 4
	isBalanced, heightLeft := isBalancedWithHeight(root.Left)
	if !isBalanced {
		return isBalanced, 0
	}
	isBalanced, heightRight := isBalancedWithHeight(root.Right)
	if !isBalanced {
		return isBalanced, 0
	}

	height := math.Abs(float64(heightLeft - heightRight))
	if height >= 1 {
		return false, int(height) + 1
	}

	return true, int(math.Max(float64(heightLeft), float64(heightRight))) + 1

}

func checkBalanced(root *TreeNode) bool {
	if root == nil {
		return true
	}
	if root.Left == nil && root.Right == nil {
		return true
	}

	leftNode := heightImp(root.Left)
	rightNode := heightImp(root.Right)

	return math.Abs(float64(leftNode-rightNode)) < 1
}

func heightImp(root *TreeNode) int {
	if root == nil {
		return 0
	}
	heighLeft := heightImp(root.Left)
	heighRight := heightImp(root.Right)
	return int(math.Max(float64(heighLeft), float64(heighRight))) + 1
}
