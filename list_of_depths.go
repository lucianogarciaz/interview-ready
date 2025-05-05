package main

// Create an unbalanced tree:
//     1            // level = 0  [1]
//    / \
//   2   3         // level = 1 [2,3]
//  /
// 4              // level =2 [4]

// BFS

func listOfDepths(t *TreeNode) []*ListNode {
	if t == nil {
		return nil
	}
	first := &ListNode{
		Val: t.Val.(int),
	}
	mapOutput := map[int]*ListNode{
		0: first,
	}
	queue := []levelQueue{{Node: t.Left, Level: 1}, {Node: t.Right, Level: 1}}
	// queue       						mapOutput  		peak
	//{2.1,3.1}							{0:1}			2.1
	// {3.1, 4.2, nil.2}				{0:1, 1:2}
	// { 4.2, nil.2}					{0:1, 1:2-3}    3.1
	// {nil.2}											4.2
	for len(queue) > 0 {
		peak := queue[0]
		queue = queue[1:]
		if peak.Node == nil {
			continue
		}

		val, ok := mapOutput[peak.Level]
		node := &ListNode{
			Val: peak.Node.Val.(int),
		}
		if !ok {
			mapOutput[peak.Level] = node
		} else {
			head := val
			// move until the last element
			for val.Next != nil {
				val = val.Next
			}

			val.Next = node

			mapOutput[peak.Level] = head
		}

		if peak.Node.Right != nil || peak.Node.Left != nil {
			queue = append(queue, levelQueue{Node: peak.Node.Left, Level: peak.Level + 1}, levelQueue{Node: peak.Node.Right, Level: peak.Level + 1})
		}
	}

	output := []*ListNode{}
	for _, val := range mapOutput {
		output = append(output, val)
	}

	return output
}

type levelQueue struct {
	Node  *TreeNode
	Level int
}
