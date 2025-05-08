package main

func closestNodes(root *TreeNode, queries []int) [][]int {
	output := [][]int{}
	result := inorder2(root)

	for _, q := range queries {
		left := 0
		right := len(result) - 1
		res := []int{-1, -1}
		for left <= right {
			pivot := (left + right) / 2
			if q == result[pivot] {
				res[0] = result[pivot]
				res[1] = result[pivot]
				break
			}
			if q > result[pivot] {
				res[0] = result[pivot]
				left = pivot + 1
			}

			if q < result[pivot] {
				res[1] = result[pivot]
				right = pivot - 1
			}

		}
		output = append(output, res)
	}

	return output
}

func inorder2(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	output := inorder2(root.Left)
	output = append(output, root.Val.(int))
	output = append(output, inorder2(root.Right)...)

	return output
}
