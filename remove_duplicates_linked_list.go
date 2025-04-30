package main

//	4 -> 1 -> 3 -> 2 -> 1 -> 5  //
//	1 -> 2 -> 2 -> 2 -> 3
//
// NICE
func removeDuplicatesWithBuffer(head *ListNode) *ListNode {
	op := head
	setMap := map[int]bool{}
	for op != nil && op.Next != nil {
		setMap[op.Val] = true
		_, ok := setMap[op.Next.Val]
		if ok {
			op.Next = op.Next.Next // remove from the linked list.
			continue
		}

		op = op.Next
	}
	return head
}

func removeDuplicatesNoBuffer(head *ListNode) *ListNode {
	root := head

	for root != nil {
		removeDuplicatesLinkedList(root)

		root = root.Next
	}
	return head
}

func removeDuplicatesLinkedList(root *ListNode) {
	n := root
	p := root
	val := n.Val
	if n.Next == nil {
		return
	}

	n = n.Next
	for n != nil && p != nil {
		if val == n.Val {
			p.Next = p.Next.Next
			n = n.Next
			continue
		}

		n = n.Next
		p = p.Next
	}
}
