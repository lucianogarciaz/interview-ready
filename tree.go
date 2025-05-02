package main

type TreeNode struct {
	Val   any
	Left  *TreeNode
	Right *TreeNode
}

func Dfs(t *TreeNode) {
	if t == nil {
		return
	}

	Dfs(t.Left)
	// visit or do any calculations
	Dfs(t.Right)
}

func Bfs(t *TreeNode) {
	if t == nil {
		return
	}
	// create a queue
	queue := []*TreeNode{t}
	for len(queue) > 0 {
		// do any calculations
		t = queue[0]
		queue = queue[1:len(queue)]

		if t.Left != nil {
			queue = append(queue, t.Left)
		}
		if t.Right != nil {
			queue = append(queue, t.Right)
		}
	}
}
