package main

// * Definition for a binary tree node.
type BinaryTreeNode struct {
	Val   int
	Left  *BinaryTreeNode
	Right *BinaryTreeNode
}

func inorderTraversal(root *BinaryTreeNode) []int {
	return recursive(root, []int{})
}

// [4]
func recursive(root *BinaryTreeNode, results []int) []int {
	if root == nil {
		return results
	}
	results = recursive(root.Left, results)
	results = append(results, root.Val)
	results = recursive(root.Right, results)
	return results
}
