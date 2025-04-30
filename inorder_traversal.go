package main

// * Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	return recursive(root, []int{})
}

// [4]
func recursive(root *TreeNode, results []int) []int {
	if root == nil {
		return results
	}
	results = recursive(root.Left, results)
	results = append(results, root.Val)
	results = recursive(root.Right, results)
	return results
}
