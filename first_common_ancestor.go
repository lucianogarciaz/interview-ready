package main

func firstCommonAncestor(root *TreeNode, p *TreeNode, q *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	if root == p || root == q {
		return root
	}

	left := firstCommonAncestor(root.Left, p, q)   // 2
	right := firstCommonAncestor(root.Right, p, q) // 3

	if left != nil && right != nil {
		return root
	}

	if left == nil {
		return right
	}

	return left
}
