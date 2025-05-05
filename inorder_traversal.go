package main

// * Definition for a binary tree node.
type BinaryTreeNode struct {
	Val   int
	Left  *BinaryTreeNode
	Right *BinaryTreeNode
}

func inorder(root *BinaryTreeNode) []int {
	if root == nil {
		return []int{}
	}
	results := inorder(root.Left)
	results = append(results, root.Val)
	results = append(results, inorder(root.Right)...)
	return results
}

//	{
//		name: "Example 1: Simple tree",
//		root: &BinaryTreeNode{
//			Val: 1,
//			Left: &BinaryTreeNode{
//				Val: 2,
//			},
//			Right: &BinaryTreeNode{
//				Val: 3,
//			},
//		},
//		expected: []int{1, 2, 3},
//	},
//
// [1 , 2 ,3 ]
func preOrderTraversal(root *BinaryTreeNode) []int {
	if root == nil {
		return []int{}
	}

	results := []int{root.Val} // [1, 2]
	results = append(results, preOrderTraversal(root.Left)...)
	results = append(results, preOrderTraversal(root.Right)...)

	return results
}

func postOrderTraversal(root *BinaryTreeNode) []int {
	if root == nil {
		return []int{}
	}
	results := postOrderTraversal(root.Left)
	results = append(results, postOrderTraversal(root.Right)...)
	results = append(results, root.Val)

	return results
}
