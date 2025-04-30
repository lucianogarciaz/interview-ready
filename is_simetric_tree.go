package main

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}

	return areTheSame(root.Left, root.Right)
}

func areTheSame(left *TreeNode, right *TreeNode) bool {
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
